import os
import torch
import numpy as np
from tokenizers import SentencePieceBPETokenizer
from transformers import GPT2LMHeadModel
import random
from torch.utils.data import Dataset, DataLoader
from transformers import AdamW

class My_Dataset(Dataset):
    def __init__(self, tokenizer):

        self.data = []
        self.file = open("../data/dialog_single_turn.txt", 'r', encoding='utf-8')
        self.tokenizer = tokenizer

    def load_data(self):
        train_data_set = []
        while True:
            line = self.file.readline()
            if not line:
                break
            
            x = line.split('\t')
            Q, A = x[0], x[1]           
            A = A.rstrip('\n')

            train_data = '<s>' + Q + '</s>' + '<s>' + A + '</s>'
            train_data_set.append(train_data)

        tokenized_train_data = self.tokenizer.encode_batch(train_data_set)
      
        for single_data in tokenized_train_data:
            self.data.append(torch.tensor(single_data.ids).unsqueeze(0))

        self.file.close()

    def __len__(self):
        return len(self.data)

    def __getitem__(self,index):
        item = self.data[index]
        return item


def seed_everything(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)  # if use multi-GPU
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    np.random.seed(seed)
    random.seed(seed)        

def train():

  device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
 
  MODEL_NAME = "taeminlee/kogpt2"
  model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
  tokenizer = SentencePieceBPETokenizer("kogpt2/vocab.json", "kogpt2/merges.txt")

  model.to(device)

  tokenizer.add_special_tokens(["<s>", "</s>"])
  pad_id = tokenizer.token_to_id("<pad>")
  tokenizer.enable_padding(pad_id=pad_id, pad_token="<pad>")
  tokenizer.enable_truncation(max_length=128)
  
  train_dataset = My_Dataset(tokenizer=tokenizer)
  train_dataset.load_data()
  
  data_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
  optimizer = AdamW(model.parameters(), lr=5e-5, correct_bias=False, weight_decay=0.01)

  epochs = 4
  avg_loss = (0.0, 0.0)
  for epoch in range(epochs):
    count=0
    for data in data_loader:
        optimizer.zero_grad()
        data = data.transpose(1,0)
        data = data.to('cuda')
        model = model.to('cuda')
          
        outputs = model(data, labels=data)
        loss, logits = outputs[:2]
        loss = loss.to('cuda')
        loss.backward()
        avg_loss = (avg_loss[0] * 0.99 + loss, avg_loss[1] * 0.99 + 1.0)
        optimizer.step()
        if count % 10000 == 0:
            print('epoch no.{0}  train ({1}/{2})  loss = {3:.5f}  avg_loss = {4:.5f}' . format(epoch, count, len(data_loader), loss, avg_loss[0] / avg_loss[1]))
        count += 1
  torch.save(model.state_dict(), os.path.join(f'./best_model_kogpt', 'single_turn_model.bin'))

def main():
  train()

if __name__ == '__main__':
  seed_everything(42) 
  main()
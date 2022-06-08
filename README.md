## WERODA(위로다)
<a href="https://share.streamlit.io/jujeongho0/weroda/main/app.py" rel="nofollow"><img src="https://camo.githubusercontent.com/767be70c92254555bd347ab07908fec67854c2264b77702581bd230fd7eac54f/68747470733a2f2f7374617469632e73747265616d6c69742e696f2f6261646765732f73747265616d6c69745f62616467655f626c61636b5f77686974652e737667" alt="Open in Streamlit" data-canonical-src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" style="max-width: 100%;"></a>
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/jujeongho0/weroda)


#### Multi-Turn 기반의 심리상담 챗봇
#### KoGPT2 및 Elastic Search를 이용해 구현


<br>


## 💯 Feedback
<details markdown="1"> 
<summary> <b>프로젝트 피드백 접기/펼치기</b> </summary>

</br>

<details style='margin-left:20px !important'>
<summary> <b>정성준 멘토님</b> </summary>
    
</br>
 
>**5월 17일**     
>    
>- 심리상담 봇대화(심리상담)(어려움, 입력이 꼭 질문 만은 아님, dialogue 방법들 찾아보기, )
>    - 사용 시나리오 짜기(사용자 입력, 최종 아웃풋 등, 기존의 방법들과 차이점 생각해서)
>        - 시각화, 순서도 ..
>    - 각 팀원 역할, (PM역할 누구)
>    - 정량적 평가 방법 고민
>    - 일정 짜고, 일정에 따른 목표들
>    - 우리팀만의 아이디어를 살릴 수 있는 방법들 고민하기
>        - MBTI 한국어(일기...) 입력 → MBTI 예측(classfication?) 쉬운데, 번역한거 말고 한게 뭐야?
>        - 명언 생성, 테스크를 선택(쉬움, 명언생성, 인용구 생성)
>        - 관련 다른 데이터셋 더 찾아보기
>        - 부속, 질문이 들어오는데 질문에 혐오표현이 있을때 감지를 한다 (김성현 마스터 언스마일데이터셋, 순화는 못하고, 감지)


>**5월 26일**  
>    
>어떠한 과정을 거쳐서 결과를 내놓은 건지, 특정 상황에서 어째서 그런 판단과 결정을 내렸는지 항상 이유를 생각하고 기록하자.  
    
    
</details>

<details style='margin-left:20px !important'>
<summary> <b>오수지 멘토님</b> </summary>
    
</br>

>**5월 17일**
>
>안녕하세요 기원님! 연락주셔서 감사합니다!:booduck_happy:
>캐글에서 CC0 라이센스와 같이 상업적 사용이 허가된 데이터의 경우 한글로 번역한 다음 사용해도 무방한가요? ⇒ 사실 저도 저작권 관련한 부분은 잘 알지 못하지만, 상업적인 용도가 아닌
>이렇게 소규모 프로젝트의 경우 아마 웬만한 데이터들은 저작권 문제 걱정없이 사용 가능한 걸로 알고 있습니다. 그래도 혹시 모르니 정성준 멘토님께 한번 더 여쭤봐주세요...!
>
>혐오표현 감지 특정주제 QA → 어떤 서비스인지 감이 안 오네요.. 어떤 게 질문으로 주어지고 어떤 게 답변으로 나오는지 대략적으로 설명해주실 수 있을까요!? (특정 주제에 속하는 혐오표현 >span을 찾아내는 걸까요?) 혐오 표현 감지가 참 매력적인 분야이긴 한데 워낙 혐오표현 데이터로 진행되는 프로젝트들이 많다보니, 단순히 이중/다중분류를 넘어서 더 독창적인 아이디어가 필>요할 것 같습니다. 어떤 아이디어를 적용해볼 수 있을지 저도 더 고민해보겠습니다!+) 
>악성 채팅 관련해서 부캠 2기 이종혁 멘토님께서 수행하셨던 프로젝트를 (몰래) 공유드립니다!
>
> <https://docs.google.com/presentation/d/1NVaqXQ8ddHfszraarmLkI-_e3kXruzId/edit#slide=id.p1>
>
>회의 음성파일 텍스트로 변환하기 → 아마 아시겠지만 이미 클로바 노트에서 끝내주게 좋은 성능으로 제공하고 있어서, 아마 웬만한 성능으로는 눈에 띄기 힘들 것 같습니다..ㅠㅠ 그리고 음성>을 텍스트로 변환하는 부분은 공개된 stt api로 쉽게 가능할 것 같아서 텍스트로 변환한 후 클로바노트처럼 +a(핵심 키워드 추출 등)를 하지 않는 한 큰 메리트가 없을 것 같습니다.
>
>텍스트 압축/모델 경량화 → 모델 경량화에 관심이 있는 팀원들이 많을까요..? 아무래도 ‘모델 경량화'를 프로젝트로 하게 되면 그 분야의 취업을 타겟팅하게 되실텐데 제 기억상 1기에는 모델 >경량화 관련 취업 연계가 거의 없었습니다ㅠㅠ
>
>아마 정성준 멘토님께서 훨씬 좋은 피드백을 주시겠지만, 저한테도 언제든지 편하게 의견 여쭤보셔도 괜찮습니다! (뭐든지 앙상블이 성능이 좋기도 하고 저는 이런 아이디에이션 너무 좋아합니>다ㅎㅎ)
>그리고 지금 당장 주제를 정해지 못했다고 걱정 안 하셔도 될 것 같아요! 멘토 회의에서 나온 이야기를 짧게 말씀드리자면 생각보다 일찍 정하고 계속 뒤엎는 팀도 많다고 하더라구요. 이번주 >내로 주제 확정하고 데이터 수집 완료하는 걸 목표로, 한번에 똭 최고의 주제를 정해봐요ㅎㅎ 오늘도 화이팅하시길 바랍니다!:booduck_coding_no_bg:
 
</details>

<details style='margin-left:20px !important'>
<summary> <b>전종섭 멘토님</b> </summary>
    
</br>

> **5월 18일**
> 
> 지민님 질문 :
> 
> 1) 심리 상담 챗봇(ai허브 정신건강 상담 데이터셋)
> 
>       - 코로나로 우울한 현대인들을 위한 챗봇
>       - 이미 같은 데이터 사용하여 KoGPT2, KoELECTRA, KoBERT로 구현된 깃헙이 존재함
>       - 혐오 표현 필터링 or 단발성이 아닌 멀티턴 대화를 하는 등 차별점을 둬야 함 - 그러나 현재 저희 수준으로 멀티턴이 가능할지 미지수
> 
> 2) 명언 제조기 (책, 인용문 등 데이터셋)
> 
>       - 키워드 주면 명언 생성 or 유사도 높은 명언 반환
>       - 메일 등에 들어가는 명언을 찾는 사람들을 위한 서비스
> 
> 3) MBTI 예측
> 
>       - 캐글 영어 데이터셋 번역해서 사용
>           - MBTI 갤러리 등 한국어 데이터 수집 더 필요해 보임
>       - 짧은 글을 입력하면 AI가 MBTI 예측
>       - 글만 보고 MBTI 예측하기 좋아하는 사람들을 위한 서비스
>       - 어떤 근거로 예측했는지 밑줄 기능 구현가능하다면 추가
>       - 스무고개처럼 MBTI 맞히는 것도 가능하다면
> 
> 바쁘시겠지만, 주제에 대한 현실적인 피드백을 부탁드리고 싶습니다! 


>멘토님 답변 : 
>
>프로젝트에서 주제를 정하는 건 사실 어떤 걸 하든 크게 상관은 없습니다. 어려운 문제면 쉽게 풀면 되고, 쉬운 문제면 점진적으로 확장시킬 수 있거든요. 그런데 보통 의견이 나뉘는 이유는 >서로 프로젝트에 기대하는 목적이 다르기 때문이라고 생각합니다. 어떤 사람은 재미있는 프로젝트를 하고 싶어하고(3번 MBTI와 같이), 어떤 사람은 사회적으로 의미가 있는 프로젝트를 하고 >싶어하고(1번과 같이), 어떤 사람은 실제 사용자들이 많이 쓸법한 프로젝트를 하고 싶어합니다(2번). 사실 세 개의 접근 모두 틀린 게 없고 다른 것이기 때문에…
>
>우선 주제를 정하기에 앞서서 팀원들 전체가 어떤 프로젝트를 하고 싶어 하는지 정하면 좋을 것 같습니다. 여기서 새로운 주제를 정하기엔 조금 늦은 감이 있고 ㅎㅎ;
>
>3개 중 우리가 원하는 프로젝트의 목적은 무엇인지 정한 후 진행하면 될 것 같습니다!
>
>현재 정보를 기준으로는 시간과 노력을 고려해서 가장 현실적인 주제는 2번인 것 같습니다! 1번을 진행하시려면 처음부터 multi-turn보다는 single-turn → short-turn으로 점진적으로 확장>해 나가면 될 것 같아요. 3번은 재미는 있어 보이나 어떻게 단순화 시킬지는 잘 모르겠네요 ㅎㅎ;

</details>
</details>

</br>

## 👋 Team
|김남현|민원식|전태양|정기원|주정호|최지민|
|:-:|:-:|:-:|:-:|:-:|:-:|
|<img src='https://avatars.githubusercontent.com/u/54979241?v=4' height=80 width=80px></img>|<img src='https://user-images.githubusercontent.com/73579424/164642795-b5413071-8b14-458d-8d57-a2e32e72f7f9.png' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/55140109?v=4' height=80 width=80px></img>|<img src='https://user-images.githubusercontent.com/73579424/164643061-599b9409-dc21-4f7a-8c72-b5d5dbfe9fab.jpg' height=80 width=80px></img>|<img src='https://user-images.githubusercontent.com/73579424/164643280-b0981ca3-528a-4c68-9331-b8f7a1cbe414.jpg' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/97524127?v=4' height=80 width=80px></img>|
|[Github](https://github.com/NHRWV)|[Github](https://github.com/wertat)|[Github](https://github.com/JEONSUN)|[Github](https://github.com/greenare)|[Github](https://github.com/jujeongho0)|[Github](https://github.com/timmyeos)|
|Hate Speech Filtering<br>Data Collection|PM<br>Validation Server<br>Data Collection|EDA<br>Data Collection|Elastic Search<br>Text Style Transfer<br>Data Collection|Model Research<br>UI<br>Server Deploy|DialogBERT<br>Data Collection|
<br>

## File Structure
    ```
    .
    |-- README.md
    |-- code
    |   |-- app
    |   |   |-- app.py # KoGPT2 (Multi Downstream Task) 모델을 Streamlit으로 실행
    |   |   |-- app_kogpt_multi_turn.py # KoGPT2 (Multi-Turn) 모델을 Streamlit으로 실행
    |   |   |-- app_kogpt_single_turn.py # KoGPT2 (Single-Turn) 모델을 Streamlit으로 실행
    |   |   `-- app_roberta.py # RoBERTa 모델을 Streamlit으로 실행
    |   |-- best_model # KoGPT2 (Multi Downstream Task) 모델의 parameter와 config가 저장되는 장소
    |   |   |-- README.md
    |   |   `-- config.json
    |   |-- kogpt2 # SentencePieceBPETokenizer를 load하는데 필요한 파일
    |   |   |-- merges.txt
    |   |   `-- vocab.json
    |   |-- model # KoGPT2 (Multi-Turn / Single-Turn), RoBERTa 모델의 parameter가 저장되는 장소
    |   |   `-- README.md
    |   `-- train
    |       |-- train.py # KoGPT2 (Multi Downstream Task) 모델 학습
    |       |-- train_kogpt_multi_turn.py # KoGPT2 (Multi-Turn) 모델 학습
    |       |-- train_kogpt_single_turn.py # KoGPT2 (Single-Turn) 모델 학습
    |       |-- train_roberta.py # RoBERTa 모델 학습
    |       `-- unsmile_filter.py # 스마일게이트의 혐오 표현 감지 모델 load
    |-- data
    |   |-- answer_total.json # Elastic Search의 검색 대상 데이터셋
    |   |-- chatbot_dataset.csv # KoGPT2 (Multi Downstream Task) 모델 학습 데이터셋
    |   |-- dialog_multi_turn.csv # KoGPT2 (Multi-Turn) 모델 학습 데이터셋
    |   |-- dialog_single_turn.csv # KoGPT2 (Single-Turn) 모델 학습 데이터셋
    |   |-- idx2label.json
    |   |-- label2answer.json
    |   `-- wellness_dialog_for_text_classification.txt # RoBERTa 모델 학습 데이터셋
    |-- elasticsearch
    |   |-- README.md # elastic search 설치법
    |   `-- elastic.ipynb # elastic search 사용법
    `-- requirements.txt
    ```
<br>

## How to run
```
git clone https://github.com/boostcampaitech3/final-project-level3-nlp-10.git
pip install -r requirements.txt
cd app
streamlit run {app} --server.port {포트번호}
```       
<br>

## Dataset
- [[KETI] 웰니스 대화 스크립트 데이터셋](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-006)
    - 정신 건강 상담 주제의 359개 대화 의도에 대한 5,232개의 사용자 발화 및 1,023개의 챗봇 발화
    - KoGPT2 모델 학습, Retrieval 데이터셋 구축에 사용
- [[songys/Chatbot_data] Chit-Chat 데이터셋](https://github.com/songys/Chatbot_data)
    - 다음 카페 "사랑보다 아름다운 실연([http://cafe116.daum.net/_c21_/home?grpid=1bld](http://cafe116.daum.net/_c21_/home?grpid=1bld))"에서 자주 나오는 이야기들을 참고하여 제작
    - 챗봇 학습용 문답 페어 11,876개
    - 일상 0, 이별(부정) 1, 사랑(긍정) 2로 라벨링
    - Retrieval 데이터셋 구축에 사용
- [[AI-Hub] 감성 대화 말뭉치](https://aihub.or.kr/aidata/7978)
    - 60가지 다양한 감정의 코퍼스 27만 문장
    - 우울증 관련 및 대화 응답 시나리오 포함
    - 감성 대화 엔진 또는 챗봇을 개발하려는 목적에 맞추어 제작
    - 형태소 단위의 세부 태깅을 하지 않고 문장 단위의 정합성만 검수하면 데이터 모델링에 큰 문제가 없으며, 문장에서 의미와 의도를 추출하는 확률이 기존 통계 모델링 기법(CRF+ 등)에 비해 월등히 높은 성능을 보여줌
    - Retrieval 데이터셋 구축에 사용
<br>

## Model
- KoGPT2 (Multi DownStream Task)
    ![1](https://user-images.githubusercontent.com/62659407/172053006-fab0eb7a-d7b5-4bb6-a2de-9b9deb777261.png)

    - 다양한 DownStream Task를 수행할 수 있는 GPT2의 장점을 이용 → Question으로 심리상담 주제 분류와 Answer 생성을 동시에!
    - 심리상담 데이터는 Wellness DataSet, 일상 대화 데이터는 Chit-Chat DataSet을 이용
        - Wellness DataSet2에서 챗봇의 답변에 대한 응답 데이터는 <긍정답변>과 <부정답변>으로 전환 → Multi-Turn 대화에서 사용
        ![1 (1)](https://user-images.githubusercontent.com/62659407/172053018-2ee6fef2-8dfa-4642-b29f-64685db847dc.png)

    - Auto-Regressive
        ![1 (2)](https://user-images.githubusercontent.com/62659407/172053056-f376ca43-698b-43ac-8c13-ddc92763f8c1.png)

        - GPT2는 이전 토큰들을 이용해 다음 토큰을 예측 → Question 뿐만 아니라, 예측한 심리상담 주제를 이용해 Answer을 생성 → 문맥에 맞는 Answer 생성

    - Multi-Turn
        ![1 (3)](https://user-images.githubusercontent.com/62659407/172053076-f0dfdb4d-75d0-4104-9ee8-7e4a24332c76.png)

        - Question을 긍정 답변 및 부정 답변으로 예측했을 때, 사용자의 이전 Question을 추가해 다시 Task 진행 → 연속한 대화 수행 가능

    - Beam Search
        ![1 (4)](https://user-images.githubusercontent.com/62659407/172053095-70c1887c-00e0-4ed0-92cb-2f67ce024ab5.png)

        - Task를 여러 번 수행하여 최다 예측된 심리상담 주제의 Answer을 최종 답변으로 추출 → Answer의 정확도 향상

    - Retrieve
        ![1 (5)](https://user-images.githubusercontent.com/62659407/172053102-3a642ab0-e99b-4852-9da4-1e9ecb6ed488.png)

        - GPT 계열의 생성 모델의 특성 상 Answer의 완성도가 떨어져 챗봇의 성능 하락을 야기

        ![1 (6)](https://user-images.githubusercontent.com/62659407/172053119-249763b3-0eea-4515-a6bc-5ff8662df2f4.png)

        → Answer Dataset을 구축하여 Elastic Search의 BM25 Retrieval을 이용해 생성된 Answer과 가장 유사한 답변을 Answer Dataset에서 추출하여 답변으로 채택

    - Conclusion
        ![1 (7)](https://user-images.githubusercontent.com/62659407/172053132-442b2dc4-c8cc-4e0f-854f-c6abadf036f6.png) 

        - 위의 기능들을 모두 결합하고 발전시켜 다음과 같은 과정으로 최종 답변으로 선택
            1. KoGPT2: Question을 이용해 심리상담 주제와 Answer을 5번 생성
            2. Beam Search: 최다 예측된 심리상담 주제의 답변을 채택 → 답변 후보에 추가
            3. Retrieve: 채택된 답변과 유사한 답변을 Answer Dataset에서 5개 검색 → 유사도 점수가 10점 이상인  유사 답변을 답변 후보에 추가
            4. Count: 답변 후보에서 최다 빈도의 답변을 최종 답변으로 선택
<br>

## WorkFlow
![1 (8)](https://user-images.githubusercontent.com/62659407/172053145-98ba7b1b-56e5-460c-a388-540f75669fac.png)

1. 사용자가 Question을 입력
2. Korean UnSmile Dataset으로 학습한 혐오 표현 필터링 모델을 통해 Question의 혐오 표현 점수 확인 → 0.1점 미만이면, 혐오 표현으로 간주해 사용자에게 ‘순화된 표현을 사용하세요’  경고 및 Question 재입력 요구
3. Model을 이용해 Question에 대한 적절한 Answer 생성 및 출력
4. Streamlit을 이용해 위 과정을 Chatting 형태의 Web 구현
<br>

## Validation
- 모델 성능 평가 지표 (SSA)
    - 2020년 구글이 챗봇 Meena를 발표하면서 도입한 대화 만족도 평가 지표
    - Sensibleness : 답변의 맥락과 논리성 평가
    - Specificity : 답변의 구체성과 사람과의 유사성 평가
    - e.g. 너 중국 음식 좋아해?

        → 오늘 메뉴가 뭔가요? (Sensibleness :0, Specificity: 0)

        → 응, 좋아해. (Sensibleness :1, Specificity: 0)

        → 응, 난 그 중에 ‘짜장면이’ 제일 좋아. (Sensibleness :1, Specificity: 1)


- 작업자 간 일치도 평가
    - 구글 Meena 발표 논문의 작업자 간 일치도 평가 방법을 참조
    - Krippendorff’s alpha : 0~1 사이의 값(0 불일치, 1 일치)을 가짐
    - Agreement는 SSA 계산을 위해 사용.
    ![1 (9)](https://user-images.githubusercontent.com/62659407/172053157-6a90fb70-702f-4c29-94aa-dfdc7f8b25fd.png)

    ⇒ 팀의 작업자 간 일치도 평가 점수가 구글 Meena 발표 논문보다 높음 → 팀의 평가 일치도 ↑


- 모델 별 성능 평가
    - 모델 성능
        - Sensibleness: 66.60
        - Specificity: 59.39
        - SSA: 62.99

    - 다른 모델과 비교
        ![1 (10)](https://user-images.githubusercontent.com/62659407/172053172-3ae29b04-9242-4e76-b7d0-b2bebb270586.png)
<br>

## Demo
![KakaoTalk_20220605_192331995](https://user-images.githubusercontent.com/62659407/172053397-11044ee5-d7a5-4b1d-adcb-aea95e954d38.gif)


## Korean UnSmile Dataset
```
@misc{SmilegateAI2022KoreanUnSmileDataset,
  title         = {Korean UnSmile dataset: Human-annotated Multi-label Korean Hate Speech Dataset},
  author        = {Seonghyun Kim},
  year          = {2022},
  howpublished  = {\url{https://github.com/smilegate-ai/korean_unsmile_dataset}},
}
```

# NaverWebtoon_Recommendation
데이터사이언스개론 - 최종프로젝트 (TF-IDF 모델을 이용한 장르기반 네이버 웹툰 추천 서비스)


현재 연재중인 (2022.12.08 기준) 월요일 ~ 일요일 웹툰 584편을 크롤링함.

![image](https://github.com/spolice0324/NaverWebtoon_Recommendation/assets/82880442/11b4466f-80e5-4ee6-af78-3220da545cdf)

## 🔍 Description

**데이터사이언스개론 - 최종프로젝트 (TF-IDF 모델을 이용한 장르기반 네이버 웹툰 추천 서비스)**

- kaggle에서 찾은 **네이버웹툰**에서 서비스되는 2100편 이상의 웹툰들과 **네이버 베스트도전**의 3100편 이상의 웹툰들에 대한 데이터셋을 통해 원하는 데이터를 가공하여 추천 서비스를 만들었다.
- 현재 연재중인 (2022.12.08 기준) 월요일 ~ 일요일 웹툰 584편 데이터 크롤링 과정, 데이터 가공 과정 전반에 참여했다.
- 정확도를 향상시키기 위해 TF-IDF 모델을 이용하여 웹툰 시놉시스와 시나리오를 읽고 장르기반 추천 서비스를 만드는데 기여했다.

## 📜 Contents

한국콘텐츠진흥원 실태조사에 따르면 웹툰 선택 기준 중 ‘소재와 줄거리’가 35.7%로 높은 비중을 차지하고 있음을 알 수 있다.  하지만 웹툰 플랫폼에서는 장르별로 웹툰을 구분해주지만 비슷한 시놉시스로 묶는 기능이 없어, 시놉시스가 비슷한 웹툰을 추천해주는 기능을 구현하고자 했다. 

✅ **Core Role** **-**  **NaverWebtoon Web Data Crawling , Data Analysis(EDA) , Data Extracting**

## ⛏️ Develop Growing Points

### 📈 웹 크롤링


![image](https://github.com/spolice0324/NaverWebtoon_Recommendation/assets/82880442/92b9856f-18dd-4c37-b34e-258162c48da7)

- 크롤링 코드를 작성하여 네이버 웹툰 사이트 https://comic.naver.com/webtoon/weekday 에 접근하여 정보를 수집하였습니다.
- 자연어 처리에서 크롤링으로 얻어낸  데이터를(tokenization) & 정제(cleaning) & 정규화(normalization)하는 전처리를 진행했습니다.

### 📊 EDA

![image](https://github.com/spolice0324/NaverWebtoon_Recommendation/assets/82880442/ebefeba8-adf6-42da-b77c-36f0408cc388)
![image](https://github.com/spolice0324/NaverWebtoon_Recommendation/assets/82880442/5086c15c-f901-4972-9b4b-a6d1eed10cad)

장르별 작품수를 분석하고 구성방식 별, 장르별로 구분하여 데이터를 추출하여 정리했습니다. 

### 🧠 Deep Learning

![image](https://github.com/spolice0324/NaverWebtoon_Recommendation/assets/82880442/cd77e933-11f3-462f-b272-70d007d41172)

- 단어의 빈도와 역 문서 빈도를 사용하여 DTM 내의 각 단어들마다 중요한 정도를 가중치로 주는 방법인 TF-IDF(Term Frequency- Inverse Document Frequency)를 사용하여 텍스트 분석을 진행했습니다.
- konlpy 형태소 분석기를 사용하여 토큰화를 진행했습니다.
- StopWord를 지정하여 허수 형태소를 처리했습니다.


### 🖥️ Service

![image](https://github.com/spolice0324/NaverWebtoon_Recommendation/assets/82880442/926f984e-12d9-450e-a99d-05d25804a8ef)
![image](https://github.com/spolice0324/NaverWebtoon_Recommendation/assets/82880442/4e48ab8e-9c2c-4d94-84d1-7a4f132ec32a)
![image](https://github.com/spolice0324/NaverWebtoon_Recommendation/assets/82880442/3e03a74f-a53a-4ee7-be13-e0603e391289)

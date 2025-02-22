# Data_Mining
- 2024 -1 데이터 마이닝 수업
- 사용교재 : 데이터 과학 기반의 파이썬 빅데이터 분석 / 이지영 / 한빛아카데미

## 목차





## Data_Crawling
### NaverAPI Crawling
- 목표 : 네이버 API기반 크롤링 

### PublicAPI Crawling - tour
- 목표 : 공공데이터 API기반 크롤링
- 데이터 : 공공데이터포털의 '출입국관광통계서비스'

### StaticWeb Crawling - HollysCoffee
- 목표 : 정적 웹페이지 크롤링
- 데이터 : 할리스 커피 사이트에서 매장이름, 주소, 전화번호 추출
- BeautifulSoup 이용

### DynamicWeb Crawling - CoffeeBean
- 목표 : 동적 웹페이지 크롤링
- 커피빈 사이트에서 매장이름, 주소, 전화번호 추출
- BeautifulSoup 이용








## Statistical_Analysis 통계 분석

### wine_quality_prediction
- 목표 : 와인 속성을 분석하여 품질 등급을 예측
- 핵심개념 : 기술통계, 회귀분석, t검정, 히스토그램
- matplotlib, seaborn, scipy 이용

### titanic_survival_analysis
- 목표 : 타이타닉호 승객 변수를 분석하여 생존율과의 상관관계를 찾는다.
- 핵심개념 : 상관분석, 상관계수, 피어슨 상관계수, 히트맵
- seaborn, pandas 이용


## Text_Analysis 텍스트 빈도 분석

### news_text_analysis
- 한글 뉴스 기사의 키워드 분석하기
- 목표 : '4차 산업혁명'에 관한 한글 기사에서 명사 키워드를 분석한다.
- 핵심개념 : 형태소 분석, 품사 태깅
- 데이터 : 4차 산업혁명 기사. 페이스북 전자신문 페이지에서 크롤링하여 저장한 json 파일

### RISS_article text_analysis
- 목표 : 'big data' 에 관한 RISS 논문에서 명사 키워드를 분석한다.
- 핵심개념 : 형태소 분석, 품사 태깅
- pandas, glob, nltk, matplotlib, wordcloud 이용









## Geographic_Analysis

### Coffeebean_geomap
- 커피빈매장 정보 분석 후 맵 생성 
- 목표 : 커피빈 매장 주소의 지리 정보인 지오 데이터를 분석한 후 지도에 시각화하여 나타내기
- 핵심개념 : GPS 좌표 구하기, 지리정보 시각화 라이브러리 
- folium, pandas 이용

### korea_medical_center_geomap
- 행정구역별 의료기관 현황 분석 
- 목표 : 행정구역별로 공공보건의료기관 수를 파악하고, 인구수 대비 공공보건의료기관 비율을 비교분석. 분석결과는 블록맵으로 시각화함
- 핵심개념 : 블록맵
- 데이터 수집 : 공공보건의료기관현황
- ggplot, matplotlib 사용







## Classification_Analysis

### breast_cancer_diagnosis
- 특징 데이터로 유방암 진단하기 
- 목표 : 유방암 특징을 측정한 데이터에 로지스틱 회귀 분석을 수행하여 유방암 발생을 예측
- 핵심 개념 : 로지스틱 회귀, 시그모이드 함수, 성능평가 지표, 오차행렬, 정밀도, 재현율, F1스코어, ROC기반 AUC스코어
- 데이터 : 유방암진단 데이터 - 사이킷런 내장 데이터
- 결과분석 : 성능평가 지표 계산 - confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

### movement_sensor_analysis
- 센서 데이터로 움직임 분류하기 
- 목표 : 스마트폰에서 수집한 센서 데이터를 분석하여 사람의 움직임을 분류 하는 모델을 생성. 새로운 데이터에 대해 움직임 유형을 예측해서 분류
- 핵심개념 : 핵심개념 : 결정트리, 정보이득지수, 지니계수
- numpy, pandas, sklearn, seaborn, matplotlib, Graphviz 이용







## Cluster_Analysis

### consumer_clustering
- 타깃마케팅을 위한 소비자 군집분석하기 
- 목표 : k-menas 으로 온라인 판매 데이터를 분석한 후 타깃 마케팅을 위한 소비자 군집을 만듬
- 핵심개념 : 타겟마케팅, 비지도학습, 군집화, K-평균, 엘보우방법, 실루엣분석
- pandas, math, matplotlib, seaborn, numpy, sklearn.cluster, sklearn.metrics






## Regression-Analysis

### home price prediction
- 환경에 따른 주택 가격 예측하기
- 목표 : 보스턴 주택 가격 데이터에 머신러닝 기반의 회귀 분석을 수행. 주택 가격에 영향을 미치는 변수를 확인하고 그 값에 따른 주택 가격을 예측
- 머신러닝, 지도학습, 사이킷런, 사이킷런 내장 데이터셋, 분석평가지표

###  fuel efficiency prediction
- 항목에 따른 자동차 연비 예측하기 
- 목표 : 자동차 연비 데이터에 머신러닝 기반의 회귀 분석을 수행/ 연비에 영향을 미치는 항목을 확인하고, 그에 따른 자동차 연비를 예측



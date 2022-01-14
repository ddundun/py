# python, mldl, flask, django, spring같은거

import numpy as np
import pandas as pd  # csv, json, xml파일 등 읽을 수 있는 라이브러리
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

import matplotlib.pyplot as plt

fish = pd.read_csv('https://bit.ly/fish_csv_data')
# print(fish.head()) #head ->5개의 데이터 출력
# print(fish)  # 159 rows * 6 colums
#
# print(pd.unique(fish['Species']))  # unique함수 len으로 감싸면 개수 알수있음. 7개의종

fish_input = fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()
fish_target = fish['Species'].to_numpy()

print(fish_input.shape) # 159,5 //2차원데이터 안에 1차원데이터
print(fish_target.shape) #159행 //1차원 데이터

# 데이터를 맞춰줘야 함. 학습시키려면..ㅎ
# 75퍼비율과 25퍼 비율로 맞추기?

train_input, test_input, train_target, test_target = train_test_split(fish_input,fish_target,random_state=42)

print(train_input.shape) #119,5
print(test_input.shape) #40,5

print(train_target.shape) #119 75퍼
print(test_target.shape) #40  25퍼?

print(train_input[:5]) #변환 전값..
#standardscaler사용하면 표준편차이용한값으로바뀜 (?)
ss = StandardScaler() #변환기 // PolynomalFeatures: 열의 개수 늘리기

ss.fit(train_input,train_target) #학습

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

print(train_scaled[:5]) #첫줄에서 얼만큼 떨어져있는가...(?)

train_score = []
test_score = []
for hip in range(1,6):
    knclf = KNeighborsClassifier(n_neighbors=hip)
    knclf.fit(train_scaled,train_target)

    ta_score = knclf.score(train_scaled,train_target)
    te_score = knclf.score(test_scaled,test_target)
    train_score.append(ta_score)
    test_score.append(te_score)

    # print(train_score) #훈련데이터
    # print(test_score) #학습데이터?
# plt.plot(train_score)
# plt.plot(test_score)
# plt.show()


knclf = KNeighborsClassifier(n_neighbors=3)
knclf.fit(train_scaled,train_target)

print(knclf.classes_)
proba = knclf.predict_proba([test_scaled[3]])# 나머지가 될 확률 0,
# Perch 0.66667 Roach 0.33333 // 이웃된거 세개중에 두개, 세개중에 한개 .
# print(proba)
print(np.round(proba,decimals=5)) #5번째에서 반올림

dis, indexes = knclf.kneighbors([test_scaled[3]])
print(train_target[indexes]) #'Roach' 'Perch' 'Perch' 인접한 세개의 값

# 로지스틱회귀: 음의 무한대로 갈수록 0이고, 양의무한대로 갈수록 1이다.
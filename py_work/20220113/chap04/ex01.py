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
# plt.xlabel('n_neighbors') 0?1?
# plt.ylabel('scores')
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

# 로지스틱회귀: 음의 무한대로 갈수록 0이고, 양의무한대로 갈수록 1이다. ??? 시그모이드는 또 뭐여 ㅜ

 # z = a * 무게 +b * 길이+c * 대각선+d * 높이+e * 넓이
# z = np.arange(-5,5,0.1) // a*x + b*y + c*z = z
# phi = 1/(1+np.exp(-z)) 시그모이드함수 ..
#
# plt.plot(z,phi)
# plt.xlabel('z')
# plt.ylabel('phi')
#
# plt.show()

# 인덱싱(하나하나 가리키는것), 슬라이싱[:]
# char_arr = np.array(['A','B','C','D','E'])
# print(char_arr[[True,False,True,False,False]]) # True인 것 출력 a,c
#
# ary = np.array([1,2,3,4,5])
# print(ary[[True,False,True,True,False]]) #1,3,4

bream_smelt_indexes = (train_target =='Bream') | (train_target =='Smelt')
# print(bream_smelt_indexes) #bream이거나 smelt인것

train_bream_smelt = train_scaled[bream_smelt_indexes] # bream과 smelt의 특성값 5개씩 있는 x 119
target_bream_smelt = train_target[bream_smelt_indexes] # bream과 smelt의 특성값 5개씩 있는 x 40

print(train_bream_smelt.shape)
print(target_bream_smelt.shape)

from sklearn.linear_model import LogisticRegression

#bream smelt (브림스멜트만분류) 이진분류..
lr = LogisticRegression()
lr.fit(train_bream_smelt,target_bream_smelt)

predvalue = lr.predict(train_bream_smelt[:5])
print(train_bream_smelt[:5]) #표준편차로 변경
print(predvalue)

predprovalue = lr.predict_proba(train_bream_smelt[:5])
print(predprovalue)

'''
    학습기를 통해서 학습을 하고.. 그 예측값이 제일 정확한 것을 찾는거를 개발하는 학분
'''
print("차수 가중치","절편 바이러스")
print(lr.coef_,lr.intercept_) #절편?

z값들 = lr.decision_function(train_bream_smelt[:5])
# print(z값들[0],z값들[1],z값들[3])
from scipy.special import expit
print(expit(z값들))

lr = LogisticRegression(C=20, max_iter=1000) # 규제 20?
lr.fit(train_scaled, train_target)

print(lr.score(train_scaled,train_target))
print(lr.score(test_scaled,test_target))

print(lr.predict(test_scaled[:5]))

proba = lr.predict_proba(test_scaled[:5]) #
print(np.round(proba,decimals=3))

z값들 = lr.decision_function(test_scaled[:5])
print(z값들)

from scipy.special import softmax

proba = softmax(z값들, axis=1) #softmax함수 통과하게되면
print(np.round(proba,decimals=3)) #점수로변한다?

'''
    -딥러닝-
    activate  활성화..
    엄청큰수나오더라도 ->시그모이드통과-> 0 or 1 -> 양의무한대수..1 음의무한대수..0
    계산적게하기때문에 사용
    
    시그모이드  
    음성데이터, 양성데이터
    imdb 리뷰데이터.. 영화리뷰..
    좋아요, 싫어요 ..
    좋 0 싫 1
    
    
    소프트맥스
    이미지데이터
    바지, 원피스, 구두, 운동화
    
'''
# -*- coding: utf-8 -*-

import pandas as pd

X = pd.DataFrame()

print(X)
print(X.info())

X['gender'] = ['F','M','F','F','M']
print(X)

X['age'] = [15, 35, 25, 37, 55]
print(X)

# 데이터 전처리
# 1. 문자열
# - 결측 데이터
# - 라벨 인코딩
# - 원핫 인코딩

# 2. 수치형
# - 결측 데이터
# - 이상치 제거(대체)
# - 스케일링

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler

<<<<<<< HEAD
#sparse는 희소행렬, handle_unkown은 모르는 값 왔을 때 그냥 무시하기.
=======
>>>>>>> 33070394b66d27e6418adbff09f9d7ccb8ba3c45
encoder = OneHotEncoder(sparse=False,
                        handle_unknown='ignore')

scaler = MinMaxScaler()

from sklearn.compose import ColumnTransformer

obj_columns=['gender']
num_columns=['age']

ct = ColumnTransformer(
    [('scaler',scaler,num_columns),
     ('encoder',encoder,obj_columns)])
<<<<<<< HEAD
# age   F    M
# [[0.   1.   0.  ]
# [0.5  0.   1.  ]
# [0.25 1.   0.  ]
# [0.55 1.   0.  ]
# [1.   0.   1.  ]]
=======
>>>>>>> 33070394b66d27e6418adbff09f9d7ccb8ba3c45

ct.fit(X)

print(X)
print(ct.transform(X))









# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

X = pd.DataFrame()

print(X)
print(X.info())

# 문자의 none은 괜츈하지만 수치형의 none은 안괜찮다. 
X['gender'] = ['F','M','F','F', None] #바뀐부분-None 
print(X)

X['age'] = [15, None, 25, 37, 55] #바뀐부분-None
print(X)

print(X.info())
print(X.isnull().sum())

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
# 결측데이터를 처리해주는 전처리 클래스
from sklearn.impute import SimpleImputer

encoder = OneHotEncoder(sparse=False,
                        handle_unknown='ignore')

scaler = MinMaxScaler()

# 수치형 데이터
imputer_num = SimpleImputer(
    missing_values=np.nan, # 결측데이터라고 생각하는 것을 적으세요=>np의 nan
    strategy='mean') # 평균, 다른걸로는 median, most_frequent,constant등이 올 수 있다.

# 문자형 데이터
imputer_obj = SimpleImputer(
    missing_values=None, # None을 직접 선택, np.nan이랑 None은 좀 달라서 잘 못 인식할 수 있음
    strategy='most_frequent') # 최빈도값

# 결축 처리후 스케일 처리
from sklearn.pipeline import Pipeline
num_pipe = Pipeline(
    [('imputer_num',imputer_num), #결측 먼저
     ('scaler',scaler)])

obj_pipe = Pipeline(
    [('imputer_obj',imputer_obj), #결측 먼저
     ('encoder',encoder)])

from sklearn.compose import ColumnTransformer

obj_columns=['gender']
num_columns=['age']

ct = ColumnTransformer(
    [('num_pipe',num_pipe,num_columns),
     ('obj_pipe',obj_pipe,obj_columns)])

ct.fit(X)

print(X)
print(ct.transform(X))








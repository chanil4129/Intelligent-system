# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names) 
y = pd.Series(data.target)

print(X.info())

print(X.describe())


# 데이터 전처리
# 1. 문자열
# - 결측 데이터
# - 라벨 인코딩 - 메달 처럼 차별을 줘야할 때
# - 원핫 인코딩 - 대부분의 경우

# 2. 수치형
# - 결측 데이터
# - 이상치 제거(대체) - 사기꾼 고르기 거래에서 사기거래에 대한 사기 이상치만 제거했더니 좋은 결과..
# - 스케일링

# pandas 쓰다가 scikit learn쓰면 numpy로 바뀌어서 다시 pandas 데이터 프레임 맞추는거 상당히 힘듦...

# - 전처리 클래스 로딩
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

# - 전처리를 적용할 컬럼을 식별
num_columns = X.columns

# 전처리를 지원하는 클래스
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(
    [('scaler', scaler, num_columns)])
# scikit learn에서 예제코드 slice(2,4)는 2,3컬럼 쓰겠다는 거임
ct.fit(X)

print(X.head())
print(ct.transform(X)[:5])













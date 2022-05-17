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
<<<<<<< HEAD
# - 라벨 인코딩 - 메달 처럼 차별을 줘야할 때
# - 원핫 인코딩 - 대부분의 경우

# 2. 수치형
# - 결측 데이터
# - 이상치 제거(대체) - 사기꾼 거래에서 사기꾼에 대한 이상치만 제거했더니 좋은 결과..
# - 스케일링

# pandas 쓰다가 scikit learn쓰면 numpy로 바뀌어서 다시 pandas 데이터 프레임 맞추는거 상당히 힘듦...

=======
# - 라벨 인코딩
# - 원핫 인코딩

# 2. 수치형
# - 결측 데이터
# - 이상치 제거(대체)
# - 스케일링

>>>>>>> 33070394b66d27e6418adbff09f9d7ccb8ba3c45
# - 전처리 클래스 로딩
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

# - 전처리를 적용할 컬럼을 식별
num_columns = X.columns

<<<<<<< HEAD
# 전처리를 지원하는 클래스
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(
    [('scaler', scaler, num_columns)])
# scikit learn에서 예제코드 slice(2,4)는 2,3컬럼 쓰겠다는 거임
=======
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(
    [('scaler', scaler, num_columns)])
>>>>>>> 33070394b66d27e6418adbff09f9d7ccb8ba3c45
ct.fit(X)

print(X.head())
print(ct.transform(X)[:5])













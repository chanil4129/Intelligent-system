# -*- coding: utf-8 -*-

# 1_cross_validation.py
# 교차검증 - 학습 시킨것이 올바른 결과인가? 검증하는 것.
# 교차검증을 하는 이유는 이 예제에서 학습 과정에서의 문제점 때문임
# 머신러닝은 데이터에 굉장히 민감한데 random_state값을 바꾼다고 가정하면
# 분할 결과에 따라 학습 결과가 좋을 수 있고, 나쁠 수 있다.

# 머신러닝을 사용하여 데이터를 분석하는 과정
# 1. 데이터 셋 로딩
from sklearn.datasets import load_breast_cancer
X, y = load_breast_cancer(return_X_y=True)

# 2. 데이터의 전처리
# - 라벨 데이터 인코딩!
# - 원핫인코딩
# - 특성 확장
# ...

# 3. 데이터 셋의 분할
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(
    X, y,
    test_size=0.3,
    stratify=y,
    random_state=1)

# 2. 데이터의 전처리
# - 스케일 처리
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. 머신러닝 모델의 학습
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(
            C=1.0,
            n_jobs=-1,
            random_state=1).fit(X_train_scaled,y_train)

# 5. 머신러닝 모델의 평가
# - 모델의 평가 기준(테스트 데이터 셋이 사용)
score = model.score(X_train_scaled, y_train)
print(f'(MODEL) TRAIN SCORE : {score}')

score = model.score(X_test_scaled, y_test)
print(f'(MODEL) TEST SCORE : {score}')











# -*- coding: utf-8 -*-

import pandas as pd
pd.options.display.max_columns=100
pd.options.display.max_rows=10

from sklearn.datasets import load_boston

data=load_boston()

print(data.keys())

X=pd.DataFrame(data.data,columns=data.feature_names)
y=pd.Series(data.target)

X.info()
X.describe()
print(X.isnull())
print(X.isnull().sum())

X.head()
y.head()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1)

from sklearn.ensemble import GradientBoostingRegressor

model=GradientBoostingRegressor(n_estimators=100,
                                learning_rate=0.1,
                                subsample=1.0,
                                max_depth=3,
                                random_state=1,
                                max_features=None,
                                alpha=0.9)

model.fit(X_train,y_train)

score=model.score(X_train,y_train)
print(f'score (train) : {score}')
score=model.score(X_test,y_test)
print(f'score (test) : {score}')
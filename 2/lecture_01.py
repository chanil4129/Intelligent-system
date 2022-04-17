# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.datasets import load_iris

iris=load_iris()
iris.keys()
iris.data
iris.target

df=pd.DataFrame(iris.data,columns=iris.feature_names)
df.head()
df.tail()
df['target']=iris.target
df.head()
df.info()
df.describe()




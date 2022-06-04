# -*- coding: utf-8 -*-


# 최적의 군집(클러스터)의 개수를 검색하는 방법
# - 엘로우 방법을 활용하여 처리할 수 있음
from sklearn.cluster import KMeans

values=[]
for i in range(1,11) :
    km= KMeans(n_clusters=i,
               init='k-means++',
               n_init=10,
               max_iter=300,
               random_state=0)
    km.fit(X)
    # 클러스터 내의 각 클래스의 SSE 값을 반환하는 ineria_ 속성값
    values.append(km.inertia_)

print(values)

plt.plot(range(1,11),values,marker='o')
plt.xlabel('numbers of cluster')
plt.ylabel('ineria_')
plt.show()
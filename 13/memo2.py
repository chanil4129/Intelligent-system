# -*- coding: utf-8 -*-

# 비지도 학습 / 스태킹 학습

# 비지도 학습
# 지도 학습 / 비지도 학습 / (준지도 학습) / (강화학습)
# 지도학습과 다르게 종속변수(정답데이터)가 제공되지 않는 데이터에 대한 학습을 처리하는 기법
# 비지도 학습의 결과는 주관적인 판단으로 처리



# 비지도 학습의 카테고리
# - 차원 축소
#   => 시각화에 효과적(시각화에 주로 사용됨) 
#   => 데이터에 포함된 특성 중 유의미한 값을 추출
#   => 데이터에 포함된 특성을 투영하여 대표하는 값을 반환
#   => 소셜 네트워크 분석, 이미지 분석, RGB 컬러

# - 군집 분석
#   => 데이터(샘플)의 유사성을 비교하여 동일한 특성으로 구성된 데이터(샘플)들을 하나의 군집으로 처리하는 기법



# 비지도 학습 시 유의사항
# 비지도 학습의 결과는 100% 신뢰할 수 없음
# 매번 실행될 때마다 결과는 변경될 수 있음




# 군집 분석을 활용하여 데이터의 클러스터링 처리과정을 확인
# - 지도학습에서 군집 분석의 결과를 활용하는 방법

from sklearn.datasets import make_blobs
X, y= make_blobs(n_samples=150,  # 150개의 데이터 생성
                 n_features=2,# 두개의 특성
                 centers=3, # 3개의 군집
                # cluster_std=0.5, # 보기편하게 하기위해
                 shuffle=True, # 셔플
                 random_state=0) 

print(X[:10])
print(y[:10])

import matplotlib.pyplot as plt
plt.scatter(X[:,0],X[:,1], 
            c='white', 
            marker='o', 
            edgecolor='black',
            s=50) #marker o로 표시
plt.grid()
plt.show()


# 이제는 y 데이터 없이 군집 생성해보기!
# 최근접 이웃 알고리즘???
# 군집분석을 위한 클래스
# KMeans
# 가장 많이 사용되는 군집분석 클래스
# 알고리즘이 단순하고 변경에 용이
# (수정사항의 반영이 손쉬움)
from sklearn.cluster import KMeans
km = KMeans(n_clusters=5, # 군집하고자 하는 개수
            init='k-means++',
            n_init=10,
            max_iter=300,# 하루종일 돌릴 수는 없으니 300번만 돌리기
            random_state=0)
# 군집 분석 알고리즘인 KMeans의 fit 메소드의 동작
# - n_clusters에 정의된 개수만큼 포인트를 지정하여 최적의 위치를 찾도록 검ㅁ색하는 과정을 수행 
km.fit(X) 

# 군집의 결과를 생성하여 반환
y_cluster=km.predict(X)
print(y_cluster)

plt.scatter(X[y_cluster==1,0],
            X[y_cluster==1,1],
            s=50, c='lightgreen',
            marker='s',label='Cluster 1')

plt.scatter(X[y_cluster==2,0],
            X[y_cluster==2,1],
            s=50, c='orange',
            marker='o',label='Cluster 2')

plt.scatter(X[y_cluster==3,0],
            X[y_cluster==3,1],
            s=50, c='lightblue',
            marker='v',label='Cluster 3')

plt.scatter(X[y_cluster==4,0],
            X[y_cluster==4,1],
            s=50, c='lightblue',
            marker='v',label='Cluster 4')

plt.scatter(X[y_cluster==5,0],
            X[y_cluster==5,1],
            s=50, c='lightblue',
            marker='v',label='Cluster 5')

plt.scatter(km.cluster_centers_[:,0],
            km.cluster_centers_[:,1],
            s=100, c='red',
            marker='*',label='Center')

plt.legend()
plt.grid()
plt.show()








































































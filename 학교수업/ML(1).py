import numpy as np
import matplotlib.pyplot as plt

# 평균과 공분산 설정
mean = [10, 5] # 각각 첫번째와 두번째 평균
covariance = [[16, 10], [10, 16]] # 분산과 공분산
N = 1000 # 생성할 샘플의 개수

# 2변량 가우시안 분포에서 무작위 샘플 생성(1000개)
data = np.random.multivariate_normal(mean, covariance, N)

# 데이터 시각화
plt.figure(figsize=(8, 16)) # 그림 생성
plt.scatter(data[:, 0], data[:, 1], alpha=0.5) # 산점도
plt.title('2D Gaussian Distribution with mean and covariance')
plt.xlabel('X1')
plt.ylabel('X2')
plt.grid(True) # 격자 허용

plt.axis('equal') # 격자가 정사각형으로 나오도록 조정
plt.show() # 화면 표시


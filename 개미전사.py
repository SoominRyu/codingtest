# 개미전사
n = int(input())
k = list(map(int,input().split()))

d  = [0] * 100

d[0] = k[0]
d[1] = max(k[0],k[1])

for i in range(2,n):
  #현위치에서 i-1이 클지 i-2+현위치 값이 클지 계산
  d[i] = max(d[i -1], d[i-2]+k[i])

print(d[n-1])
n = int(input())

# 1~30000
d = [0] * 30001


for i in range(2,n+1):
  # 현재 - 1
  d[i] = d[i-1] + 1

#가장 작은 값으로 현재 값 갱신
  if i % 2 == 0:
    #연산 횟수를 구하는 것 
    d[i] = min(d[i], d[i//2]+1)
  
  if i % 3 == 0:
    d[i] = min(d[i], d[i//3]+1)

  if i % 5 == 0:
    d[i] = min(d[i], d[i//5]+1)

print(d[n])
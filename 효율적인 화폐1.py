n, m = map(int,input().split())

a = []
for i in range(n):
 a.append(int(input()))

# 0원 m+1원
d = [10001] * (m+1)

d[0] = 0
#i = 화폐단위
for i in range(n):
  #j = 금액
  for j in range(a[i], m+1):
    coin = j - a[i]
    if(coin) != 10001:
      d[j] = min(d[j], coin+1)


if d[m] == 10001:
  print(-1)

else:
  print(d[m])

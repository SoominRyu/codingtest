# + 먼저 계산하고 - 계산했을 때가 최소
n = list(input().split('-'))

plus = []

for i in n:
  p = i.split('+')
  hap = 0
  for j in p:
    hap += int(j)
  # + 값들 계산한 리스트  
  plus.append(hap)

ans = plus[0] 

for h in range(1,len(plus)):
  ans -= plus[h]

print(ans)

n = int(input())
snow = list(map(int,input().split()))

snow.sort()

m = 10**9

for i in range(n-1):
  a = snow[i]
  b = snow[i+1]
  for j in range(n-1,0,-1):
    if i >= j or i+1 >= j-1:
      break
    c = snow[j]
    d = snow[j-1]
    if abs((a+c) - (b+d)) < m:
      # print(a,b,c,d)
      m = abs((a+c) - (b+d))

print(m)
    
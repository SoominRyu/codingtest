n,k = map(int,input().split())
a = list(map(int,input().split()))
s = [0]
start = 0
him = 0

for _ in range(0,n):
  for j in range(start+1,n):
    him = (j-start) * (1 + abs(a[start]-a[j]))
    # print("h:",him,"i:",start,"j:",j)
    if k - him >=0:
      s.append(j)
      start = j
      break
    elif j == n-1:
      print('No')
      exit(0)
# print(start)
if start == n-1:
  print('YES')
else:
  print('NO')



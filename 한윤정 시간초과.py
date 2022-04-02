from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
f = []
# num = [i for i in range(1,n+1)]

for _ in range(m):
  s, s1 = map(int,input().split())
  f.append((s,s1))
  
# c = list(combinations(num,3))

ans = 0
# for i in c:
#     for j in range(m):
#       set1 = set(i+f[j])
#       if len(set1) == 3:
#         break
#       elif j == m-1:
#         ans +=1
# print(ans)

for i in combinations(range(n),3):
  for j in range(m):
    set1 = set(i+f[j])
    if len(set1) == 3:
      break
    elif j == m-1:
      ans +=1
print(ans)
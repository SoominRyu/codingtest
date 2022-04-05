from itertools import combinations

n,m = map(int,input().split())
card = list(map(int,input().split()))

c = list(combinations(card,3))
cc = []
for i in c:
  cc.append(sum(i))
cc.sort()
for i in cc:
  # print(i)
  if i <= m:
    ans = i
  else:
    break

print(ans)

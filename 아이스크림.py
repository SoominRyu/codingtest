from itertools import combinations

n, m = map(int, input().split())

ice = list(combinations(range(1,n+1),3))

check = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
  s, s1 = map(int,input().split())
  check[s][s1] = 1
  check[s1][s] = 1

ans = 0
# print(check)
# [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]]

for i in ice:
  if check[i[0]][i[1]] or check[i[0]][i[2]] or check[i[1]][i[2]]:
    continue
  ans +=1
print(ans)
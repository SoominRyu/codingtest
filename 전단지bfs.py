from collections import deque

n = int(input())

z = [list(map(int, list(input()))) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

ans = []


def bfs(x,y):
  count = 1
  queue = deque()

  queue.append((x,y))
  z[x][y] = 0

  while queue:
    a, b = queue.popleft()

    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]

      if 0 <= nx < n and 0 <= ny < n:
        if z[nx][ny] == 1:
          z[nx][ny] = 0
          queue.append((nx,ny))
          count += 1
  ans.append(count)

for i in range(n):
  for j in range(n):
    if z[i][j] == 1:
      bfs(i,j)


ans.sort()
print(len(ans))
for i in ans:
  print(i)
    
  




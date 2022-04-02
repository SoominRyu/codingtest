from collections import deque

def bfs(a,b):
  q = deque()
  visited = [[0] * m for _ in range(n)]

  q.append((0,0))
  visited[0][0] = 1

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if c[nx][ny] == 0 and visited[nx][ny] == 0:
          visited[nx][ny] = 1
          q.append((nx,ny))

        if c[nx][ny] >= 1:
          c[nx][ny] += 1

 
n, m = map(int, input().split())

c = []
for _ in range(n):
    c.append(list(map(int, input().split())))
print(c)


for i in range(n):
  for j in range(m):
    if c[i][j] == 1:
      bfs(i,j)

dx = [0,0,-1,1]
dy = [-1,1,0,0]



# cheese = 0
# while cheese != 0:
#   bfs(c)
# q = deque([0,0])


 

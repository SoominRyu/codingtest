from collections import deque
r, c, n = map(int,input().split())
rc = []

for _ in range(r):
  rc.append(list(input()))

# print(rc)


time = 1
bomb = [[-1] * c for _ in range(r)]

def first():
  for i in range(r):
    for j in range(c):
      if rc[i][j] == 'O':
        # bfs(time,i,j)
        q.append((i,j))
    
def second():
  for a in range(r):
    for b in range(c):
      if rc[a][b] == '.':
        rc[a][b] = 'O'
        # bomb[a][b] = t

def third():
  dx = [0,0,1,-1]
  dy = [1,-1,0,0]
  while q:
    x, y = q.popleft()
    rc[x][y] = '.'
    # print(x,y)

    for a in range(4):
      nx = x + dx[a]
      ny = y + dy[a] 
      if 0<= nx < r and 0 <= ny < c:
        if rc[nx][ny] == 'O':
          # print('hi')
          rc[nx][ny] = '.'

n -= 1

while n:
  q = deque()

  first()

  second()

  # third()

  n -= 1

  if n == 0:
    break
  
  third()
  n -= 1
  
# print(rc)
for p in rc:
  print(''.join(p))
# for i in range(r):
#   for j in range(c):
#     if rc[i][j] == 'O':
#       bomb[i][j] = time
# # print(bomb)

# def bfs(t,i,j):
#   q = deque()
#   q.append((i,j))

#   # t += 1
#   print("time:",t)
  
#   if t % 2 == 0:
#     for a in range(r):
#       for b in range(c):
#         if rc[a][b] == '.':
#           rc[a][b] = 'O'
#           bomb[a][b] = t
#     t += 1
#   print(bomb)
#   # print(rc)
#   while q:
#     x, y = q.popleft()
#     print(x,y)
#     if t % n == 0:
#       for a in range(4):
#         nx = x + dx[a]
#         ny = y + dy[a] 
#         if 0<= nx < r and 0 <= ny < c:
#           if rc[nx][ny] == 'O':
#             print('hi')
#             rc[nx][ny] = '.'
#             rc[x][y] = '.'
#             bomb[nx][ny] = t
#             bomb[x][y] = t
#             q.append((nx,ny))
#       t += 1

#         # for rr in range(r):
#         #   for cc in range(c):
#         #     if rc[rr][cc] == 'O':
#         #       rc[rr][cc] = '.'
#         #       rc[nx][ny] = '.'
#         #       bomb[rr][cc] = t
              
#     print(rc)
#     # print(x,y)

  
  


# while time != n+1:
#   for i in range(r):
#     for j in range(c):
#       if rc[i][j] == 'O':
#         bfs(time,i,j)
#   time += 1

#1초 , 2초, 3초일 때 나눠서 구현해야함 -> 다시 해보기
from collections import deque

r, c = map(int,input().split())
maze = []

for _ in range(r):
  maze.append(list(input()))

# print(maze)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[0] * c for _ in range(r)]

for i in range(r):
  for j in range(c):    
    if maze[i][j] == 'J':
      q = deque([('J', i, j)])
      visited[i][j] = 1

for i in range(r):
  for j in range(c):    
    if maze[i][j] == 'F':
      q.append(('F', i, j))
      
while q:
  key, a, b = q.popleft()
  # print(key,a,b)

  for d in range(4):
    nx = a + dx[d]
    ny = b + dy[d]
    if key == 'J':
      if 0 <= nx < r and 0 <= ny < c:
        if maze[nx][ny] == '.' and visited[nx][ny] == 0:
          visited[nx][ny] = visited[a][b] + 1
          # if maze[a][b] != 'F':
          #   maze[a][b] = '.' 
          maze[nx][ny] = 'J'
          q.append(('J',nx,ny))
          # print(maze)

      # 여기가 잘못되었을 것 같다 -> 가장자리를 판단하는 조건을 모르겠음
      # elif a == 0 or b == 0 or a == r-1 or b == c -1:
      elif nx < 0 or nx == r or ny < 0 or ny == c:
        # print(visited)
        print(visited[a][b])
        exit(0)
      else:
        print(1)
        exit(0)
        
    if key == 'F':
      if 0 <= nx < r and 0 <= ny < c:
        if maze[nx][ny] != '#':
          # print(maze)
          # print(visited)
          if maze[nx][ny] == 'J':
            count = 0
            
            for rr in range(r):
              for cc in range(c):
                if maze[rr][cc] == 'J':
                  count += 1
            if count == 1: 
              print('IMPOSSIBLE')
              exit(0)
            # print(q)
            # print(nx,ny)
            if ('J',nx,ny) in q:
              q.remove(('J', nx, ny))
              q.append(('F',nx,ny))
          maze[nx][ny] = 'F'
          # kk, aa, bb = q.pop()
          # print(kk,aa,bb)
          
          # visited[nx][ny] = 0
          # print(maze)
          
        
      
print('IMPOSSIBLE')

# 틀리고 있는 반례
# 4 6
# ######
# ......
# #.J###
# #F####
# 답 5 / 내 답 4

# 5 5
# ....F
# ...J#
# ....#
# ....#
# ...#.
# 답 4 / 내 답 2
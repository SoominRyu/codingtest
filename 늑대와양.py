from collections import deque
r, c = map(int,input().split())
m = []

for _ in range(r):
  m.append(list(input()))

dx = [0,0,1,-1]
dy = [-1,1,0,0]
q = deque()
# check = False

# for i in range(r):
#   for j in range(c):

#     #늑대
#     if m[i][j] == 'W':
#       dx = [0,0,1,-1]
#       dy = [-1,1,0,0]

#       for r in range(4):
#         nx = i + dx[r]
#         ny = j + dy[r]

#         if 0 <= nx < r and 0 <= ny < c and m[nx][ny] == 'S':
#           check = True
#           break

#     elif m[i][j] == 'S': #양
#       continue
#     elif m[i][j] == '.': #울타리 조건 없으므로 다 가두기
#       m[i][j] = 'D'

# if check:
#   print(0)
#   # print(m)
# else:
#   # print(0)
#   print(1)
#   for i in m:
#     print(''.join(i))
          



for i in range(r):
  for j in range(c):
    if m[i][j] == 'S':
      q.append((i,j))

check = False

while q:
  a, b = q.popleft()
  

  for i in range(4):
    nx = a + dx[i]
    ny = b + dy[i]
    # q.append((nx,ny))

    if 0 <= nx < r and 0 <= ny < c:
      if m[nx][ny] == 'W':
        print(0)
        exit(0)
      elif m[nx][ny] == '.':
        m[nx][ny] = 'D'
        check = True

      # if m[nx][ny] == '.':
      #   m[nx][ny] = 'D'
      #   check = True
      # elif m[nx][ny] == 'W':
      #   wolf = True

if check:
  # print(0)
  print(1)
  for k in range(r):
    print(''.join(m[k]))
else:
  print(0)
  # print(1)
  # for k in m:
  #   print(''.join(k))
# print(m) 
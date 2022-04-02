# non pass
import sys
import copy
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
ice = []
for _ in range(n):
  ice.append(list(map(int,input().split())))
repeat = 1

while True:
  visited = copy.deepcopy(ice)
  
  # 북 남 서 동
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  dung = 0

  def bfs(i,j,visited,dung):
    
    count = 0 # 바닷물(0) 있는 곳 체크
    for r in range(4): # 4면 체크
      nx = i + dx[r] 
      ny = j + dy[r]
  
      if nx >= 0 and ny >= 0:
        if ice[nx][ny] == 0: #바닷물이라면
          count += 1

    if ice[i][j] - count >= 0: #빙산이 녹을 수 있으면
      visited[i][j] -= count
    else: #최대로 녹았을 경우
      visited[i][j] = 0

    # 덩어리 구분되는 경우
    # 이거 틀림
    if count <= 1: 
      dung += 1
      return dung

  
  dd = []
  for i in range(n):
    for j in range(m):
      # 빙산이 있는 곳이라면
      if ice[i][j] != 0:
        d = bfs(i,j,visited,dung)
        if d != None:
          dd.append(d)
  
  #덩어리 체크
  ddd = 0
  for i in range(n):
    for j in range(m):
      if visited[i][j] != 0:
        ddd +=1
        
  if len(dd) == ddd:
    break
  else: 
    ice = copy.deepcopy(visited)
    repeat += 1

c = visited.count([0 for _ in range(m)])
if c == n: #전체가 다 0이라면
  print(0)
else:
  print(repeat)
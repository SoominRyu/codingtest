# 처음 (1,1)로 이동해 시작
# 인접 노드 중 값 1 경우만 이동 가능
# 초기 원소 1인 경우에만 bfs 진행
# 최단 경로에 있는 노드의 수 출력 : 노드 간 거리 1씩 증가 시켜 찾기
# BFS 계속 수행 : 최단 경로의 값들이 1씩 증가하는 형태
from collections import deque
# 1) n과 m 입력 받음
n, m = map(int, input().split())

# 2차원 리스트 정보 입력 받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 이동할 네 가지 방향 벡터 정의(상 하 좌 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS
def bfs(x, y):

  # queue 구현
  que = deque()
  # x y  튜플 데이터 담음
  que.append((x, y))

  # 큐가 빌 때까지 반복
  while que:
    # 원소 하나 꺼내서 현재 위치에서 4가지 위치 확인
    x, y = que.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 공간 벗어난 경우 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 벽도 무시
      if graph[nx][ny] == 0:
        continue
      
      #해당 노드 처음 방문 경우만 최단 거리에 기록됨
      if graph[nx][ny] == 1:
        #직전 노드 위치값에 1을 더해서 넣어줌, 1만큼 거리가 더 먼 곳임
        graph[nx][ny] = graph[x][y] + 1
        que.append((nx, ny))

    #가장 오른쪽 아래까지 최단 거리
  return graph[n - 1][m - 1]


# BFS 수행 결과
print(bfs(0,0))

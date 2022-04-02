from collections import deque

#dfs 메서드 정의
# start : 시작 노드를 큐에 넣어줌
def bfs(graph, start, visited):
  queue = deque([start])

  #현재 노드를 방문 처리
  visited[start]= True
  
  #큐가 빌 때까지 반복
  while queue:
    #큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')

    #아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True



 # 각 노드가 연결된 정보 표현 (2차원 리스트)
  # 노드 인덱스 1로 시작하는 경우 많기 때문에 인덱스 0 비워놓기
  graph = [
    [],
    [2,3,6],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
  ]

  visited = [False] * 9

  bfs(graph, 1, visited)
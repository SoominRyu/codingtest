#dfs로 특정 노드를 방문, 연결된 모든 노드들 방문

def dfs(x, y):
  #주어진 범위 벗어나는 경우 즉시 종료
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False

  #현재 노드를 아직 방문 안했을 경우
  if graph[x][y] == 0:
    #해당 노드 방문 처리
    graph[x][y] = 1

    #상 하 좌 우 위치들 모두 재귀 호출 - 왜? 연결된 모든 위치 방문 처리 진행 위해서 
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

  
# N, M을 공백을 기준으로 구분하여 받음
n, m = map(int, input().split())

# 2차원 리스트 맵 정보 입력 받음
graph = []
for i in range(n):
  graph.append(list(map(int,input())))


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    #현재 위치에서 DFS 수행
    #해당 노드와 연결된 모든 노드 방문처리됨 
    #시작점 노드 방문처리 
    if dfs(i,j) == True:
      #처음 방문일 때만 result값 증가
      result += 1

print(result)
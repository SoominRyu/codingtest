def dfs(v):
  visited[v] = 1
  s = select[v]
  print(s)
  if visited[s] == 0:
    # print("hi")
    dfs(v)
  else:
    


  
t = int(input())

for _ in range(t):
  n = int(input())
  
  # student = [i for i in range(1,n+1)]
  select = list(map(int,input().split()))

  # team = [[] for _ in range(n+1)]
  visited = [0 for _ in range(n+1)]

  for i in range(1,n+1):
    if visited[i] == 0:
      dfs(i)
  print(visited)
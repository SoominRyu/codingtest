def dfs(v):
  # visited[v] = v
  for i in team[v]:
    
    visited[i] = select[i]
    dfs(i)
  
t = int(input())

for _ in range(t):
  n = int(input())
  
  student = [i for i in range(1,n+1)]
  select = list(map(int,input().split()))

  team = [[] for _ in range(n+1)]
  visited = [0 for _ in range(n+1)]

  for i in range(n):
    a = student[i]
    b = select[i]
    print(a,b)
    team[a].append(b)
    team[b].append(a)
    team[a].append(a)

  # for i in range(1,n+1):
  #   team[i].sort()

  dfs(1)
  print(visited)


      
  


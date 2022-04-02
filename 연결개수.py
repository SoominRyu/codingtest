# from collections import deque
import sys
sys.setrecursionlimit(10000)

def dfs(v):
  visited[v] = 1
  for i in link[v]:
    if visited[i] == 0:
      dfs(i)

n, m = map(int,input().split())

link = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for i in range(m):
  a, b = map(int,input().split())
  link[a].append(b)
  link[b].append(a)

# print(link)

for j in range(1, n+1):
  if visited[j] == 0:
    dfs(j)
    count += 1
    # print(count)

# def bfs(v):
#   q = deque()
#   # q.append(v)

#   # visited[v] = 1
#   while q:

#     x = q.popleft()
#     print(x)
  
#     if i in link[x]:
#       print(i)
#       if visited[v] == 0:
#         visited[v] = 1
#         q.append(i)
        
# print(visited)  
print(count)


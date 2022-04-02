from collections import deque

def bfs(v):
  q = deque()
  q.append(v)

  visited[v] = 1

  while q:
    a = q.popleft()

    for i in [-rock[a], rock[a]]:
      jump = a + i

      if 0 <= jump < n and visited[jump] == 0:
        q.append(jump)
        visited[jump] = 1
    


n = int(input())

rock = list(map(int,input().split()))
print(rock)
s = int(input())

visited = [0] * n
bfs(s-1)

print(visited.count(1))
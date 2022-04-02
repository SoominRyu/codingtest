from collections import deque

n = int(input())
m = int(input())

f = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())

  f[b].append(a)
  f[a].append(b)

# print(f)
visited = [0 for _ in range(n+1)]

for i in f[1]:
  visited[i] = 1
  for j in f[i]:
    visited[j] = 1
visited[1] = 0
print(visited.count(1))

# q = deque()
# q.append(1)
# count = 0
# while q:
#   r = q.popleft()

#   for i in f[r]:
#     # print(i
#     if visited[i] == 0:
#       count += 1
#       q.append(i)
#       visited[i] = 1

# print(count-1)
# print(visited)
# c = []
# for i in visited:
#   if i != 1 and i != 0:
#     c.append(i)
# # c = set(c)
# print(len(set(c)))
n = int(input())
m = []

for _ in range(n):
  m.append(int(input()))
mm = m.copy()

for i in range(n-1,0,-1):
  if m[i] <= m[i-1]:
    m[i-1] = m[i] - 1

count = 0
for j in range(n):
  count += mm[j] - m[j]

print(count)
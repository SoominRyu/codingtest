n = int(input())
k = []
for i in range(n):
  k.append(int(input()))

k.sort(reverse=True)

nk = []

for i in range(n):
  nk.append(k[i]*(i+1))

print(max(nk))

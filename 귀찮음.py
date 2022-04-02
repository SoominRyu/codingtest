n = int(input())
a = list(map(int,input().split()))

have = sum(a)
a.sort(reverse=True)
cost = 0
for i in a:
  have -= i
  cost += i * have

print(cost)
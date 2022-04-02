n, m = map(int, input().split())

a = list(map(int,input().split()))
count = 0
#i : 1 3 2 3 2
for i in a:
  #j : 0 1 2 3 4 5
  for j in range(len(a)):
    if i != a[j]:
      count +=1

print(count//2)

  
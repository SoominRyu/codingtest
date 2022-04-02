n = map(int,input())
a = list(map(int,input().split()))

result1 = 0
result2 = 0
result3 = 0
result = []
a.sort()

for i in a:
  result1 += abs(a[len(a)//2 -1] - i)
  result2 += abs(a[len(a)//2 -2] - i)
  result3 += abs(a[len(a)//2] - i)

result.append(result1)
result.append(result2)
result.append(result3)

min1 = result.index(min(result))

if min1 == 0:
  print(a[len(a)//2 -1])
elif min1 == 1:
  print(a[len(a)//2 -2])
else:
  print(a[len(a)//2])

#답
n = map(int,input())
a = list(map(int,input().split()))
a.sort()

print(a[(n-1)//2])
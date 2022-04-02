n = int(input())

a = []

for i in range(n):
  student = input().split()
  5.append((student[0], int(student[1])))


print(a[1])
a = sorted(a, key=lambda grade:grade[1])

for grade in a:
  print(grade[0],end=' ')
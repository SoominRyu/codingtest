n = int(input())

hap = 0

for i in range(1,n+1):
  s = sum((map(int,str(i))))
  # 각 자리 수 str(i)
  ss = i + s

  if ss == n:
    print(i)
    break
  if i == n:
    print(0)
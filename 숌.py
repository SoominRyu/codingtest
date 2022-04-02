n, m = map(int,input().split())
if n == 0:
  print(0)
  exit(0)
w = list(map(int,input().split()))
count = 1
box = m
for i in w:
  if i <= box:
    box -= i
  else:
    box = m-i
    count += 1  
    
print(count)
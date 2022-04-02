n = list(map(int,input()))

left = 0
right = 0

for i in range(len(n)//2):
  left += n[i]

for j in range(len(n)//2,len(n)):
  right += n[j]

if(left == right):
  print("LUCKY")
else:
  print("READY")

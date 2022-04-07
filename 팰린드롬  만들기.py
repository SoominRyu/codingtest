n = list(input())

a = n[:len(n)//2]
b = n[::-1]
b = b[:len(n)//2]  

if a == b:
  print(1)
else:
  print(0)  
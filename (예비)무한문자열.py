s = list(input())
t = list(input())

# st = s * (len(t) // len(s))

if s * len(t) == t * len(s):
  print(1)
else:
  print(0)
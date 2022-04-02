import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
  s = list(input().strip())

  #문자열 길이 짝수
  if len(s) % 2 == 0:
    a = s[:len(s)//2]
    b = s[-1:len(s)//2-1:-1]

    if a == b:
      print(0)
    else:
      print(1)

  cc = []
  #문자열 길이 홀수
  for i in range(len(s)):
    c = s.count(s[i])
    if c % 2 == 1:
      cc.append(i)

  ## 2개 이상 겹칠 때
  ## 1개만 겹칠 때 
  
    
    


  # print(a,b)
  # if a == b:
  #   print(0)
  # else:
  #   if a == b[:-2]:
  #     print(0)
  #   else:
  #     a = set(a)
  #     b = set(b)
  #     if a & b == a:
  #       print(1)
  #     else:
  #       print(2)
  # a = set(a)
  # b = set(b)
  # print(a,b)
  # if a & b == a:
  #   if len(a) == len(b):
  #     print(0)
  #   elif a == b[:-2]:
  #     print(0)
  #   else:
  #     print(1)

# for _ in range(n):
#   s = list(input().strip())

#   tag = True
#   d = 1
#   p = len(s) - 1


  

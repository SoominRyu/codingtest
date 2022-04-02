from collections import deque
from collections import Counter

s = list(input())

s.sort()

a = deque()
b = deque()

for i in range(len(s)):
  if i % 2 == 1:
    a.append(s[i])
  else:
    b.appendleft(s[i])

if len(a) != len(b):
  c = list((Counter(b)-Counter(a)).keys())
  b.remove(c[0])
  ab = list(a) + list(c) + list(b)
else:
  ab = list(a)+list(b)
  
if len(ab) == 1:
  print(''.join(ab))
else:
  # print(ab)
  x = ab[:len(ab)//2]
  y = ab[::-1]
  y = y[:len(ab)//2]

  if x == y:
    print(''.join(ab))
  else:
    print("I'm Sorry Hansoo")


# c = ''
# for i in s:
#   if i != c:
#     c = i
#     a.append(i)
#   else:
#     b.appendleft(i)

  
# a = list(a)
# b = list(b)
# # print(a,b)
# if len(a) != len(b):
#   ab = list((Counter(b)-Counter(a)).keys())
#   print(ab,a,b)
#   try:
#     b.remove(ab[0])
#   except:
#     ab = []
#   ans = ''.join(a+ab+b)
# else:
#   ans = ''.join(a+b)
  
# print(ans)
# if len(ans) == 1:
#   print(ans)
# else:
#   a1 = ans[:len(ans)//2]
#   b1 = ans[::-1]
#   b1= b1[:len(ans)//2]  
# print(a1, b1)
# if a1 == b1:
#   print(ans)
# else:
#   print("I'm Sorry Hansoo")


  
#   # print(''.join(a+ab+b))
#   # exit(0)
# print(''.join(a+b))
# # print(b)

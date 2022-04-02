s = list(input())

num = []

alpha = []

for x in range(97,123):
  if chr(x) in s:
    num.append(s.count(chr(x)))
  else:

    num.append(0)




print(*num)
# for i in range(len(s)):
#   if s[i] in s[0:i]:
#     num.append(-1)
#   else:
#     num.append()

  

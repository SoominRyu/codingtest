s = list(input())

num = [-1] * 26


# for x in range(97,123):

for i in range(len(s)):
  if num[ord(s[i])-97] == -1:
    num[ord(s[i])-97] = i

print(*num)
    
  
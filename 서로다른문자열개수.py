# from itertools import combinations

# s = list(input())

# count = 0
# for i in range(1,len(s)+1):
#   print(list(map(''.join, combinations(s,i))))
#   count += len(set(list(map(''.join, combinations(s,i)))))

# print(count)

s = input()
count = set()
for i in range(len(s)):
  for j in range(i,len(s)):
    ss = s[i:j+1]
    count.add(ss)

print(len(count))
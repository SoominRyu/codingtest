
from itertools import combinations
a = list(input())
b = sorted(a)

for i in range(len(a)):
  if i == 0:
    print(b[0])
  else:
    s = list(combinations(a,i+1))
    s.sort()
    print("".join(s[0]))

  

# a.sort()
# b = sorted(a)
# # print(b)
# for i in range(len(a)):
#   ind = []
#   for j in range(i+1):
#     a_idx = a.index(b[j])
#     if a_idx in ind:
#       # print(a_idx)
#       for s in range(a_idx+1,len(a)):
#         # print("hel")
#         if b[j] == a[s]:
#           # print("hi")
#           ind.append(s)
#     else:
#       ind.append(a.index(b[j]))
#   # print(ind)
#   ind.sort()
#   # print(ind)
#   for k in ind:
#     print(a[k], end='')
#   print("")


# for i in range(len(a)):
#   pr = i+1 #출력할 문자 수 
#   visit = []
#   for i in a:
#     visit.append(ord(i))
#   print(visit)

#   for p in range(pr):
#     # print(min(a))
#     # p += 1
#     # visit[a.index(min(a))] = 0
#     # if p != pr:
#     s = [min(a)]
#     start = a.index(min(a))
    
#     while p != pr:
#       p += 1
#       if start != len(a)-1:
#         s.append(min(a[start+1:]))
#         start = a.index(min(a[start+1:]))
#     print(s)
          

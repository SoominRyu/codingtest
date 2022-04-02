n = int(input())
name = []
count = {}
for _ in range(n):
  s, a = input().split('.')
  name.append(a)

for i in name:
  try:
    count[i] += 1
  except:
    count[i] = 1

nn = list(count.items())
nn.sort()

for j in nn:
  print(j[0],j[1])

      
#   if a not in name:
#     name.append([a,1])
#   else:
#     name[name.index(a)][1] += 1
# print(name)
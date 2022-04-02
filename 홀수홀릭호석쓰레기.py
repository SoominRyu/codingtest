from itertools import combinations
n = list(map(int,input()))

com = list(combinations(n,3))
# print(com)

def check(num):
  if num % 2 == 0:
    holic = 'even'
  else:
    holic = 'odd'

  return holic

def combi(num):
  com = list(combinations(,3))
  hap = []
  print(com)
  for i in com:
    hap.append(n[i[0]:i[1]] + n[i[1]:i[2]] + n[i[2]:])
    print(i[0])
    print(n[i[0]:i[1]] + n[i[1]:i[2]] + n[i[2]:])
  return min(hap), max(hap)

count = 0
for i in n:
  holic = check(i)
  # print(holic)
  if holic == 'odd':
    count += 1

  if len(n) >= 3:
    min3, max3 = combi(n)
    # print(min3, max3)



    
  elif len(n) == 2:
    new = n[0] + n[1]
  elif len(n) == 1:
    break

# print(count)

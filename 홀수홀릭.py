from itertools import combinations
n = list(map(int,input()))
m  = list(range(len(n)))
com = list(combinations(m,2))

def check(num):
  holic = 0
  for i in n:
    if i % 2 == 0:
      holic += 1
  return holic

# 3 이상일 때 
def combi(num):
  hap_max, hap_min = [], []
  count_max, count_min = 0, 3
  print(com)

  for i in com:  
    if (i[1] != (len(m)-1)):
      hap = []
      hap.append(sum(n[:i[0]+1]))
      hap.append(sum(n[i[0]+1:i[1]+1]))
      hap.append(sum(n[i[1]+1:]))
    print(hap)
    temp = check(hap)
    if temp >= count_max:
      count_max = temp
      hap_max = hap
    elif temp <= count_min:
      count_min = temp
      hap_min = hap

  # print(hap_max,hap_min)
  
  return hap_min, hap_max

# count = 0

def holic(n):
  # for i in n:
  #   holic = check(i)
  #   if holic == "odd":
  #     count += 1
  # count += check(n)
    
  if len(n) > 3:
    min3, max3 = combi(n)
    new_min = min3
    new_max = max3
    print(new_min,new_max)
    holic(new_min)
    holic(new_max)

  # return count

  
  # elif len(n) == 3:
  
  # elif len(n) == 2:

  # elif len(n) == 1:

holic(n)
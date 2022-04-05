n = int(input()) #기둥 개수

lh = []

for _ in range(n):
  lh.append(list(map(int, input().split())))

lh.sort()

# print(lh)
start = lh[0][1]
max1 = sorted(lh,reverse = True)
max1 = sorted(max1,reverse=True, key=lambda x:x[1])
# print(max1)
# print(lh.index(max1[0]))
maxi = lh.index(max1[0])
w = lh[0][0]
hap = 0

for i in range(maxi):
  if lh[i][1] >= lh[i+1][1]:
    lh[i+1][1] = lh[i][1]

for i in range(n-1, maxi, -1):
  if lh[i][1] >= lh[i-1][1]:
    lh[i-1][1] = lh[i][1]

for i in range(maxi):
  hap += (lh[i+1][0] - lh[i][0]) * lh[i][1]

for i in range(n-1, maxi, -1):
  hap+= (lh[i][0] - lh[i-1][0]) * lh[i][1]

hap += max1[0][1]
print(hap)

# if maxi > 0:
#   for i in range(1,maxi+1):
#     if lh[i][1] > start:
#       hap += (lh[i][0] - w) * start
#       start = lh[i][1]
#       w = lh[i][0]
#   # print(hap)

#   start1 = lh[-1][1]
#   w1 = lh[-1][0]
#   for j in range(n-1,maxi, -1):
#     if lh[i][1] > start1:
#       hap += (w1 - lh[i][0]) * start1
#       start1 = lh[i][1]
#       w1 = lh[i][0]

#   hap += max1[0][1]

#   print(hap)
#   exit(0)
# else:
#   start1 = lh[-1][1]
#   w1 = lh[-1][0]
#   for j in range(n-1,maxi, -1):
#     if lh[j][1] > start1:
#       hap += (w1 - lh[j][0]) * start1
#       start1 = lh[j][1]
#       w1 = lh[j][0]

#   hap += max1[0][1]

#   print(hap)
#   exit(0)



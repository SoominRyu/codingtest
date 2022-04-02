from itertools import accumulate
from itertools import chain
import sys
input = sys.stdin.readline
n, m = map(int,input().split())

box = []

for _ in range(n):
  box.append(list(map(int,input().split())))

k = int(input())

kbox = []
for _ in range(k):
  kbox.append(list(map(int,input().split())))


for r in range(k):
  k = kbox[r]
  a, b, c, d = k[0]-1, k[1]-1, k[2], k[3]
  # print(a,b,c,d)
  # ans = 0
  kkm =[]
  for i in range(c):
    kk = box[i][b:d]
    kkm.append(kk)
    # kkm = list(accumulate(box[i][b:d]))
    # print(kkm)
    # ans += kkm[-1]
  
  ans =list(accumulate(chain(*kkm)))
  print(ans[-1])
  # print(ans[-1])
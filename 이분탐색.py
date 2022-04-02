import sys
import bisect
#bisect : 이분탐색

input = sys.stdin.readline
num = int(input())

while num:
  bi = 0

  n, m = map(int,input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))

  a.sort()
  b.sort()

  for i in a:
    bi += bisect.bisect_left(b,i) #왼쪽 인덱스 구하기

  print(bi)
  num -= 1
    

# for _ in range(int(input())):
#   n, m = map(int,input().split())
#   a = list(map(int,input().split()))
#   b = list(map(int,input().split()))
#   hap = 0
#   h = 0
#   a.sort()
#   b.sort()
#   idx = -1
#   for i in range(n):
#     # print("idx",idx)
#     for j in range(idx+1,m):
#       if a[i] > b[j]:
#         hap += 1
#         idx = j
#       else:
#         break
#     # print(h,hap)
#     hap += h
#     if hap < m:
#       h = hap
#     else:
#       h = m
    

#   # if n >= m:
#   #   for i in range(n):
#   #     for j in range(m):
#   #       if a[i] > b[j]:
#   #         hap += 1
#   # else:
#   #   for i in range(m):
#   #     for j in range(n):
#   #       if a[j] > b[i]:
#   #         hap +=1

#   print(hap)

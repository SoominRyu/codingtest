#두 배열의 원소 교체
import math

N, K = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


A.sort()
B.sort() #B.sort(reverse=True)가 더 좋다

for i in range(K):
  #A의 원소가 B의 원소보다 작은 경우
  if A[i] < B[N-1-i]:
    A[i], B[N-1-i] = B[N-1-i], A[i]
  else: #A의 원소가 B의 원소보다 크거나 같을 때 반복문 탈출
    break


print(sum(A))



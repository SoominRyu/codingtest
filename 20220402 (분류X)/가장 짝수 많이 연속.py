n,k = map(int,input().split())
s = list(map(int,input().split()))


for j in range(k+1):
  dp = [0] * len(s)
  even = 0

  #현재 s의 짝수 연속 표시
  for i in range(len(s)):
    if s[i] % 2 == 0:
      even += 1
      dp[i] = even
    else:
      even = 0

  mm = 0 #가장 많이 연속됐을 때 개수
  mi = 0 #가장 많이 연속됐을 때 인덱스 넘버
  
  #동률 시 가장 뒤에 있는 인덱스
  for d in range(len(dp)-1,-1, -1):
    if mm < dp[d]:
      mi = d
      mm = dp[d]
  if j == k:
    break

  # [1 0 0 1 2 3 4 0 0 1 2 3 0 1 2 3]  
  #  2 1 1 2 2 2 2 1 1 2 2 2 1 2 2 2
  #최대 연속 앞쪽부터 탐색
  for k in range(mi-mm ,0,-1):
    try:
      if dp[k] == 0:
        del s[k]
        break
      #앞까지 홀수 없으면 뒷쪽 탐색  
      elif k == 1:
        for t in range(mi,len(dp)):
          if dp[t] == 0:
            del s[t]
            break
    except:
      break
# print(s)
print(mm)
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0


while (start <= end):
  total = 0
  mid = (start + end) // 2
  
  for i in array:
    if i > mid:
      # 자르고 남은 양 계산
      total += i - mid
    
#자르고 남은 양이 M보다 작으면 왼쪽 탐색
  if total < m :
    end = mid -1

  #자르고 남은 양이 m보다 크면 오른쪽 탐색
  else:
    #최대한 덜 잘랐을 때 값 result에 기록
    result = mid
    start = mid + 1


print(result)

    



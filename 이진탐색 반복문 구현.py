#이진탐색 반복

def bs(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    
    #중간점 왼쪽 확인
    elif array[mid] > target:
      end = mid -1

    # 중간점 오른쪽 확인
    else:
      start = mid + 1

  
n, target = list(map(int, input.split()))

array = list(map(int, input().split()))


result = bs(array, target, 0, n-1)

if result == None:
  print("원소 존재하지 않음")
else:
  print(result+1)
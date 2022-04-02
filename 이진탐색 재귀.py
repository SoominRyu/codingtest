#이진 탐색 코드: 재귀

def bs(array, target, start, end):
  # 데이터 존재하지 않음
  if start > end:
    return None
  
  mid = (start + end) // 2

# 찾은 경우 중간점 인덱스 반환
  if array[mid] == target:
    return mid

#중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif array[mid] > target:
    return bs(array, target, start, mid-1)
#중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else:
    return bs(array, target, mid+1, end)
  
#n:원소의 개수 target:찾고자 하는 값 입력 받기
n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

#이진 탐색 수행 결과 출력
result = bs(array, target, 0, n-1)

if result == None:
  print("원소 존재하지 않음")
else:
  print(result + 1)
#퀵 정렬

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(array, start, end):
  #원소 1개인 경우 종료
  if start >= end:
    return
  pivot = start #피벗 = 첫번째 원소
  left = start +1
  right = end
  

  while(left <= right):
    #피벗보다 작은 데이터를 찾을 때까지 반복
    while(left <= end and array[left] <= array[pivot]):
      left += 1
    while(right > start and array[right]>= array[pivot]):
      right -= 1
    
    #엇갈린 경우 작은 데이터 <-> 피벗
    if (left > right) :
      array[right], array[pivot] = array[pivot], array[right]

    #엇갈리지 안흠 작은 데이터 <-> 큰 데이터
    else:
      array[left], array[right] = array[right], array[left]
  
  #분할 이후 왼쪽/오른쪽 각각 정렬
  quick(array, start, right-1)
  quick(array, right+1, end)

quick(array, 0, len(array)-1)
print(array)


#  퀵 정렬 (파이썬 장점)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(array):
  pivot = array[0]
  tail = array[1:]

  left = [x for x in tail if x <= pivot]
  right = [x for x in tail if x > pivot]

  return quick(left) + pivot + quick(right)

print(quick(array))
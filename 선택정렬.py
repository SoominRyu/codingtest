#선택정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

#데이터의 개수 -1까지 반복
#가장 앞쪽 원소 위치
for i in range(len(array)):
  min_index = i #가장 작은 원소 인덱스
  #i+1 ~ 전체 원소 
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  # 값 교환, 위치 바꿔줌
  # 스와프  
  array[i], array[min_index] = array[min_index], array[i]

print(array)
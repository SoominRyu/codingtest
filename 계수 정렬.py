#계수 정렬

#모든 원소 값이 0보다 크다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

#모든 범위를 포함하는 리스트 선언
#10만큼 크기 가진 배열 만들기
count = [0] * (max(array)+1)
#count = [0] * len(array)
#print(max(array)) = 9
#print(len(array)) = 15

for i in range(len(array)):
  #각 데이터에 해당하는 인덱스의 값 증가(개수 count)
  count[array[i]] += 1

#리스트에 기록된 정렬 정보 확인
for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')

#삽입 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

#두 번째 원소부터 왼쪽으로 이동하며 자리 바꿔줌
for i in range(1, len(array)):
  #인텍스 i부터 1까지 1씩 감소시켜 반복
  # j : 삽입하고자 하는 원소의 위치 
  for j in range(i, 0, -1):
    if array[j] < array[j-1]:
      #한 칸씩 왼쪽으로 이동
      #스와프
      array[j], array[j-1] = array[j-1], array[j]
    else:
      #자기보다 작은 데이터를 만나면 그 위치에 멈춤
      break

print(array)
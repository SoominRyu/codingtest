#num = 8, 8
arr = [[0 for r in range(8)] for c in range(8)]
col = ['a','b','c','d','e','f','g','h']
move = input()
count = 0


steps = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

for i in range(8):
  for j in range(8):
    arr[i][j] = col[j] + str(i+1)
    if(move == arr[i][j]):
      for s in steps:
        move_i = i+s[0]
        move_j = j+s[1]
        if move_i >=0 and move_j >=0 and move_i<=7 and move_j<=7:
          count+=1

print(count)

#답안
#현재 나이트 위치 입력 받기
input_data = input()

# 행 번호 = 행+1
row = int(input_data[1])

#문자 들어온 값을 아스키 코드 형태로 
#ord 유니코드로 돌려줌 --> 실제 열 번호값을 찾음
col = int(ord(input_data[0]))-int(ord('a'))+1

# 나이트가 이동할 수 있는 8가지 방향 정의(튜플)
steps = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
  #이동하고자 하는 위치
  next_row = row + step[0]
  next_col = col + step[1]
#해당 위치로 이동 가능하면 카운트 증가
  if next_row >= 1 and next_row <=8 and next_col >=1 and next_col <=8:
    result +=1

print(result)


#수정

col = ['a','b','c','d','e','f','g','h']
move = input()
count = 0


steps = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

for i in range(8):
  for j in range(8):
    arr = col[j] + str(i+1)
    if(move == arr):
      for s in steps:
        move_i = i+s[0]
        move_j = j+s[1]
        if move_i >=0 and move_j >=0 and move_i<=7 and move_j<=7:
          count+=1

print(count)
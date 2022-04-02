#오목

arr = []
#입력받기
for i in range(19):    
	arr.append(list(map(int, input().split())))

print(arr)

while True:
  ## 가로
  #가로 연속 5개
  # print(arr[2].count(2))

  # 5개 이상 있는 곳 세기
  one_r = [] #5개 이상 1이 있는 가로 줄 인덱스
  two_r = [] #5개 이상 2가 있는 가로 줄 인덱스

  for j in range(19):
    if arr[j].count(1) >=5:
      one_r.append(j)
    if arr[j].count(2) >=5:
      two_r.append(j)

  if len(one_r) > 0 :
    # 5개 이상 있는 가로줄 체크 (1)
    for ro in one_r:
      for oo in range(15):
        if arr[ro][oo] == 1:
          if arr[ro][oo+1] == 1:
            if arr[ro][oo+2] == 1:
              if arr[ro][oo+3] == 1:
                if arr[ro][oo+4] == 1:
                  if oo+5 < 20 and arr[ro][oo+5] != 1:
                    print(1,"가로")
                    print(ro+1, oo+1)
    break

  if len(two_r) > 0:
  # 5개 이상 있는 가로줄 체크 (2)
    for ro in two_r:
      for oo in range(15):
        if arr[ro][oo] == 2:
          if arr[ro][oo+1] == 2:
            if arr[ro][oo+2] == 2:
              if arr[ro][oo+3] == 2:
                if arr[ro][oo+4] == 2:
                  if oo+5 < 20 and arr[ro][oo+5] != 2:
                    print(2,"가로")
                    print(ro+1, oo+1)
    break 

      
  # print(arr[4].index(1))
  # print(one_r, two_r)


  ##세로
  #세로 연속 1
  for d in range(19):
    for c in range(15):
      if arr[c][d] == 1:
        if arr[c+1][d] == 1:
          if arr[c+2][d] == 1:
            if arr[c+3][d] == 1:
              if arr[c+4][d] == 1:
                if c+5 < 20 and arr[c+5][d] != 1:
                  print(1,"세로")
                  print(c+1, d+1)
  break

  #세로 연속 2
  for d in range(19):
    for c in range(15):
      if arr[c][d] == 2:
        if arr[c+1][d] == 2:
          if arr[c+2][d] == 2:
            if arr[c+3][d] == 2:
              if arr[c+4][d] == 2:
                if c+5 < 20 and arr[c+5][d] != 2: 
                  print(2,"세로")
                  print(c+1, d+1)
  break

  ##대각선

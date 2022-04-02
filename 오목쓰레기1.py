#오목

arr = []
#입력받기
for i in range(19):    
	arr.append(list(map(int, input().split())))

print(arr)

#오른쪽 이동
xr, yr = 0, 1

#아래로 이동
xd, yd = 1, 0

#대각선 이동
xc, yc = 1, 1

nx, ny = 0, 0
count = 1

num = 0

# while count != 2:
  
        # if arr[nx+xd][ny+yd] == num:
        #   print("d")
        # if arr[nx+xc][ny+yc] == num:
        #   print("c")
      
for i in range(19):
  if (nx < 0) or (ny < 0) or (nx >= 19) or (ny >= 19):
    break
  else:
    if arr[nx][ny] == 1 or arr[nx][ny] == 2:
      num = arr[nx][ny]
      for r in range(4):
        if arr[nx+xr][ny+yr] == num:
          nx += xr
          ny += yr
          count +=1
          print("r")
        else:
          break
  print(count)
  if count == 5:
    print("1연속")
    break





n = int(input())

count = 0

#n까지 1씩 증가
for hour in range(n+1):
  for min in range(60):
    for sec in range(60):
      # 시 분 초를 문자열 형태로 만들어 더함 -> 문자열 안에 3이 포함되었는지 확인
      if '3' in str(hour) + str(min) + str(sec):
        count += 1

print(count)
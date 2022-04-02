n, m = map(int(input().split()))

a = list(map(int, input().split()))

# 1 ~ 10까지의 무게를 담는 리스트 만들기
array = [0] * 11

# 각 무게에 해당하는 볼링공 개수가 넣어주기 
for x in a:
  array[x] += 1

result = 0
# 1 ~ m까지 각 무게에 대하여 처리 

for i in range(1, m+1):
  #무게 i인 볼링공 개수 제외 
  n -= array[i]
  #b가 선택하는 경우의 수
  result += array[i] * n 

  print(result)
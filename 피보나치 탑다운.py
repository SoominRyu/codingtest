# 피보나치 탑다운 (하향식)

#한 번 계산된 결과 메모이제이션, 리스트 초기화
d = [0] * 100

# 피보나치 재귀
def fibo(x):
  
  #종료조건 (1/2 일 때 1 반환)
  if x == 1 or x ==2:
    return 1

  #이미 계산했던 적 있음 - 그대로 반환
  if d[x] != 0:
    return d[x]
  
  #아직 계산 안함 - 피보나치 결과
  d[x] = fibo(x-1) + fibo(x-2)
  return d[x]

print(fibo(99))
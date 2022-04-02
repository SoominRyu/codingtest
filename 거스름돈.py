n = 1260
count = 0
coin = 0
i = 1
array = [500, 100, 50, 10]

for coin in array:

    count += n // coin  #해당 화폐로 거슬러 줄 수 있는 동전 개수, 몫
    print(i, ": count+=n//coin -", coin, count, n)
    n %= coin  #나머지 값
    print(i, ": n %= coin -", coin, count, n)
    i += 1
    print()

print('총 사용 동전 수:', count)

#시간복잡도 : 동전의 총 종류

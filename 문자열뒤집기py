n = list(map(int,input()))

# 0001100
# 0000000 -> 1
# 1111100 -> 11111111 -->2

#1001

#zero = [0] * len(n)
#one = [1] * len(n)

count0 = 0
count1 = 0

if n[0] == 0:
  count1 +=1
else:
  count0 +=0

for i in range(len(n)-1):
  if n[i] != n[i+1]:
    # 1로 바뀜
    if n[i+1] == 1:
      count0 +=1
    #0으로 바귐
    else:
      count1 +=1

print(min(count0,count1))
    
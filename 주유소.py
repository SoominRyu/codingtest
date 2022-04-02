n = int(input())
d = list(map(int,input().split()))
o = list(map(int,input().split()))

# temp = 0
# cost = 0

# j = 1

# for i in range(n-1):
#   if o[i] != 0:
#     if o[temp] < o[temp+j]:
#       # print("작:",cost)
#       # temp = i
#       cost += o[temp] * (d[temp] + d[temp+1])
#       o[temp+j] = 0
#       j+=1
#     else:
#       # print("큰",cost)
#       cost += o[i] * d[i]
#       o[i] = 0
#       temp += 1

cost = 0
min_c = o[0]

print(cost)
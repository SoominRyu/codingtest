n = int(input())
x = list(map(int, input().split()))

x.sort() #오름차순 정렬
print(x)

group = 0 #전체 그룹 수 
people = 0 #현재 그룹 모험가 수

for i in x:
  people += 1
  if people >= i: #people:현재 그룹 내 모험가 수 >= i:현재 공포도 
    group +=1
    people = 0 #현재 그룹 내 모험가 수 초기화

print(group)


#max_x = max(x)
#max_x_index = x.index(max(x))


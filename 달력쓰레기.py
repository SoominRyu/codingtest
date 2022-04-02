n = int(input())
day = []
for i in range(n):
  day.append(list(map(int,input().split())))

day.sort(key=lambda x:x[1], reverse=True)
day.sort(key=lambda x:x[0])

a = 0 #가로
b = 1 #세로
# d1 = day[0][0]
# d2 = day[0][1]
# # for j in range(n):
# #   d = day[j]
# #   a += d[1]-d[0]+1
# #   if 

#달력
cal = []
maxd = max(day)
mind = min(day)
cal = [0] * (maxd[1]-mind[0]+1)
for k in range(mind[0],maxd[1]+1):
  cal[k-mind[0]] = k

# print([cal]*2)
# # 
# print(cal)
# print(day)
el = []
ncal = cal.copy()
ncal1 = cal.copy()

test = [[0,0,0,0],[1,2,3,4]]
for s in range(len(test)):
  if 2 in test[s]:
    print("yes")

for j in range(n):
  for 

# for j in range(n):
  
#   if day[j][0] in cal:
#     print("j:",day[j][0])
#     ind = cal.index(day[j][0])

#     for p in range(day[j][1]-day[j][0]+ 1):
#       print("p:",p)      
#       cal[ind+p] = 0
  
#   else:
#     if day[j][0] in ncal:
#       ind = ncal.index(day[j][0])

#       for q in range(day[j][1]-day[j][0]+ 1):
#         # print("p:",p)      
#         cal[ind+q] = q
    
#     else:
#       b += 1
#       ncal = 


     

    # for p in range(day[j][1]-day[j][0]+ 1):
      

print(cal)
print(len(cal),b) 

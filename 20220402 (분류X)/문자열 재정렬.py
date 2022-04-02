#내가 푼 풀이
string = list(input())
string.sort()
num = list('1234567890')

location = 0

for s in string:
  for n in num:
    if s == n:
      location += 1

x = map(int,string[:location])
y = string[location:]
result = 0

for p in x:
  result += p


print("".join(y) + str(result))

#답
data = input()
result = []
value = 0

#문자 확인
for x in data:
  #알파벳이면 결과 리스트에 삽입
  if x.isalpha():
    result.append(x)
  #숫자는 value에 덧셈하여 담기
  #덧셈하려면 int로 변환 필요
  else:
    value += int(x)
  
  #알파벳 오름차순
  result.sort()

#value가 존재하면 뒤에 삽입
if value != 0:
  result.append(str(value))

print(''.join(result))



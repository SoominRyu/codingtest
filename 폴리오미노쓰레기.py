x = input()
xd = x.split('.')
while '' in xd:
  xd.remove('')
xs = x.split('X')
# xs = ''.join(xs).split(' ')
# print(xs)
print(xd,xs)
dot = []
for d in xs:
  if d != '':
    dot.append(d) 
print(dot)

ab =[]

# print(xd)
for i in xd:
  if 'X' not in i:
    print(x)
    exit(0)
  else:
    if len(i) % 4 == 0:
      ab.append('AAAA'*(len(i)//4))
    elif len(i) % 4 == 2:
      ab.append('AAAA'*(len(i)//4)+'BB')
    elif len(i) == 2:
      ab.append('BB')
  
    else:
      print(-1)
      exit(0)

pol = []
for a in range(len(ab)):
  pol.append(ab[a])
  # print(len(xd))
  if a != (len(ab)-1):
    pol.append(dot[a])

print(''.join(pol))

# XXCC --> X가 아닌 다른 문자열이 왔을 때 어떻게 해야할지
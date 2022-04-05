s = input()

c = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in c:
  if i in s:
    s = s.replace(i,'*')

print(len(s))
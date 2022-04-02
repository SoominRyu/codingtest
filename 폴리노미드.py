n = input()

re = n.replace('XXXX','AAAA')
re = re.replace('XX','BB')

if 'X' in re:
  print(-1)
else:
  print(re)
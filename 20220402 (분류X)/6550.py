
while True:
  try:
    s, t = input().split()
    if s in t:
      print('Yes')
    else:
      s = list(s)
      t = list(t)
    
      w = [0]
      start = 0
      count = 0
      for i in s:
        for j in range(start+1,len(t)):
          if i == t[j]:
            count += 1
            start = j
            break
          
      if count == len(s):
        print('Yes')
      else:
        print('No')
  except:
    break

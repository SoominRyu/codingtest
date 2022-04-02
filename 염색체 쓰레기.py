import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
  s = list(input())
  al = ['A','B','C','D','E','F']
  tag = True
  while tag == True:
    if s[0] not in al:
      tag = False
      break
    # ind = 1
    if s[1] != 'A':
      print("1")
      tag = False
      # break
    else:
      if s[0] != 'A':
        tag = False
        break
      else:
        tag = True
        ind = 0
        for j in range(ind,len(s)):
          if s[j] == 'A':
            ind = j
          else:
            break
    print(ind)
    if s[ind+1] != 'F':
      print("2")
      tag = False
      break
    
    else:
      ind = ind+1
      for j in range(ind,len(s)):
        if s[j] == 'F':
          ind = j
        else:
          break
    if s[ind+1] != 'C':
      print("3")
      tag = False
      break
    else:
      ind = ind+1
      for j in range(ind,len(s)):
        if s[j] == 'C':
          ind = j
        else:
          break
    if ind == len(s)-1:
      print("Infected!")
      break
    else:
      if s[-1] in al:
        # tag = 'OK'
        print("Infected!")
        break
      else:
        print("4")
        tag = False
    


  if tag == False:
    print("Good")
  elif tag == 'OK':
    print("Infected!")

t = int(input()) #문자열 게임 수
w = input() #문자열
k = int(input()) #정수
wc = [0] * len(w)
wl = []

while t != 0:
  count = 0
  for i in range(len(w)):
    wc[i] = w.count(w[i])
  
  print(wc)

  for j in range(len(w)):
    if wc[j] == k:
      wl.append(w[j])
  wl = set(wl)
  print(wl)

  for w in wl:
    while True:
      
    # for k in range(len(w)):
    #   if w[k] == w:
      
  

  t -= 1


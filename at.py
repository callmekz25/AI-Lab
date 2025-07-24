def AT(sodinh, h, adj, start, stop):
  OPEN = [start]
  CLOSE = []
  FATHER = [-1] * sodinh
  g = [float('inf')] * sodinh
  g[start] = 0
  while len(OPEN) > 0:
    n = min(OPEN, key=lambda x: g[x])
    print(f"n = {n}")
    OPEN.remove(n)
    CLOSE.append(n)

    print(f"CLOSE = {CLOSE}")
    
    if n == stop:
      print(f"Tim thay duong di tu {start} -> {stop}")
      i = stop
      while i != -1:
        print(i, end="<-")
        i = FATHER[i]
      return True
    Tn = []
    for i in range(sodinh):
      if adj[n][i] == 1 and i not in OPEN and i not in CLOSE:
        Tn.append(i)
        FATHER[i] = n
        g[i] = g[n] + h[i]
    print(f"Tn = {Tn}")
    
    OPEN += Tn

    print(f"OPEN = {OPEN}")

  print(f"Khong tim thay duong di tu {start} -> {stop}")
  return False
    
    


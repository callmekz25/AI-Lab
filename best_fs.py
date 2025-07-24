
def BestFirstSearch(sodinh, h, adj, start, stop):
  OPEN = [start]
  CLOSE = []
  FATHER = [-1] * sodinh
  while len(OPEN) > 0:
    n = OPEN.pop(0)
    print(f"n = {n}")    
    CLOSE.append(n)
    print(f"CLOSE = {CLOSE}")

    if n == stop:
      print(f"Tim thay duong di tu: {start} -> {stop}")
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
    print(f"Tn = {Tn}")

    OPEN = Tn + OPEN
    OPEN.sort(key=lambda x: h[x])
    print(f"OPEN after sort {OPEN}")

    

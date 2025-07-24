from readfile import readFileHeuristic, readFileMtk

def HillClimbing(sodinh, h, adj, start, stop):
  OPEN = [start]
  CLOSE = []
  FATHER = [-1] * sodinh
  while len(OPEN) > 0:
    n = OPEN.pop(0)
    print(f"n = {n}")
    CLOSE.append(n)
    print(f"CLOSE = {CLOSE}")
    if n == stop:
      print(f"Tim thay duong di tu {start} -> {stop}")
      i = stop
      while i != -1:
        print(i, end="<-")
        i = FATHER[i]
      return True
    # tim dinh ke, sap xep Tn theo h va chen vao dau OPEN
    Tn = [] # reset
    for i in range(sodinh):
      if adj[n][i] == 1 and i not in OPEN and i not in CLOSE:
        Tn.append(i)
        FATHER[i] = n
      Tn = sorted(Tn, key = lambda x: h[x])
    print(f"Tn = {Tn}")

    OPEN = Tn + OPEN
    print(f"OPEN = {OPEN}")
  print(f"Khong tim thay duong di tu {start} -> {stop}")  
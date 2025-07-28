def BranchAndBound(sodinh, h, adj, start, stop):
  OPEN = [start]
  CLOSE = []
  FATHER = [-1] * sodinh
  g = [float('inf')] * sodinh
  f = [float('inf')] * sodinh
  g[start] = 0
  f[start] = h[start]

  while len(OPEN) > 0:
    n = OPEN.pop(0)

    print(f"n = {n}")

    CLOSE.append(n)
    if n == stop:
      print(f"Tim thay duong di tu {start} -> {stop}")
      i = stop
      while i != -1:
        print(i, end="<-")
        i = FATHER[i]
      return True
    Tn = []

    for i in range(sodinh):
      if adj[n][i] > 0 and i not in OPEN and i not in CLOSE:
        g[i] = g[n] + adj[n][i]
        f[i] = g[i] + h[i]
        FATHER[i] = n
        Tn.append(i)
      if adj[n][i] > 0 and i not in OPEN and i in CLOSE:
        gnew = g[n] + adj[n][i]
        fnew = gnew + h[i]
        if fnew < f[i]:
          g[i] = gnew
          f[i] = fnew
          Tn.append(i)
          FATHER[i] = n
      if adj[n][i] > 0 and i in OPEN and i not in CLOSE:
        gnew = g[n] + adj[n][i]
        fnew = gnew + h[i]
        if fnew < f[i]:
          g[i] = gnew
          f[i] = fnew
          FATHER[i] = n
    Tn = sorted(Tn, key = lambda x: f[x])
    print(f"Tn = {Tn}")
    OPEN = Tn + OPEN
  print(f"Khong tim thay duong di tu {start} -> {stop}")
  return False
      
def CMS(sodinh, adj, start, stop):
  OPEN = [start]
  CLOSE = []
  FATHER = [-1] * sodinh
  g = [float('inf')] * sodinh
  g[start] = 0
  while len(OPEN) > 0:
    # Lay min nhung da sort open o duoi nen chi can lay dau tien ra
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
    Tn = []
    for i in range(sodinh):
      # TH1 khong thuoc OPEN va CLOSE
      if adj[n][i] > 0 and i not in OPEN and i not in CLOSE:
        Tn.append(i)
        FATHER[i] = n
        g[i] = g[n] + adj[n][i]
      # TH2 thuoc OPEN thi cap nhat gnew va so sanh khong dua vao Tn
      if adj[n][i] > 0 and i in OPEN:
        gnew = g[n] + adj[n][i]
        print(f"gnew = {gnew}")
        if gnew < g[i]:
          g[i] = gnew
          print(f"Update g[{i}]")
          FATHER[i] = n;
    print(f"Tn = {Tn}")
    
    OPEN = OPEN + Tn

    print(f"OPEN = {OPEN}")

    OPEN = sorted(OPEN, key = lambda x: g[x])
    print(f"OPEN Sorted = {OPEN}")

  print(f"Khong tim thay duong di tu {start} -> {stop}")
  return False
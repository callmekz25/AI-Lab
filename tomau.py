
def tomau(sodinh, adj):
  bac = [0] * sodinh
  # Cac dinh
  OPEN = []
  for i in range(sodinh):
    OPEN.append(i)
  
  print(f'OPEN = {OPEN}')
  for i in range(sodinh):
    for j in range(sodinh):
      if adj[i][j] == 1:
        bac[i] += 1
  print(f'So bac cua do thi: {bac}')

  # Sap xep cac dinh cua do thi theo bac giam dan

  OPEN = sorted(OPEN, key = lambda x: bac[x], reverse=True)

  print(f'OPEN Sorted = {OPEN}')

  mau = 0
  color = [-1] * sodinh

  while len(OPEN) > 0:
    n = OPEN.pop(0)
    print(f'n = {n}')
    color[n] = mau
    # Cac dinh khong ke
    Tn = []
    for i in range(sodinh):
        if adj[n][i] == 0 and color[i] == -1:
          Tn.append(i)
    
    print(f'Tn = {Tn}')

    # Giu lai cac dinh khong ke nhau trong Tn
    for i in Tn:
      for j in Tn:
        # Khong phai chinh no
        if adj[i][j] == 1 and i != j:
          Tn.remove(j)
    print(f'Tn sau khi giu lai cac dinh khong ke nhau = {Tn}')
    
    for i in Tn:
      color[i] = mau
      OPEN.remove(i)
    mau += 1
    print(f'Color = {color}')



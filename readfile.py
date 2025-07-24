def readFileMtk(fileName):
    with open(fileName) as f:
        sodinh = int(f.readline())
        adj = []
        for i in range(sodinh):
            line = list(map(int, f.readline().strip().split()))
            adj.append(line)
    return sodinh, adj

def readFileHeuristic(filename):
    with open(filename) as f:        
        h = list(map(int, f.readline().strip().split()))
 
    return h
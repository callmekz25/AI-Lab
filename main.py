from readfile import readFileMtk, readFileHeuristic
from best_fs import BestFirstSearch
from hill_climbing import HillClimbing
from bfs import BFS
from bfs_test import BFS_Test
from dfs_test import DFS_Test
from dfs import DFS
from at import AT
from a_star import AStar
from cms import CMS
from branch_and_bound import BranchAndBound
if __name__ == "__main__":
    # sodinh, adj = readFileMtk("file/branch_bound.mtk")
    # sodinh, adj = readFileMtk("file/BFS.mtk")
    sodinh, adj = readFileMtk("file/DFS.mtk")
    # h = readFileHeuristic("file/branch_bound.heuristic")
    # AStar(sodinh, h, adj, 0, 10)
    # BranchAndBound(sodinh, h, adj, 0, 7)
    # CMS(sodinh, adj, 0, 7)
    # BFS(sodinh, adj, 0, 7)
    # BFS_Test(sodinh, adj, 0, 7)
    # DFS(sodinh, adj, 0, 6)
    # DFS_Test(sodinh, adj, 0, 6)
    
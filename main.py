from readfile import readFileMtk, readFileHeuristic
from best_fs import BestFirstSearch
from hill_climbing import HillClimbing
from at import AT
from cms import CMS
if __name__ == "__main__":
    sodinh, adj = readFileMtk("file/cms.mtk")
    # h = readFileHeuristic("file/AT.heuristic")
    CMS(sodinh, adj, 0, 7)
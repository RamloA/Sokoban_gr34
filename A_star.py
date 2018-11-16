import numpy as np
class Nodes:
    """"
    def _init__(self):
        self.nodes = []
    """
    def __init__(self):
            self.nodes = np.empty([8,7])

    def in_bounds(self, id):
            #self.rows = self.nodes.shape[0]
            #self.cols = self.nodes.shape[1]
            (x, y) = id
            return 0 <= x < self.width and 0 <= y < self.height

    def neighbours(self, index):
        """
        Input: 
        M: should be the the array of the map 
        """""
        (x, y) = index
        results = []
        neighbours_res = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
        """
        for neigbour in neighbours_res:
            if self.nodes[neigbour] == 1 or self.nodes[neigbour] == 2:
                results.put(neigbour)
        #neighbours_res = filter(self.in_bounds, neighbours_res)
        """
        return neighbours_res


    def heuristics(self, a, b):
        (x1, y1) = a
        ()






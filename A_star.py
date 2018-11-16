import numpy as np
class Nodes:
    """"
    def _init__(self):
        self.nodes = []
    """
    def __init__(self):
            self.nodes = np.empty([1, 1])
            self.width = self.nodes.shape[0]
            self.height = self.nodes.shape[1]
            #self.walls = []

    def in_bounds(self, id):
            (x, y) = id
            return 0 <= x < self.width and 0 <= y < self.height

    def neighbours(self, index):
        """
        Input: 
        M: should be the the array of the map 
        """""
        (x, y) = index
        neighbours_res = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
        return neighbours_res




class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]


example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}





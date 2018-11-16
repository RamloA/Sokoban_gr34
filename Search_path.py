from A_star import Nodes
import numpy as np

A_map = Nodes()

#A_map = [1, 1, 1, 1]


A_map.nodes = (
    [[0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 2, 1, 0],
     [0, 1, 1, 1, 1, 1, 0],
     [0, 2, 1, 2, 1, 2, 0],
     [0, 1, 1, 0, 1, 0, 0],
     [0, 1, 3, 2, 1, 1, 0],
     [0, 0, 0, 1, 3, 1, 0],
     [0, 0, 0, 1, 0, 1, 0]])


index = (1, 1)
N_R = A_map.neighbours(index)
print(N_R)



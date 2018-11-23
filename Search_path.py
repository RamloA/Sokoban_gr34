from A_star import *
import numpy as np

A_map = Nodes()

#A_map = [1, 1, 1, 1]


A_map.nodes = np.array([[0, 0, 0, 0, 0, 0, 0],
                        [0, 2, 1, 1, 1, 1, 0],
                        [0, 1, 1, 1, 1, 1, 0],
                        [0, 2, 0, 2, 1, 2, 0],
                        [0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 3, 1, 1, 1, 0],
                        [0, 1, 3, 1, 1, 1, 0],
                        [0, 1, 1, 0, 0, 0, 0],
                        [0, 1, 3, 1, 3, 1, 0],
                        [0, 1, 1, 1, 1, 1, 0],
                        [0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]])

print(A_map.nodes.shape)

#index = [1, 1]
"""
#ALLE INDEX skal skrives med ()
"""
index = (1,1)
print(A_map.neighbours(index))

print("HER:   ", A_map.nodes[1, 1])

Start, Goal = (8, 3), (1, 4)

Vis, cost = a_star(A_map, Start, Goal)

print("Visited: ", Vis)
print(cost)

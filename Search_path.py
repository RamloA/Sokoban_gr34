from A_star import *
import numpy as np

A_map = Nodes()
End = Nodes()
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

End.nodes = np.array([[0, 0, 0, 0, 0, 0, 0],
                        [0, 3, 1, 1, 1, 1, 0],
                        [0, 1, 1, 1, 1, 1, 0],
                        [0, 3, 0, 3, 1, 3, 0],
                        [0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 1, 1, 1, 1, 0],
                        [0, 1, 1, 1, 1, 1, 0],
                        [0, 1, 1, 0, 0, 0, 0],
                        [0, 1, 1, 1, 1, 1, 0],
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

Goals =[(1, 1), (3, 1), (3, 3), (3, 5)]

Cans = [(5, 2), (6, 2), (8, 2), (8, 4)]
Robot = (8, 5)

#print("element 1 i cans: ", Cans[1])

#print(type(Cans[1]))

#rint("element 1: ", A_map.nodes[Cans[1]])
Find_solution(A_map, Cans, Goals)

Start, Goal = (5, 2), (3, 1)


#Vis, cost = a_star(A_map, Start, Goal)

#print("Visited: ", Vis)
#print(cost)

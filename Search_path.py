from A_star import *
import numpy as np
import matplotlib.pyplot as plt
import cv2



A_map = Nodes()

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

"""
B_map = np.array([[0, 0, 0, 0, 0, 0, 0],
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
for (x,y), value in np.ndenumerate(B_map):
    #print(x, y)
    if B_map[x, y] == 2:
        B_map[x, y] = 200
        print("2")
    if B_map[x, y] == 3:
        print("3")
        B_map[x, y] = 30
    if B_map[x, y] == 1:
        print("1")
        B_map[x, y] = 100

print(B_map)
cv2.imshow("Simple_black", B_map)
cv2.resizeWindow("Simple_black", 1000, 1000)
cv2.waitKey(0)
"""


print(A_map.nodes.shape)

#index = [1, 1]
"""
#ALLE INDEX skal skrives med ()
"""
index = (1, 1)
print(A_map.neighbours(index))

print("HER:   ", A_map.nodes[1, 1])

Goals =[(1, 1), (3, 1), (3, 3), (3, 5)]

Cans = [(5, 2), (6, 2), (8, 2), (8, 4)]
Robot = (8, 5)

#print("element 1 i cans: ", Cans[1])

#print(type(Cans[1]))

#rint("element 1: ", A_map.nodes[Cans[1]])
Find_solution(A_map, Cans, Goals, Robot)

Start, Goal = (5, 2), (3, 1)


#Vis, cost = a_star(A_map, Start, Goal)

#print("Visited: ", Vis)
#print(cost)

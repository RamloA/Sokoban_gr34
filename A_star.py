import numpy as np
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

class Nodes:
    """"
    def _init__(self):
        self.nodes = []
    """
    def __init__(self):
            self.nodes = []

    def in_bounds(self, id):
            #self.rows = self.nodes.shape[0]
            #self.cols = self.nodes.shape[1]
            (x, y) = id
            return 0 <= x < self.width and 0 <= y < self.height

    def neighbours(self, index):

        [x, y] = index
        neighbours_res = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
        """
        for neigbour in neighbours_res:
            if self.nodes[neigbour] == 1 or self.nodes[neigbour] == 2:
                results.put(neigbour)
        #neighbours_res = filter(self.in_bounds, neighbours_res)
        """
        return neighbours_res




def heuristics(a, b):
    [x1, y1] = a
    [x2, y2] = b
    dist_h = (x1-x2) + (y1-y2)
    return abs(dist_h)

def a_star(plan, start, goal):
    """
          Input:
          Plan: should be the the array of the map
          open_list: is the listed of nodes we should visit
          visited: nodes we have visited
          We know distance between neighbours will always be 1 -> therefor we can hardcode the distance
    """
    open_List = PriorityQueue()
    open_List.put(start, 0)
    Visited = {}
    cost = {}
    Visited[start] = 0
    cost[start] = 0
    cost_neighbours = 1

    while not open_List.empty():
        current = open_List.get()

        if current == goal:
            break

        for next_node in plan.neighbours(current):
            if plan.nodes[next_node] == 1 or plan.nodes[next_node] == 2:
                new_cost = cost[current] + cost_neighbours

                if next_node not in cost or new_cost < cost[next_node]:
                    cost[next_node] = new_cost
                    priority = new_cost + heuristics(current, goal)
                    open_List.put(next_node, priority)
                    Visited[next_node] = current
    return Visited, cost



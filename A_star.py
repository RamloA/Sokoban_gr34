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
    def popemty(self):
        return heapq.heappop(self.elements)

class Nodes:
    """"
    def _init__(self):
        self.nodes = []
    """
    def __init__(self):
        self.nodes = []


    def neighbours(self, index):

        [x, y] = index
        neighbours_res = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]

        return neighbours_res


def heuristics(a, b):
    [x1, y1] = a
    [x2, y2] = b
    dist_h = (x1-x2) + (y1-y2)
    return abs(dist_h)

def a_star(plan_map, start, goal):
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
    closed_list = []
    totalt_cost = {}
    End = 1
    t = "false"
    while not open_List.empty():
        current = open_List.get()

        if current not in closed_list:
            closed_list.append(current)

        if current == goal:
            break

        for next_node in plan_map.neighbours(current):
            if plan_map.nodes[next_node] == 1 or plan_map.nodes[next_node] == 2:
                new_cost = cost[current] + cost_neighbours
                #print("New cost: ", new_cost, "Next_node", next_node)
                if next_node not in closed_list:
                    cost[next_node] = new_cost
                    priority = new_cost + heuristics(next_node, goal)
                    #print("Priority", priority)
                    open_List.put(next_node, priority)
                    #print("Open_l", open_List.elements)

                    Visited[next_node] = current
                    """ 
                    For this part it should be a function -> update of can movement -> should do this in moving with robot!
                    """
                    if next_node == goal:
                        plan_map.nodes[goal] = 3
                        plan_map.nodes[start] = 1
                        # if there is a path, it returns 0
                        End = 0

    #print(Visited)
    path = []
    Find_Path(Visited, start, goal, path)
    path.reverse()

    #print("Closed:  ", closed_list)
    #return Visited, cost
    return End, path

def Find_solution(plan_map, cans, goals, rob_pos):
    i = 0
    min_dist = 100
    can_goal_res = {}
    cans_res = []
    goals_res = []

    for can in cans:
        for goal in goals:
            dist = heuristics(can, goal)
            if dist < min_dist and dist > 0 and goal not in goals_res:
                min_dist = dist
                cans_s = can
                goal_s = goal
                #print("Can found", cans_s, "closest goal found; ", goal_s, "Dist:  ", dist)
            i += 1
            if i == 4:
                print("Can found", cans_s, "closest goal found; ", goal_s, "Dist:  ", dist)
                #can_goal_res[cans_s] = goal_s
                Is_there_a_path, path_can = a_star(plan_map, cans_s, goal_s)
                print("The path_can is:", path_can)
                i = 0
                min_dist = 100

                if Is_there_a_path == 0:
                    Path_from_rob_to_can = Rob_Path_can(rob_pos, cans_s, plan_map)
                    print("There is a path_can from rob to can", Path_from_rob_to_can)
                    if Path_from_rob_to_can == 0:
                        rob_pos = cans_s
                        Rob_push(rob_pos, path_can, plan_map)
                        print("NEW rob pos", rob_pos)

                        cans_res.append(cans_s)
                        goals_res.append(goal_s)


def Find_Path(V_list, start, goal, path):
    for node in V_list:
        if node == goal:
            path.append(node)
            Next_ = V_list[node]
            Find_Path(V_list, start, Next_, path)
            break

def Rob_Path_can(rob_pos, can, plan_map):
    End, path = a_star(plan_map, rob_pos, can)
    print("Robot path:", path)

    return End


def Rob_push(rob_pos, path_can, plan_map):
    i=0

    while true:
     #   print("I'm here!!")

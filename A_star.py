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

    def x (self, index):
        [x, y] = index
        return x

    def y (self, index):
        [x, y] = index
        return y
    def neighbour_State(self, index, neighbour):
        [x,y] = index
        State = None

        if neighbour == (x-1, y):
            State = "North"
        if neighbour == (x+1, y):
            State = "South"
        if neighbour == (x , y-1):
            State = "West"
        if neighbour == (x, y+1):
            State = "East"
        return State


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
    print("_______________________________A_star_______________________________")
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
    path = []
    while not open_List.empty():
        current = open_List.get()

        if current not in closed_list:
            closed_list.append(current)

        if current == goal:
            break

        for next_node in plan_map.neighbours(current):
            if plan_map.nodes[next_node] == 1 or plan_map.nodes[next_node] == 2:
                new_cost = cost[current] + cost_neighbours
                if next_node not in closed_list:
                    cost[next_node] = new_cost
                    priority = new_cost + heuristics(next_node, goal)
                    open_List.put(next_node, priority)
                    Visited[next_node] = current
                    """ 
                    For this part it should be a function -> update of can movement -> should do this in moving with robot!
                    """
                    if next_node == goal:
                        #plan_map.nodes[goal] = 3
                        #plan_map.nodes[start] = 1
                        # if there is a path, it returns 0
                        End = 0

            if plan_map.nodes[next_node] == 3 and next_node == goal:
                Visited[next_node] = current
                End = 0

    #print(Visited)

    Find_Path(Visited, start, goal, path)
    path.reverse()

    #print("Closed:  ", closed_list)
    #return Visited, cost
    return End, path

def Find_solution(plan_map, cans, goals, rob_pos):
    print("_______________________________Finding a solution_______________________________")
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
                    print("Finding a path from Rob to can")
                    print("There is a path_can from rob to can", Path_from_rob_to_can)
                    if Path_from_rob_to_can == 0:
                        rob_pos = cans_s
                        Rob_push(rob_pos, cans_s, path_can, plan_map)

                        print("NEW rob pos", rob_pos)

                        cans_res.append(cans_s)
                        goals_res.append(goal_s)


def Find_Path(V_list, start, goal, path):
    #print("_______________________________Find path _______________________________")
    for node in V_list:
        if node == goal:
            path.append(node)
            Next_ = V_list[node]
            Find_Path(V_list, start, Next_, path)
            break

def Rob_Path_can(rob_pos, can, plan_map):
    print("_______________________________Robot paths to can_______________________________")
    End, path = a_star(plan_map, rob_pos, can)
    print("Robot path:", path)
    return End


def Rob_push(rob_pos, goal, path_can, plan_map):
    print("_______________________________Robots pushing strategy_______________________________")
    i = 0
    path = []

    #while rob_pos != goal:
    len_path = len(path_can)
    for node in path_can:
        i += 1
        if node == rob_pos:
            previous = node
            path.append(node)
            print("current position", node)
            continue
        if node == goal:
            break
        if i == 2:
            previous_state = plan_map.neighbour_State(previous, node)
            print("Previous_state", previous_state)
        for x in plan_map.neighbours(node):
            if i < len_path:
                if x == path_can[path_can.index(node)+1]:
                    print("Node", node, "next ", x)
                    #end, path = a_star(plan_map, node, x)
                    State = plan_map.neighbour_State(node, x)
                    if State == "North":
                        print("State: " + State)
                        if previous_state == State:
                            push(node, previous, plan_map)
                            previous_state = State
                            path.append(node)
                            rob_pos = node
                        elif previous_state != State:
                            push(node, previous, plan_map)
                            print("different from previous  " + previous_state)
                            print("robot ", rob_pos)
                            end, patha = a_star(plan_map, rob_pos, x)
                            print("patha", patha)
                            previous_state = State
                            path.append(node)

                    if State == "South":
                        print("State: " + State)
                        if previous_state == State:
                            push(node, previous, plan_map)
                            previous_state = State
                            path.append(node)
                            rob_pos = node
                        elif previous_state != State:
                            print("different from previous  " + previous_state)
                            previous_state = State
                            path.append(node)

                    if State == "West":
                        print("State: " + State)
                        if previous_state == State:
                            push(node, previous, plan_map)
                            previous_state = State
                            path.append(node)
                            rob_pos = node
                        elif previous_state != State:
                            print("different from previous  " + previous_state)
                            previous_state = State
                            path.append(node)

                    if State == "East":
                        print("State: " + State)
                        if previous_state == State:
                            push(node, previous, plan_map)
                            previous_state = State
                            path.append(node)
                            rob_pos = node
                            print("East robot new", rob_pos)
                        elif previous_state != State:
                            print("different from previous  " + previous_state)
                            previous_state = State
                            path.append(node)
            previous = node


    print("Path push", path)
    print(plan_map)


def push(node, previous_node, plan_map):
    #print("Before can", plan_map.nodes[node])
    plan_map.nodes[node] = 3
    #print("After can", plan_map.nodes[node])
    #print("Can earlier", plan_map.nodes[previous_node])
    plan_map.nodes[previous_node] = 1
    #print("Can moved", plan_map.nodes[previous_node])

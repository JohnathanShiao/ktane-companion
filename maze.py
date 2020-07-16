from collections import defaultdict, deque

# Undirected connected graph class RENAME to maze class and adjust

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    # Add a coordinate to the graph and connect it to the four surrouding
    # Add in order left down up right for sorting ease
    def add_node(self, num):
        s_num = str(num)
        if s_num[0] != '1':
            self.graph[num].append(num - 10) # left
        if s_num[1] != '1':
            self.graph[num].append(num - 1) # down
        if s_num[1] != '6':
            self.graph[num].append(num + 1) # up
        if s_num[0] != '6':
            self.graph[num].append(num + 10) # right

    # Adds walls by removing edges in the adjacency lists
    def add_wall_up(self, u):
        self.graph[u].remove(u + 1)
        self.graph[u + 1].remove(u)

    def add_wall_right(self, u):
        self.graph[u].remove(u + 10)
        self.graph[u + 10].remove(u)

    # Return the shortest path from s to t as an array of points including s and t
    def BFS(self, s, t):
        
        # If the goal is the location where it started, return s (aka t)
        if s == t:
            return [s]

        visited = defaultdict(list)
        prior_to = defaultdict(list)
        for key in self.graph.keys(): # Init defaultdict key values to False
            visited[key] = False
        queue = []  # BFS Queue

        # Mark the source node as visited and enqueue it
        queue.append(s)
        prior_to[s] = None
        visited[s] = True

        while queue:

            # Dequeue a vertex
            s = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it visited and
            # enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    prior_to[i] = s
                    if (i == t):
                        del queue[:]
                        break
                    queue.append(i)
                    visited[i] = True

        instructions = deque()
        while prior_to[t] != None:
            instructions.appendleft({'direction': get_instr(prior_to[t], t), 'from': prior_to[t], 'to': t})
            t = prior_to[t] 
        return instructions

def get_instr(source, dest):
        diff = dest - source
        if diff == 10:
            return 'right'
        if diff == -10:
            return 'left'
        if diff == 1:
            return 'up'
        if diff == -1:
            return 'down'

# Testing code for MAZE 1 (1, 5)

def run_test():
    # Add all coordinates and connect them
    g = Graph()
    for i in range(1, 7):
        for j in range(1, 7):
            g.add_node(i * 10 + j)

    # Add walls where necessary, removes connections in graph representation
    # REDO so walls added go in increasing order, eg go up by y first then right by x
    g.add_wall_up(21)
    g.add_wall_right(21)
    g.add_wall_right(41)
    g.add_wall_up(51)
    g.add_wall_up(22)
    g.add_wall_right(32)
    g.add_wall_up(32)
    g.add_wall_up(42)
    g.add_wall_up(52)
    g.add_wall_right(52)
    g.add_wall_right(13)
    g.add_wall_up(23)
    g.add_wall_right(43)
    g.add_wall_up(53)
    g.add_wall_right(14)
    g.add_wall_up(34)
    g.add_wall_right(34)
    g.add_wall_up(44)
    g.add_wall_up(54)
    g.add_wall_right(15)
    g.add_wall_up(25)
    g.add_wall_right(35)
    g.add_wall_up(55)
    g.add_wall_up(65)
    g.add_wall_right(36)

    instructions = g.BFS(52, 51)

    for i in range(0, len(instructions)):
        instr_dict = instructions[i]
        print('Step {}: Go {} from ({}, {}) to ({}, {}).'.format(i + 1, instr_dict['direction'], \
            str(instr_dict['from'])[0], str(instr_dict['from'])[1], str(instr_dict['to'])[0], str(instr_dict['to'])[1]))

run_test()
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
            return 'RIGHT'
        if diff == -10:
            return 'LEFT'
        if diff == 1:
            return 'UP'
        if diff == -1:
            return 'DOWN'

#Determine which maze is being used
def selectMaze():
    numx = 0
    numy = 0
    valid = 0
    #sanitize the coordinates
    while not valid:
        numx = input("\nPlease input the x coordinate of ONE of the green circle: (1-6)\n")
        try:
            numx = int(numx)
            if numx>0 and numx<7:
                valid = 1
        except ValueError:
            numx = input("\nError: Coordinates need to be an integer between 1-6:\n")
    valid = 0
    while not valid:
        numy = input("\nPlease input the y coordinate of the SAME green circle: (1-6)\n")
        try:
            numy =int(numy)
            if numy>0 and numy<7:
                valid = 1
        except ValueError:
            numy = input("\nError: Coordinates need to be an integer between 1-6:\n")
    #concatenate the coordinates
    num = numx*10 + numy
    #initialize graph
    g = Graph()
    for i in range(1, 7):
        for j in range(1, 7):
            g.add_node(i * 10 + j)
    if num == 15 or num == 64:
        #MAZE 1
        u = [21,51,22,32,42,52,23,53,34,44,54,25,55,65]
        r = [21,41,32,52,13,43,14,34,15,35,36]
        for x in u:
            g.add_wall_up(x)
        for y in r:
            g.add_wall_right(y)
    elif num == 23 or num == 55:
        #MAZE 2
        u = [51,22,42,33,53,24,44,54,15,35,65]
        r = [11,31,12,22,32,52,23,43,53,14,34,25,45,36]
        for x in u:
            g.add_wall_up(x)
        for y in r:
            g.add_wall_right(y)       
    elif num == 43 or num == 63:
        #MAZE 3
        u = [21,31,14,44,54,25]
        r = [41,12,32,42,52,13,23,33,43,53,24,34,54,15,25,35,55,36,46]
        for x in u:
            g.add_wall_up(x)
        for y in r:
            g.add_wall_right(y)
    elif num == 13 or num == 16:
        #MAZE 4
        u = [21,31,41,22,32,42,52,23,33,53,44,54,35,45,55]
        r = [31,51,25,13,14,34,54,15,25,26]
        for x in u:
            g.add_wall_up(x)
        for y in r:
            g.add_wall_right(y)
    elif num == 41 or num == 54:
        #MAZE 5
        u = [31,41,51,22,32,52,33,43,24,34,54,64,15,25,35,45]
        r = [11,12,52,13,43,53,24,44,55]
        for x in u:
            g.add_wall_up(x)
        for y in r:
            g.add_wall_right(y)
    elif num == 32 or num == 56:
        #MAZE 6
        u = [21,31,51,12,23,33,63,54,45]
        r = [41,22,32,42,23,43,53,24,34,44,15,25,35,55,16,36]
        for x in u:
            g.add_wall_up(x)
        for y in r:
            g.add_wall_right(y)
    elif num == 21 or num == 26:
        #MAZE 7
        u = [21,31,41,42,52,13,23,43,63,34,44,54,25,35]
        r = [12,22,52,23,53,24,44,15,35,55,46]
        for x in u:
            g.add_wall_up(x)
        for y in r:
            g.add_wall_right(y)
    elif num == 33 or num == 46:
        #MAZE 8
        u = [31,41,51,61,22,42,52,62,33,43,24,34,44,54,35]
        r = [12,22,13,33,14,54,35,55,16,46]
        for x in u:
            g.add_wall_up(x)
        for y in r:
            g.add_wall_right(y)
    elif num == 12 or num == 35:
        #MAZE 9
        u = [61,42,52,23,33,53,44,35,45]
        r = [21,41,12,22,32,52,13,23,43,34,54,15,25,45,55,16]
        for x in u:
            g.add_wall_up(x)
        for y in r:
            g.add_wall_right(y)
    else:
        print("\nNot a valid maze!\n")
    return g

def mazeStart():
    valid = 0
    while not valid:
        x = input("\nPlease input the x coordinate of the WHITE dot: (1-6)\n")
        try:
            x = int(x)
            if x >0 and x<7:
                valid = 1
        except ValueError:
            x = input("\nError: Coordinate must be between 1-6:\n")
    valid = 0
    while not valid:
        y = input("\nPlease input the y coordinate of the WHITE dot: (1-6)\n")
        try:
            y = int(y)
            if y>0 and y<7:
                valid = 1
        except ValueError:
            y = input("\nError: Coordinate must be between 1-6:\n")
    return x*10 + y

def mazeEnd():
    valid = 0
    while not valid:
        x = input("\nPlease input the x coordinate of the RED triangle: (1-6)\n")
        try:
            x = int(x)
            if x >0 and x<7:
                valid = 1
        except ValueError:
            x = input("\nError: Coordinate must be between 1-6:\n")
    valid = 0
    while not valid:
        y = input("\nPlease input the y coordinate of the RED triangle: (1-6)\n")
        try:
            y = int(y)
            if y>0 and y<7:
                valid = 1
        except ValueError:
            y = input("\nError: Coordinate must be between 1-6:\n")
    return x*10 + y

def maze():
    # Add all coordinates and connect them
    g = selectMaze()
    start = mazeStart()
    end = mazeEnd()
    print("START: {},{}\nEND: {},{}".format(start/10,start%10,end/10,end%10))
    # Add walls where necessary, removes connections in graph representation
    # REDO so walls added go in increasing order, eg go up by y first then right by x
    instructions = g.BFS(start, end)

    for i in range(0, len(instructions)):
        instr_dict = instructions[i]
        print('Step {}: Go {} from ({}, {}) to ({}, {}).'.format(i + 1, instr_dict['direction'], \
            str(instr_dict['from'])[0], str(instr_dict['from'])[1], str(instr_dict['to'])[0], str(instr_dict['to'])[1]))

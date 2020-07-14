from collections import defaultdict

# Undirected connected graph class RENAME to maze class and adjust


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    # Add a coordinate to the graph and connect it to the four surrouding
    def add_coord(self, u):
        if u.y != 6:
            self.graph[u].append(Coordinate(u.x, u.y + 1))  # up
        if u.y != 1:
            self.graph[u].append(Coordinate(u.x, u.y - 1))  # down
        if u.x != 6:
            self.graph[u].append(Coordinate(u.x + 1, u.y))  # right
        if u.x != 1:
            self.graph[u].append(Coordinate(u.x - 1, u.y))  # left

    # Adds wall by removing edge connection, might be able to make this more efficient
    def add_wall(self, u, v):
        for key in self.graph:
            if (key.x == u.x and key.y == u.y):
                key_u = key
            if (key.x == v.x and key.y == v.y):
                key_v = key

        for coord in self.graph[key_u]:
            if coord.x == v.x and coord.y == v.y:
                self.graph[key_u].remove(coord)

        for coord in self.graph[key_v]:
            if coord.x == u.x and coord.y == u.y:
                self.graph[key_v].remove(coord)

    def BFS(self, s):
        visited = [False] * (len(self.graph))
        queue = []  # BFS Queue

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex
            s = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it visited and
            # enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# Maybe instead of storing coordinates as (1, 2), (4, 4) we store as 12, 44 to skip over need for class?
class Coordinate:

    # Add compare to method later

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dir_to(self, to_coord):
        if self.x == to_coord.x:
            if (self.y + 1 == to_coord.y):
                return 'up'
            elif (self.y - 1 == to_coord.y):
                return 'down'
        elif self.y == to_coord.y:
            if (self.x + 1 == to_coord.x):
                return 'right'
            elif (self.x - 1 == to_coord.x):
                return 'left'
        else:
            return 'Error, the two coordinates are not one cardinal step apart.'

    def __str__(self):
        return f'({self.x}, {self.y})'


# Testing code for MAZE 1 (1, 5)

# Add all coordinates and connect them (special cases for edge coordinates)
g = Graph()
for i in range(1, 7):
    for j in range(1, 7):
        g.add_coord(Coordinate(i, j))

# Add walls where necessary, removes connections in graph representation
# DEFINITELY SIMPLIFY by defining funcs to add a wall above and to the left, a bit less wordy and less prone to error? 
g.add_wall(Coordinate(2, 1), Coordinate(2, 2))
g.add_wall(Coordinate(2, 1), Coordinate(3, 1))
g.add_wall(Coordinate(4, 1), Coordinate(5, 1))
g.add_wall(Coordinate(5, 1), Coordinate(5, 2))
g.add_wall(Coordinate(2, 2), Coordinate(2, 3))
g.add_wall(Coordinate(3, 2), Coordinate(4, 2))
g.add_wall(Coordinate(3, 2), Coordinate(3, 3))
g.add_wall(Coordinate(4, 2), Coordinate(4, 3))
g.add_wall(Coordinate(5, 2), Coordinate(5, 3))
g.add_wall(Coordinate(5, 2), Coordinate(6, 2))
g.add_wall(Coordinate(1, 3), Coordinate(2, 3))
g.add_wall(Coordinate(2, 3), Coordinate(2, 4))
g.add_wall(Coordinate(4, 3), Coordinate(5, 3))
g.add_wall(Coordinate(5, 3), Coordinate(5, 4))
g.add_wall(Coordinate(1, 4), Coordinate(2, 4))
g.add_wall(Coordinate(3, 4), Coordinate(3, 5))
g.add_wall(Coordinate(3, 4), Coordinate(4, 4))
g.add_wall(Coordinate(4, 4), Coordinate(4, 5))
g.add_wall(Coordinate(5, 4), Coordinate(5, 5))
g.add_wall(Coordinate(1, 5), Coordinate(2, 5))
g.add_wall(Coordinate(2, 5), Coordinate(2, 6))
g.add_wall(Coordinate(3, 5), Coordinate(4, 5))
g.add_wall(Coordinate(5, 5), Coordinate(5, 6))
g.add_wall(Coordinate(6, 5), Coordinate(6, 6))
g.add_wall(Coordinate(3, 6), Coordinate(4, 6))

for coord in g.graph.keys():
    print('\n')
    print('{}: '.format(coord), end="")
    for edgeto in g.graph[coord]:
        print(edgeto, end="")

print('\n')

"""
# Create a graph given in 
# the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)") 
g.BFS(2) 
"""

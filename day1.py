class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    def __init__(self):
        #keys are all verts in graph, values are sets of adjacent verts 
        self.vertices = {} 
        
    def add_vertex(self, vertex):
        #Add new unconnected vertex
        self.vertices[vertex] = set()
        
    def add_edge(self, v_from, v_to):
        #connect two nodes
        if v_from in self.vertices and v_to in self.vertices:
            self.vertices[v_from].add(v_to)
        else:
            raise IndexError("Nonexistent vertex")
        
    def is_connected(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            return v_to in self.vertices[v_from]
        else:
            raise IndexError("Nonexistent vertex")
        
    def get_neighbors(self, vertex):
        return self.vertices[vertex]
    
    def bft(self, starting_vertex_id):
        q = Queue()
        visited = set()
        
        #initialization phase
        q.enqueue(starting_vertex_id)
        
        #main loop
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v) #'Visit' the node
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
                
        
        
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)

g.add_edge(2, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

print(g.vertices)
g.bft(1)
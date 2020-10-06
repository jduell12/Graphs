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
                
    def dft(self, starting_vertex_id):
        s = Stack()
        visited = set()
        
        #initialization phase
        s.push(starting_vertex_id)
        
        #main loop
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)
                    
    def dft_recursive(self, starting_vertex, visited=set()):        
        #visit node
        print(starting_vertex)
        visited.add(starting_vertex)
        
        #traverse starting vertex neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
                    
    def bfs(self, starting_vertex_id, target_vertex):
        q = Queue()
        visited = set()
        
        #init
        q.enqueue([starting_vertex_id])
        
        #while queue is not empty
        while q.size() > 0:
            #get path from queue
            path = q.dequeue()
            #get last vertex in path
            v = path[-1]
            
            if v not in visited:
                if v == target_vertex:
                    return path
                visited.add(v)
                
                for neighbor in self.get_neighbors(v):
                    newPath = path.copy()
                    newPath.append(neighbor)
                    q.enqueue(newPath)
                    
    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        visited = set()
        
        s.push([starting_vertex])
        
        while s.size() > 0:
            #get last path added to stack
            path = s.pop()
            #get last vertex on the path
            v = path[-1]
            
            #check if the vertex has been visited 
            if v not in visited:
                #check if vertex is destination
                if v is destination_vertex:
                    return path
                
                #add to visited 
                visited.add(v)
                
                #add a path to the v's neighbors to the front of the stack
                for neighbor in self.get_neighbors(v):
                    newPath = path.copy()
                    newPath.append(neighbor)
                    s.push(newPath)            
        
    def dfs_recursive(self, starting_vertex, target_vertex, visited=None, path=None):        
        
        if visited is None:
            visited = set()
        
        if path is None:
            path = []
            
            
        if starting_vertex == target_vertex:
            return path
        
        #visit node
        visited.add(starting_vertex)
        path += starting_vertex
        
        #traverse starting vertex neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                n_path = self.dfs_recursive(neighbor, target_vertex, visited, path)
                if n_path:
                    return n_path
        return 'Target vertex not in the graph' 
        
g = Graph()
g.add_vertex('A')
g.add_vertex('y')
g.add_vertex('x')
g.add_vertex('z')

g.add_edge('A', 'x')
g.add_edge('A', 'y')
g.add_edge('y', 'z')
g.add_edge('x', 'A')
g.add_edge('z', 'x')

print(g.vertices)
print("")

print(g.dfs_recursive('A', 'x'))
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
        
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)

g.add_edge(2, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

print(g.vertices)
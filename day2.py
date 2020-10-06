from day1 import Graph

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)

g.add_edge(2, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)

print(g.vertices)
g.bft(1)
print("")
g.dft(1)
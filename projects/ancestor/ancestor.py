import sys
sys.path.append('../graph')

from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    #create empty graph
    tree = Graph()
    
    #loop through the ancestors and add them to the graph
    for relationship in ancestors:
        parent = relationship[0]
        child = relationship[1]

        #check if each vertex is in the tree already
        if parent not in tree.vertices:
            tree.add_vertex(parent)
            
        if child not in tree.vertices:
            tree.add_vertex(child)
            
        #add the directed edge from the child to the parent 
        tree.add_edge(child, parent)
            
    return tree.vertices
    
    
if __name__ == '__main__':
    family = [(1,3), (2,3), (3,6), (5,6), (5, 7), (4,5), (4,8), (8,9), (11, 8), (10,1)]
    
    print(earliest_ancestor(family, 6))
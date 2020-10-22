import sys
sys.path.append('../graph')

from graph import Graph
from util import Queue

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
        
    #create queue and add starting node to queue as a path
    q = Queue()
    q.enqueue([starting_node])
    
    #create list of the current longest path 
    longest_path = []
    
    #loop while q is not empty
    while q.size() > 0:
        path = q.dequeue()
        
        #checks if current path is the same as the prior longest path, if it is keep the path with the smaller value
        if len(path) == len(longest_path) and path[-1] < longest_path[-1]:
            longest_path = path
        #if the current path is longer than the current longest path replace the current longest path with the current path
        if len(path) > len(longest_path):
            longest_path = path 
            
        #add neighbors to the queue
        for neighbor in tree.get_neighbors(path[-1]):
            newPath = path.copy()
            newPath.append(neighbor)
            q.enqueue(newPath)
    
    #check if the longest path has more than 1 node
    if len(longest_path) > 1:
        return longest_path[-1]
    else:
        return -1
    
    
if __name__ == '__main__':
    family = [(1,3), (2,3), (3,6), (5,6), (5, 7), (4,5), (4,8), (8,9), (11, 8), (10,1)]
    
    print(earliest_ancestor(family, 6))
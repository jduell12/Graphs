#each number is a node 
#edges are up, down, left and right except for the edges of the graph
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

islands_2 = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]


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


def island_counter(islands):
    counter = 0
    visited = set()
    
    def get_neighbors(coords):
        row, col = coords
        neighbors = []
        
        if row > 0 and islands[row-1][col] == 1:
            neighbors.append((row-1, col))
        
        if row < len(islands) - 1 and islands[row+1][col] == 1:
            neighbors.append((row+1, col))
            
        if col > 0 and islands[row][col-1] == 1:
            neighbors.append((row, col-1))
            
        if col < len(islands[row]) -1 and islands[row][col+1] == 1:
            neighbors.append((row, col+1))
            
        return neighbors
    
    def bft(row, col):
        q = Queue()
        q.enqueue((row, col))
        
        while q.size() > 0:
            coords = q.dequeue()
            
            if coords not in visited:
                visited.add(coords)
                
                for neighbor in get_neighbors(coords):
                    q.enqueue(neighbor)
    
    #for all nodes in the graph
    for row in range(len(islands)):
        for col in range(len(islands[row])):
            node_val = islands[row][col]
            island = (row, col)
            #if find an unvisited 1 node
            if island not in visited and node_val == 1:
                #BFT from that node 
                bft(row, col)
                #increment the counter
                counter += 1
        
    #return counter 
    return counter


print(island_counter(islands)) # returns 4
print(island_counter(islands_2)) #returns 13
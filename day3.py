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

#each number is a node 
#edges are up, down, left and right except for the edges of the graph
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

def bft(row, col):
    pass

def island_counter(islandList):
    counter = 0
    visited = set()
    
    #for all nodes in the graph
    for row in range(len(islands)):
        for col in range(len(islands[row])):
            node_val = islands[row][col]
            island = (row, col)
            #if find an unvisited 1 node
            if node_val == 1 and island not in visited:
                visited.add(island)
                #BFT from that node 
                bft(row, col)
                #increment the counter
                counter += 1
    print(visited)
        
    #return counter 
    return counter


print(island_counter(islands)) # returns 4
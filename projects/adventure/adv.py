from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt" #Main maze once done

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#traversal graph
traversal_graph = {}

print('')

#go until the traversal graph has the same length as the room graph 
while len(traversal_graph) < len(room_graph):
    # print(player.current_room.id)
    # print('graph',traversal_graph)
    # print('path', traversal_path)
    # print("")
    
    #get current room exits
    exits = player.current_room.get_exits()
    
    #put room into the traversal graph with the exits that it has 
    if player.current_room.id not in traversal_graph:
        traversal_graph[player.current_room.id] = {}
        #goes through each direction in the exit list
        for direc in exits:
            #puts ? in each direction to mark as unexplored 
            traversal_graph[player.current_room.id][direc] = '?'
    
    #checks if we have visited all rooms before moving again
    if len(traversal_graph) == len(room_graph):
        break
    
    #get the first unexplored room
    for direc in traversal_graph[player.current_room.id]:
        if traversal_graph[player.current_room.id][direc] == '?':
            traversal_path.append(direc)
            old_room = player.current_room.id
            player.travel(direc)
            traversal_graph[old_room][direc] = player.current_room.id
            break
    
print('path', traversal_path)
print('graph', traversal_graph)


# ---------------------- TRAVERSAL TEST ----------------------
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

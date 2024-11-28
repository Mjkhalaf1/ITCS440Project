import random
mazeSize = 5
mazeBlocks = {}
# create a 8x8 maze grid full of obstacles. A key-value pair will be assigned to every block of this maze.
# The key is the index of this block, and the value is a list of two values.
# The first value of the list is either 0 (obstacle) or 1 (passage). The second value is heuristic value (initially -1).
for i in range(1, mazeSize + 1):
    for j in range(1, mazeSize + 1):
        mazeBlocks[(i,j)] = [0,-1]

def mazeGenerator():
    for i in range(1,5+1):  
        obstacle = random.randint(1,3)
        path = 5 - obstacle
        while path > 0:
            currentRandom = random.randint(1,5)
            if mazeBlocks[(i,currentRandom)][0] == 0:
                mazeBlocks[(i,currentRandom)][0] = 1
                path -= 1
    while True:
        initial = random.randint(1,5)
        if(mazeBlocks[(1,initial)][0]) == 0:
            mazeBlocks[(1,initial)][0] = "I"
            break
        
    while True:
        goal = random.randint(1,5)
        if(mazeBlocks[(5,goal)][0]) == 0:
            mazeBlocks[(5,goal)][0] = "G"
            break

mazeGenerator()

# printing the maze
k = 0
for i in mazeBlocks.values():
    print(i[0], end=" ")
    k += 1
    if k == mazeSize:
        print("")
        k = 0
print("\n")

goal= 0
for i,j in mazeBlocks.items():
    
    if(mazeBlocks[i][0] == "G"):
        goal = i[1]
initial = 0
for i,j in mazeBlocks.items():
    
    if(mazeBlocks[i][0] == "I"):
        initial = i[1]

      
def dfs():
    stack = []
    stack.append((1,initial))
    while stack:
        # Give me the index of the last visited node
        i,j = stack[(len(stack)-1)][0] , stack[(len(stack)-1)][1]
        # if it is the goal, print we have a goal:
        if mazeBlocks[(i,j)][0] == "G":
            return True
        # mark it as visited(2 for visited)
        mazeBlocks[(i,j)][1] = 2
        # let's initialize temp to know if there is any valid neighbour
        temp = []
        # Right neighbour
        if (i,j+1) in mazeBlocks and (mazeBlocks[(i,j+1)][0] == 1 or mazeBlocks[(i,j+1)][0] == "G") and mazeBlocks[(i,j+1)][1] != 2:
            temp.append((i,j+1))
        # Left neighbour
        if (i,j-1) in mazeBlocks and (mazeBlocks[(i,j-1)][0] == 1 or mazeBlocks[(i,j-1)][0] == "G") and mazeBlocks[(i,j-1)][1] != 2:
            temp.append((i,j-1))
        # top neighbour
        if (i-1,j) in mazeBlocks and (mazeBlocks[(i-1,j)][0] == 1 or mazeBlocks[(i-1,j)][0] == "G") and mazeBlocks[(i-1,j)][1] != 2:
            temp.append((i-1,j))
        # bottom neighbour
        if (i+1,j) in mazeBlocks and (mazeBlocks[(i+1,j)][0] == 1 or mazeBlocks[(i+1,j)][0] == "G") and mazeBlocks[(i+1,j)][1] != 2:
            temp.append((i+1,j))
        # if temp has something, select the last node(or any one) and put it in the stack
        if temp:
            stack.append(( temp[(len(temp)-1)][0] , temp[(len(temp)-1)][1] ))
        else:
            stack.pop()
    return False
print(dfs())




# mannhatan Distance
for i in range(1, mazeSize + 1):
    for j in range(1, mazeSize + 1):
        mazeBlocks[(i,j)][1] = abs(i - mazeSize) + abs(j - goal)
# printing the 
k = 0
for i in mazeBlocks.values():
    print(i[1], end=" ")
    k += 1
    if k == mazeSize:
        print("")
        k = 0
print("\n")

'''
# A* algorithm

i,j = 1, initial

open = []
close = []
result = "The solution"
while True:
    if mazeBlocks[(i,j)][0] == "G":
        print("We have reached to the goal")
    if (i+1,j) in mazeBlocks and mazeBlocks[(i+1,j)][0] == 1:
        open.append(((i+1,j), mazeBlocks[(i+1,j)][1]))
    if (i-1,j) in mazeBlocks and mazeBlocks[(i-1,j)][0] == 1:
        open.append(((i-1,j), mazeBlocks[(i-1,j)][1]))
    if (i,j+1) in mazeBlocks and mazeBlocks[(i,j+1)][0] == 1:
        open.append(((i,j+1), mazeBlocks[(i,j+1)][1]))
    if (i,j-1) in mazeBlocks and mazeBlocks[(i,j-1)][0] == 1:
        open.append(((i,j-1), mazeBlocks[(i,j-1)][1]))
    print(open)
    for c in range(len(open)):
        min = open[0][1]
        index = 0
        if open[c][1] <= min:
            min = open[c][1]
            index = c
    current = open[0]
    open[0] = open[index]
    open[index] = current
    break
print(open)    
'''



   
   


        
    



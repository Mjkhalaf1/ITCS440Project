import random
mazeSize = 5
mazeBlocks = {}
# create a 8x8 maze grid full of obstacles. A key-value pair will be assigned to every block of this maze.
# The key is the index of this block, and the value is a list of two values.
# The first value of the list is either 0 (obstacle) or 1 (passage). The second value is heuristic value (initially -1).
for i in range(1, mazeSize + 1):
    for j in range(1, mazeSize + 1):
        mazeBlocks[(i,j)] = [0,-1]

#print(mazeBlocks) 

goal = 0
initial = 0
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
# printing the maze
mazeGenerator()
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
        initial = i[0]
        
        
start = (1,initial)
stack = []
stack.append(start)
final = False
while not final:
    temp = []
    # Specify the indexes of the last visited node
    i,j = stack[len(stack)-1][0] , stack[len(stack)-1][1]
    # Add the neighbours to the temp list if they exist and they are obstacles
    if (i+1,j) in mazeBlocks and mazeBlocks[(i+1,j)][0] == 1 and mazeBlocks[(i+1,j)][1] != 2:
        temp.append((i+1,j))
    if (i-1,j) in mazeBlocks and mazeBlocks[(i-1,j)][0] == 1 and mazeBlocks[(i+1,j)][1] != 2:
        temp.append((i-1,j))
    if (i,j+1) in mazeBlocks and mazeBlocks[(i,j+1)][0] == 1 and mazeBlocks[(i+1,j)][1] != 2:
        temp.append((i,j+1))
    if (i,j-1) in mazeBlocks and mazeBlocks[(i,j-1)][0] == 1 and mazeBlocks[(i+1,j)][1] != 2:
        temp.append((i,j-1))
    # if there are no neighbours that are obstacles, do not visit a new node and remove last visited node
    if temp:
        randomNode = random.choice(temp)
        mazeBlocks[randomNode][1] = 2
        stack.append(randomNode)   
        if randomNode == (5,goal):
            final = True 
            print("We have reached to the goal")
    else:
        break
'''








# A* algorithm
for i in range(1, mazeSize + 1):
    for j in range(1, mazeSize + 1):
        mazeBlocks[(i,j)][1] = abs(i - mazeSize) + abs(j - goal)
        
for i in mazeBlocks.values():
    print(i[1], end=" ")
    k += 1
    if k == mazeSize:
        print("")
        k = 0
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
             

# DFS to guarantee a solution
#
#

'''
'''
start = (1,initial)
stack = []
stack.append(start)
final = False
while not final:
    temp = []
    # Specify the indexes of the last visited node
    i,j = stack[len(stack)-1][0] , stack[len(stack)-1][1]
    # Add the neighbours to the temp list if they exist and they are obstacles
    if (i+1,j) in mazeBlocks and mazeBlocks[(i+1,j)][0] == 1 and mazeBlocks[(i+1,j)][1] != 2:
        temp.append((i+1,j))
    if (i-1,j) in mazeBlocks and mazeBlocks[(i-1,j)][0] == 1 and mazeBlocks[(i+1,j)][1] != 2:
        temp.append((i-1,j))
    if (i,j+1) in mazeBlocks and mazeBlocks[(i,j+1)][0] == 1 and mazeBlocks[(i+1,j)][1] != 2:
        temp.append((i,j+1))
    if (i,j-1) in mazeBlocks and mazeBlocks[(i,j-1)][0] == 1 and mazeBlocks[(i+1,j)][1] != 2:
        temp.append((i,j-1))
    # if there are no neighbours that are obstacles, do not visit a new node and remove last visited node
    if temp:
        randomNode = random.choice(temp)
        mazeBlocks[randomNode][1] = 2
        stack.append(randomNode)   
        if randomNode == (5,goal):
            final = True 
            print("We have reached to the goal")
'''
   
   


        
    

# implement DFS to create a path from top left (1,1)[satrting state] to bottom right (8,8)
   
'''   

start = (1,1)
mazeBlocks[start][0] = 1
stack = []
stack.append(start)
final = False
while not final:
    temp = []
    # Specify the indexes of the last visited node.
    i,j = stack[len(stack)-1][0] , stack[len(stack)-1][1]
    # Add the neighbours to the temp list if they exist and they are obstacles
    if (i+1,j) in mazeBlocks and mazeBlocks[(i+1,j)][0] == 0:
        temp.append((i+1,j))
    if (i-1,j) in mazeBlocks and mazeBlocks[(i-1,j)][0] == 0:
        temp.append((i-1,j))
    if (i,j+1) in mazeBlocks and mazeBlocks[(i,j+1)][0] == 0:
        temp.append((i,j+1))
    if (i,j-1) in mazeBlocks and mazeBlocks[(i,j-1)][0] == 0:
        temp.append((i,j-1))
    # if there are no neighbours that are obstacles, do not visit a new node and remove last visited node
    if temp:
        randomNode = random.choice(temp)
        mazeBlocks[randomNode][0] = 1
        stack.append(randomNode)   
        if randomNode == (mazeSize,mazeSize):
            final = True 
    else:
        stack.pop()
# print the current 8x8 maze
k = 0
for i in mazeBlocks.values():
    print(i[0], end=" ")
    k += 1
    if k == mazeSize:
        print("")
        k = 0

print("\n")
'''
    
# Manhattan distance as a hueristic value, Ali will do it :)
'''
for i in range(1, mazeSize + 1):
    for j in range(1, mazeSize + 1):
        mazeBlocks[(i,j)][1] = abs(i - mazeSize) + abs(j - mazeSize)
'''

'''
Print maze in terms of huerstic values
k = 0
for i in mazeBlocks.values():
    print(i[1], end=" ")
    k += 1
    if k == mazeSize:
        print("")
        k = 0
'''



# starting with A*

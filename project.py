import random
mazeSize = 8
mazeBlocks = {}
# create a 8x8 maze grid full of obstacles. A key-value pair will be assigned to every block of this maze.
# The key is the index of this block, and the value is a list of two values.
# The first value of the list is either 0 (obstacle) or 1 (passage). The second value is heuristic value (initially -1).
for i in range(1, mazeSize + 1):
    for j in range(1, mazeSize + 1):
        mazeBlocks[(i,j)] = [0,-1]

        
# implement DFS to create a path from top left (1,1)[satrting state] to bottom right (6,6)
        
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
# print the current 6x6 maze        
k = 0        
for i in mazeBlocks.values():
    print(i[0], end=" ")
    k += 1
    if k == mazeSize:
        print("")
        k = 0
    
# Manhattan distance as a hueristic value, Ali will do it :)



# starting with A*

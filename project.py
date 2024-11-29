
           # Husain Ali Merza - 202100358
# Mohammed Jaafar - 20217999
# Ali Sami - 202102423
import random

mazeSize = 5
mazeBlocks = {}
# create a 8x8 maze grid full of obstacles. A key-value pair will be assigned to every block of this maze.
# The key is the index of this block, and the value is a list of two values.
# The first value of the list is either 0 (obstacle) or 1 (passage). The second value is heuristic value (initially -1).
def mazeCreation():
    for i in range(1, mazeSize + 1):
        for j in range(1, mazeSize + 1):
            mazeBlocks[(i, j)] = [0, -1]

mazeCreation()

def mazeGenerator(): # Generate maze row by row
    for i in range(1, 5 + 1):
        obstacle = random.randint(1, 3)  # Random number of obstacles per row (minumum 1 and max 3)
        path = 5 - obstacle # Remaining path number per row
        while path > 0: # Creating path cells in a row
            currentRandom = random.randint(1, 5) # select a random place to set as path
            if mazeBlocks[(i, currentRandom)][0] == 0: # Ensure random place selected is not a path in the first place
                mazeBlocks[(i, currentRandom)][0] = 1 # Set as path
                path -= 1
    while True: # Select a random obstacle cell in the first row to be the initial state
        initial = random.randint(1, 5)
        if (mazeBlocks[(1, initial)][0]) == 0:
            mazeBlocks[(1, initial)][0] = "I"
            break

    while True: # Select a random obstacle cell in the last row to be the goal
        goal = random.randint(1, 5)
        if (mazeBlocks[(5, goal)][0]) == 0:
            mazeBlocks[(5, goal)][0] = "G"
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


def dfs(): # This method is used to unsure that the maze generated actually has a path from I to G
    initial = 0
    for i, j in mazeBlocks.items():  # Find I position so we can calculate heuristic later
        if mazeBlocks[i][0] == "I":
            initial = i[1]
    stack = [(1, initial)] # Create a list that contains I position first
    while stack:
        # Give me the index of the last visited node
        i, j = stack[(len(stack) - 1)][0], stack[(len(stack) - 1)][1]
        # if it is the goal, print we have a goal:
        if mazeBlocks[(i, j)][0] == "G":
            return print("Solution Exists!!")
        # mark it as visited(2 for visited)
        mazeBlocks[(i, j)][1] = 2
        # let's initialize temp to know if there is any valid neighbour
        temp = []
        # Right neighbour
        if (i, j + 1) in mazeBlocks and (mazeBlocks[(i, j + 1)][0] == 1 or mazeBlocks[(i, j + 1)][0] == "G") and \
                mazeBlocks[(i, j + 1)][1] != 2:
            temp.append((i, j + 1))
        # Left neighbour
        if (i, j - 1) in mazeBlocks and (mazeBlocks[(i, j - 1)][0] == 1 or mazeBlocks[(i, j - 1)][0] == "G") and \
                mazeBlocks[(i, j - 1)][1] != 2:
            temp.append((i, j - 1))
        # top neighbour
        if (i - 1, j) in mazeBlocks and (mazeBlocks[(i - 1, j)][0] == 1 or mazeBlocks[(i - 1, j)][0] == "G") and \
                mazeBlocks[(i - 1, j)][1] != 2:
            temp.append((i - 1, j))
        # bottom neighbour
        if (i + 1, j) in mazeBlocks and (mazeBlocks[(i + 1, j)][0] == 1 or mazeBlocks[(i + 1, j)][0] == "G") and \
                mazeBlocks[(i + 1, j)][1] != 2:
            temp.append((i + 1, j))
        # if temp has something, select the last node(or any one) and put it in the stack
        if temp:
            stack.append((temp[(len(temp) - 1)][0], temp[(len(temp) - 1)][1]))
        else:
            stack.pop()
    print("Re-Generate")
    mazeCreation()
    mazeGenerator()
    dfs()

# NOTE: This function does in fact find a solution, but it does not guarantee optimal solution, so we use A* next

dfs()
#print(dfs())
# printing the maze
k = 0
for i in mazeBlocks.values():
    print(i[0], end=" ")
    k += 1
    if k == mazeSize:
        print("")
        k = 0
print("\n")

goal = 0
for i, j in mazeBlocks.items(): # Find G position so we can calculate heuristic next
    if mazeBlocks[i][0] == "G":
        goal = i[1]


# mannhatan Distance
for i in range(1, mazeSize + 1):
    for j in range(1, mazeSize + 1):
        mazeBlocks[(i, j)][1] = abs(i - mazeSize) + abs(j - goal)
# printing the
'''
k = 0
for i in mazeBlocks.values():
    print(i[1], end=" ")
    k += 1
    if k == mazeSize:
        print("")
        k = 0
print("\n")
'''
def optimalPath(copy):
    print(copy, "Closed list")
    list = []
    list.extend(copy)
    pathlist = []
    for index in reversed(range(len(copy)-1)):
        currenti = list[index][0][0]
        nexti = list[index+1][0][0]
        currentj = list[index][0][1]
        nextj = list[index+1][0][1]
        if (abs(currenti-copy[0][0][0]) == 1 and currentj-copy[0][0][1] == 0) or (currenti-copy[0][0][0] == 0 and abs(currentj-copy[0][0][1]) == 1):
            pathlist.append(list[index+1])
            pathlist.append(list[index])
            pathlist.append(list[0])
            break
        elif (abs(nexti-currenti) == 1 and nextj-currentj == 0) or (nexti-currenti == 0 and abs(nextj-currentj) == 1):
            pathlist.append(list[index+1])
        else:
            #pathlist.append(list[index])
            del list[index]
            #index -= 1
        #print(pathlist, "path")
    #pathlist.append(list[0])
    print(pathlist, "path")



# A* Part

initial = 0
for i, j in mazeBlocks.items(): # Find I position so we can calculate in A* next
    if mazeBlocks[i][0] == "I":
        initial = i[1]

i,j = 1, initial # i and j simulates our position in the A* algorithm (the cell we are at ex.A3)

# A* Algorithm
#def aStar():
open = [] # open list
close = [((i,j), mazeBlocks[(i,j)][1])] # closed list
path = "" # This will contain the optimal path
gClosed = {(i,j): 0}
# check if (i,j) exist in open or close!
def checker(a,b,lists):
    for h in range(len(lists)):
        if a == lists[h][0][0] and b == lists[h][0][1]:
            return h
    return -1


    
# I write these two variables, to save the index of the parent of last appended node.
# [After sorting the open list and add the node from open to close, give me the parent of that node] 
 

while True:
    if mazeBlocks[(i,j)][0] == "G": # If we are at the goal position end loop
        optimalPath(close)
        print("We have reached to the goal")
        print("The path is: ?")
        break
    # Check Top neighbour
    if (i+1,j) in mazeBlocks and (mazeBlocks[(i+1,j)][0] == 1 or mazeBlocks[(i+1,j)][0] == "G") and \
            checker(i+1,j,open) == -1 and checker(i+1,j,close) == -1:
        open.append(((i+1,j), mazeBlocks[(i+1,j)][1] + gClosed[(i,j)] + 1)) #  close[checker(i,j,close)][1]+1)
    # Check Bottom neighbour
    if (i-1,j) in mazeBlocks and (mazeBlocks[(i-1,j)][0] == 1 or mazeBlocks[(i-1,j)][0] == "G") and \
                checker(i-1,j,open) == -1 and checker(i-1,j,close) == -1:
        open.append(((i-1,j), mazeBlocks[(i-1,j)][1]+ gClosed[(i,j)] + 1))
    # Check Right neighbour
    if (i,j+1) in mazeBlocks and (mazeBlocks[(i,j+1)][0] == 1 or mazeBlocks[(i,j+1)][0] == "G") and \
                checker(i,j+1,open) == -1 and checker(i,j+1,close) == -1:
        open.append(((i,j+1), mazeBlocks[(i,j+1)][1]+ gClosed[(i,j)] + 1))
    # Check Left neighbour
    if (i,j-1) in mazeBlocks and (mazeBlocks[(i,j-1)][0] == 1 or mazeBlocks[(i,j-1)][0] == "G") and \
                checker(i,j-1,open) == -1 and checker(i,j-1,close) == -1:
        open.append(((i,j-1), mazeBlocks[(i,j-1)][1] + gClosed[(i,j)] + 1))
        
        
        
    
    for c in range(len(open)): # Go through the open list to make minumum at the start
        minumum = open[0][1]
        index = 0
        i = open[0][0][0]
        j = open[0][0][1]
        if open[c][1] < minumum: # This will find the minumumimum and swap it with the start item of open list
            minumum = open[c][1]
            index = c
            current = open[0]
            open[0] = open[index]
            open[index] = current # End of swap
            position = open[0][0] # Get the new i and j for next iteration
            i = open[0][0][0] #position[0]
            j = open[0][0][1] #position[1]

    
    # before sending it to close. show me which neighbour of this node has the best g.
    tempG = []
    if (i+1,j) in gClosed:
        tempG.append(gClosed[(i+1,j)])
    if (i-1,j) in gClosed:
        tempG.append(gClosed[(i-1,j)])
    if (i,j+1) in gClosed:
        tempG.append(gClosed[(i,j+1)])
    if (i,j-1) in gClosed:
        tempG.append(gClosed[(i,j-1)])
    currentG = min(tempG)
    
    close.append(open[0]) # Add the best next state to close list
   
    # what is the g value of the parent of last visited node
    gClosed[open[0][0]] = currentG + 1
    
    
    
    #mazeBlocks[(open[0][0])][1] = 22 # Avoid infinite loops by changing the heuristic value of the visited state
    print(open, "Open list")
    del open[0] # Remove the best next state from open list
    #print(close, "Closed list")
    #optimalPath(close)

# DON'T FORGET AFTER FINISHING TO MODIFY A* TO CHECK IF YOU NEED TO UPDATE A VISITED STATE HEURISTIC
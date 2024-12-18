# ITCS440 PROJECT RANDOM MAZE 2024/2025 Semester 1

# Husain Ali Merza - 202100358 / Section 1
# Mohamed Jaafar - 202107999 / Section 1
# Ali Sami - 202102423 / Section 1
import random
mazeSize = 5
mazeBlocks = {}
pathLetter = ['A','B','C','D','E']


# create a maze grid full of obstacles. A key-value pair will be assigned to every block of this maze.
# The key is the index of this block, and the value is a list of two values.
# The first value of the list is either 0 (obstacle) or 1 (passage). The second value is heuristic value (initially -1).
def mazeCreation():
    for i in range(1, mazeSize + 1):
        for j in range(1, mazeSize + 1):
            mazeBlocks[(i, j)] = [0, -1]

# The initial creation of the maze[creating the matrix]
mazeCreation()


def mazeGenerator():  # Generate maze row by row
    for i in range(1, mazeSize + 1):
        obstacle = random.randint(1, int(mazeSize/2)+1)  # Random number of obstacles per row (minumum 1 and max almost half size)
        path = mazeSize - obstacle  # Remaining path number per row
        while path > 0:  # Creating path cells in a row
            currentRandom = random.randint(1, mazeSize)  # select a random place to set as path
            if mazeBlocks[(i, currentRandom)][0] == 0:  # Ensure random place selected is not a path in the first place
                mazeBlocks[(i, currentRandom)][0] = 1  # Set as path
                path -= 1
    while True:  # Select a random obstacle cell in the first row to be the initial state
        initial = random.randint(1, mazeSize)
        if (mazeBlocks[(1, initial)][0]) == 0:
            mazeBlocks[(1, initial)][0] = "I"
            break

    while True:  # Select a random obstacle cell in the last row to be the goal
        goal = random.randint(1, mazeSize)
        if (mazeBlocks[(mazeSize, goal)][0]) == 0:
            mazeBlocks[(mazeSize, goal)][0] = "G"
            break

# The initial generation of the maze[Filling the matrix]
mazeGenerator()



goal = 0
for i, j in mazeBlocks.items():  # Find G position so we can calculate heuristic next
    if mazeBlocks[i][0] == "G":
        goal = i[1]

# Manhattan Distance
for i in range(1, mazeSize + 1):
    for j in range(1, mazeSize + 1):
        mazeBlocks[(i, j)][1] = abs(i - mazeSize) + abs(j - goal)


def optimalPath(copy): # This finds and prints the optimal path
    #print(copy, "Closed list") # 'copy' is the closed list from A*
    list = []
    list.extend(copy) # Get a copy of 'copy'
    pathlist = [] # Will contain the optimal path to be printed
    for index in reversed(range(len(copy) - 1)): # Start checking from last cell in the closed list going backwards
        currenti = list[index][0][0]
        nexti = list[index + 1][0][0]
        currentj = list[index][0][1]
        nextj = list[index + 1][0][1]
        if (abs(nexti - copy[0][0][0]) == 1 and nextj - copy[0][0][1] == 0) or (
                nexti - copy[0][0][0] == 0 and abs(nextj - copy[0][0][1]) == 1): # Checks if the current cell is one cell away from I
            pathlist.append(list[index + 1]) 
            pathlist.append(list[0]) # append the initial cell
            break
        elif (abs(nexti - currenti) == 1 and nextj - currentj == 0) or (
                nexti - currenti == 0 and abs(nextj - currentj) == 1): # Checks what previous cell got us to the current cell
            pathlist.append(list[index + 1])
        else:
            del list[index] # Deletes cells from temporary 'list' that are not leading to path
            
        #print(list, "ITERATION", index)
    path = "" # This will contain the optimal path
    for l in reversed(range(len(pathlist))):
        path += pathLetter[pathlist[l][0][0]-1] + str(pathlist[l][0][1]) + "-"
    path = path[:-1] # Remove the last '-'
    return path






# Check if a cell (i,j) exist in open or close list and return its index
def checker(a, b, lists):
    for h in range(len(lists)):
        if a == lists[h][0][0] and b == lists[h][0][1]:
            return h
    return -1

# print the maze
def mazePrinter():
    k = 0
    p = 0
    for i in mazeBlocks.values():
        if k==0:
            print(pathLetter[p],end=" |")
            p += 1
        print("",i[0], end=" |")
        k += 1
        if k == mazeSize:
            print("")
            k = 0
    print()
    
# A* Part
def Astar():
    
    initial = 0
    for i, j in mazeBlocks.items():  # Find I position so we can calculate in A* next
        if mazeBlocks[i][0] == "I":
            initial = i[1]

    i, j = 1, initial  # i and j simulates our position in the A* algorithm (the cell we are at)


    # A* Algorithm

    open = []  # open list
    close = [((i, j), mazeBlocks[(i, j)][1])]  # closed list
    gClosed = {(i, j): 0} # This is g
    
    # [After sorting the open list and add the node from open to close, give me the parent of that node]
    while True:
        if mazeBlocks[(i, j)][0] == "G":  # If we are at the goal position end loop
            mazePrinter()
            print("The Solution Path:",optimalPath(close))
            break
        # Check Top neighbour
        if (i + 1, j) in mazeBlocks and (mazeBlocks[(i + 1, j)][0] == 1 or mazeBlocks[(i + 1, j)][0] == "G") and \
                checker(i + 1, j, open) == -1 and checker(i + 1, j, close) == -1:
            open.append(((i + 1, j), mazeBlocks[(i + 1, j)][1] + gClosed[(i, j)] + 1)) # Add above cell to open list with (h + g)
        # Check Bottom neighbour
        if (i - 1, j) in mazeBlocks and (mazeBlocks[(i - 1, j)][0] == 1 or mazeBlocks[(i - 1, j)][0] == "G") and \
                checker(i - 1, j, open) == -1 and checker(i - 1, j, close) == -1:
            open.append(((i - 1, j), mazeBlocks[(i - 1, j)][1] + gClosed[(i, j)] + 1)) # Add bellow cell to open list with (h + g)
        # Check Right neighbour
        if (i, j + 1) in mazeBlocks and (mazeBlocks[(i, j + 1)][0] == 1 or mazeBlocks[(i, j + 1)][0] == "G") and \
                checker(i, j + 1, open) == -1 and checker(i, j + 1, close) == -1:
            open.append(((i, j + 1), mazeBlocks[(i, j + 1)][1] + gClosed[(i, j)] + 1)) # Add right cell to open list with (h + g)
        # Check Left neighbour
        if (i, j - 1) in mazeBlocks and (mazeBlocks[(i, j - 1)][0] == 1 or mazeBlocks[(i, j - 1)][0] == "G") and \
                checker(i, j - 1, open) == -1 and checker(i, j - 1, close) == -1:
            open.append(((i, j - 1), mazeBlocks[(i, j - 1)][1] + gClosed[(i, j)] + 1)) # Add left cell to open list with (h + g)

        for c in range(len(open)):  # Go through the open list to make minimum at the start
            minimum = open[0][1]
            index = 0
            i = open[0][0][0]
            j = open[0][0][1]
            if open[c][1] < minimum:  # This will find the minimum and swap it with the start item of open list
                minimum = open[c][1]
                index = c
                current = open[0]
                open[0] = open[index]
                open[index] = current  # End of swap
                i = open[0][0][0]
                j = open[0][0][1]

        # Before sending it to close list. show me which neighbour of this node has the best g.
        tempG = []
        if (i + 1, j) in gClosed:
            tempG.append(gClosed[(i + 1, j)])
        if (i - 1, j) in gClosed:
            tempG.append(gClosed[(i - 1, j)])
        if (i, j + 1) in gClosed:
            tempG.append(gClosed[(i, j + 1)])
        if (i, j - 1) in gClosed:
            tempG.append(gClosed[(i, j - 1)])
        if tempG:
            currentG = min(tempG)
        try:
            close.append(open[0])  # Add the best next state/cell to close list
        except: # This will only run if no path exists
            mazeCreation()
            mazeGenerator()
            Astar()
            break
        
        # What is the g value of the parent of last visited node
        gClosed[open[0][0]] = currentG + 1

        #print(open, "Open list")
        
        del open[0]  # Remove the best next state from open list
        
# The initial execution of A* algorithm
Astar()

        
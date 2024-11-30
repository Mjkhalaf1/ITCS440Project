maze = np.full((m, n), '0')

for i in range(m):
    if i % 2 == 0:
      maze[i] = np.full(n, '0')
    else:
      for j in range(n):
        if j % 2 == 0:
          maze[i][j] = '0'
        else:
          maze[i][j] = '1'
import random

def modify(maze, m, n):
  for i in range(35):
    x = random.randint(1, n-2)
    y = random.randint(1, m-2)
    maze[x][y] = '1'
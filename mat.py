import numpy as np
from heapq import heappop, heappush

# Function to calculate the Manhattan distance (heuristic)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* algorithm to find the shortest path
def a_star(matrix, start, goal):
    rows, cols = matrix.shape
    
    if matrix[start] == 1 or matrix[goal] == 1:
        return None
    
    open_list = []
    heappush(open_list, (0 + heuristic(start, goal), 0, start))
    
    came_from = {}
    g_score = {start: 0}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while open_list:
        _, current_g, current = heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if matrix[neighbor] == 0 or matrix[neighbor] == 4:  # Allow moving to end node
                    tentative_g = current_g + 1
                    if neighbor not in g_score or tentative_g < g_score[neighbor]:
                        g_score[neighbor] = tentative_g
                        f_score = tentative_g + heuristic(neighbor, goal)
                        heappush(open_list, (f_score, tentative_g, neighbor))
                        came_from[neighbor] = current
    
    return None

# Function to find the coordinates of start (2) and goal (4) in the matrix
def find_start_and_goal(matrix):
    start, goal = None, None
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 2:
                start = (i, j)
            elif matrix[i, j] == 4:
                goal = (i, j)
    return start, goal

# Function to modify the matrix with path marked as 3
def find_path_and_modify_matrix(matrix):
    matrix = np.array(matrix)
    
    start, goal = find_start_and_goal(matrix)
    
    if start is None or goal is None:
        print("Start or Goal node not found")
        return matrix.tolist()  # Convert numpy array to list
    
    path = a_star(matrix, start, goal)
    
    if path is None:
        print("No path found")
        return matrix.tolist()  # Convert numpy array to list
    
    for (x, y) in path:
        if matrix[x, y] != 2 and matrix[x, y] != 4:  # Don't overwrite start or goal nodes
            matrix[x, y] = 3
    #print(matrix)
    return matrix.tolist()  # Convert numpy array to list
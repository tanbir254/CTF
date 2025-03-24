# Input the text as a single string
input_text = input()  # Example: "shock;979;23"

# Write your solution below and make sure to encode the word correctly
from collections import deque
import ast

def shortest_path_steps(grid, start):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(start, 0)])  # Queue holds (current_position, step_count)
    visited = set([start])  # Track visited positions

    while queue:
        (r, c), steps = queue.popleft()
        
        # If we reached 'E', return the step count
        if grid[r][c] == 'E':
            return steps

        # Explore all 4 directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check if new position is within bounds and not an obstacle (1)
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] != 1:  # Avoid obstacles
                    queue.append(((nr, nc), steps + 1))
                    visited.add((nr, nc))  # Mark as visited

    return -1  # Return -1 if no path is found

def main():
    # Read the grid input as a single line string
    input_string = input_text
    
    # Convert the string input to a grid using ast.literal_eval for safety
    try:
        grid = ast.literal_eval(input_string)
    except Exception as e:
        print("Error parsing input:", e)
        return

    # Check if 'E' exists in the grid
    found_e = False
    for row in grid:
        if 'E' in row:
            found_e = True
            break
    
    if not found_e:
        print("Target 'E' not found in the grid!")
        return
    
    # Starting position (0, 0)
    start_position = (0, 0)
    
    # Calculate the shortest number of steps to 'E'
    steps = shortest_path_steps(grid, start_position)

    if steps != -1:
        print(steps)
    else:
        print("No path found")

# Run the program
if __name__ == "__main__":
    main()

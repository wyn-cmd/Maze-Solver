# Version 1.0




def solve_maze(maze):

    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0
    

    start_row, start_col = None, None

    for r in range(rows):

        for c in range(cols):

            if maze[r][c] == 'S':
                start_row, start_col = r, c
                break

        if start_row is not None:
            break
    

    def dfs(r, c):

        maze[r][c] = '*'
        

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] in (' ', 'E'):

                if maze[nr][nc] == 'E':
                    return True
                elif maze[nr][nc] == ' ':
                    if dfs(nr, nc):
                        return True
        

        maze[r][c] = ' ' 
        
        return False
    

    dfs(start_row, start_col)
    

    maze[start_row][start_col] = '*'
    

    for row in maze:
        print(''.join(row))


def load_maze_from_file(file_path):
  """Loads a maze from a text file into a list of lists.

  Args:
    file_path: The path to the text file containing the maze.

  Returns:
    A list of lists representing the maze.
  """

  maze = []
  with open(file_path, 'r') as file:
    for line in file:
      row = line.strip().strip('"').replace('"', '').split(', ')
      maze.append(row)
  return maze

# Example usage:
file_path = "maze.txt"  # Replace with the actual file path
maze = load_maze_from_file(file_path)

print("Maze before solving:")
for row in maze:
    print(''.join(row))

print("\nMaze after solving:")
solve_maze(maze)

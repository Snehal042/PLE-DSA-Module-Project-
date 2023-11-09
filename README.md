# preplef_project-rat_in_maze
##Code
import random
def generate_maze(n):
    maze = [["▓" if random.random() < 0.3 else "◌" for _ in range(n)] for _ in range(n)]
    maze[0][0] = "S"
    maze[n - 1][n - 1] = "E"

    return maze
def print_maze(maze):
    for row in maze:
        print("".join(row))
def find_path(maze):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(maze) or y >= len(maze):
            return False
        if maze[x][y] == "E":
            return True
        if maze[x][y] == "▓" or maze[x][y] == "X":
            return False
        
        maze[x][y] = "X"
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        for dx, dy in directions:
            if dfs(x + dx, y + dy):
                return True
        
        maze[x][y] = "◌"  
        return False

    if dfs(0, 0):
        return True
    else:
        return False
def print_path(path):
    for row in path:
        print("".join(row))
def mark_path(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if path[i][j] == "X":
                maze[i][j] = "X"
def main():
    n = int(input("Enter the size of the maze: "))
    maze = generate_maze(n)
    path = [[" " for _ in range(n)] for _ in range(n)]
    if find_path(maze):
        print("Path found!")
        mark_path(maze, path)
    else:
        print("No path found!")
    print("Maze:")
    print_maze(maze)
    print("Path:")
    print_path(path)

if __name__ == "__main__":
    main()
#Screenshot

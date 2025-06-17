def check_next(matrix, position):
    positions = []
    if matrix[position[0] - 1][position[1]] == " ":

        positions.append((position[0] - 1, position[1]))
    if matrix[position[0]][position[1] - 1] == " ":

        positions.append((position[0], position[1] - 1))
    if matrix[position[0]][position[1] + 1] == " ":

        positions.append((position[0], position[1] + 1))
    if matrix[position[0] + 1][position[1]] == " ":

        positions.append((position[0] + 1, position[1]))
    return positions


rows = int(input())
maze = []
k_position = ()
position = ()

for i in range(rows):
    row = [char for char in input()]
    maze.append(row)
    if "k" in row:
        k_position = (i, row.index("k"))

current_moves = 1
new_moves = 0
position = k_position
current_maze = maze[:]
while True:
    ways = len(check_next(maze, position))
    if ways > 1:
        new_moves = current_moves

    if current_maze[position[0] - 1][position[1]] == " ":
        current_maze[position[0] - 1][position[1]] = "."
        position = (position[0] - 1, position[1])
    elif current_maze[position[0]][position[1] - 1] == " ":
        current_maze[position[0]][position[1] - 1] = "."
        position = (position[0], position[1] - 1)
    elif current_maze[position[0]][position[1] + 1] == " ":
        current_maze[position[0]][position[1] + 1] = "."
        position = (position[0], position[1] + 1)
    elif current_maze[position[0] + 1][position[1]] == " ":
        current_maze[position[0] + 1][position[1]] = "."
        position = (position[0] + 1, position[1])
    else:
        print("Kate cannot get out")
        break

    current_moves += 1

    if any(map(lambda x: x[0] == "." or x[-1] == ".", current_maze[1:len(current_maze) - 1])) or "." in current_maze[0] or "." in current_maze[-1]:
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if maze[row][col] == " ":
                    new_moves += 1

        print(f"Kate got out in {max(new_moves, current_moves)} moves")
        break


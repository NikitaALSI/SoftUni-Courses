rows = int(input())
maze = []
start_row = 0
start_col = 0

for i in range(rows):
    row = list(input())
    maze.append(row)
    if "k" in row:
        start_row = i
        start_col = row.index("k")

cols = len(maze[0])

queue = [[start_row, start_col, 0]]
visited = [[False for _ in range(cols)] for _ in range(rows)]
visited[start_row][start_col] = True

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

max_moves = 0
found_exit = False

while len(queue) > 0:
    current = queue.pop(0)
    row = current[0]
    col = current[1]
    steps = current[2]

    if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
        found_exit = True
        if steps > max_moves:
            max_moves = steps

    for d in directions:
        new_row = row + d[0]
        new_col = col + d[1]

        if 0 <= new_row < rows and 0 <= new_col < cols:
            if maze[new_row][new_col] == " " and not visited[new_row][new_col]:
                visited[new_row][new_col] = True
                queue.append([new_row, new_col, steps + 1])

if found_exit:
    print(f"Kate got out in {max_moves + 1} moves")
else:
    print("Kate cannot get out")

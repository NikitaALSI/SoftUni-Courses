def check_next(matrix, position):
    positions = []
    if matrix[position[0] - 1][position[1]] == " ":
        matrix[position[0] - 1][position[1]] = "."
        positions.append((position[0] - 1, position[1]))
    if matrix[position[0]][position[1] - 1] == " ":
        matrix[position[0]][position[1] - 1] = "."
        positions.append((position[0], position[1] - 1))
    if matrix[position[0]][position[1] + 1] == " ":
        matrix[position[0]][position[1] + 1] = "."
        positions.append((position[0], position[1] + 1))
    if matrix[position[0] + 1][position[1]] == " ":
        matrix[position[0] + 1][position[1]] = "."
        positions.append((position[0] + 1, position[1]))
    return positions


rows = int(input())
maze = []
k_position = ()

for i in range(rows):
    row = [char for char in input()]
    maze.append(row)
    if "k" in row:
        k_position = (i, row.index("k"))


moves = [k_position]
index = 0
way_out = False
steps_for_out = []
while True:
    position = 0
    if len(moves) > 1:
        position = moves[index][-1]
    else:
        position = moves[-1]

    if position[0] == 0 or position[0] == len(maze) or position[1] == 0 or position[1] == len(maze[0]):
        way_out = True
        index += 1
        continue
    current_moves = check_next(maze, moves[index])
    if not current_moves:
        moves[index].append(["no"])
        index += 1
    moves = [moves.append(moves) for moves in range(len(current_moves))]
    for z in range(len(current_moves)):
        moves[z] += current_moves[z]

if way_out:
    print(f"Kate got out in {max(moves)} moves")
else:
    print("Kate cannot get out")


6
# #####
#  ####
## k###
### ###
### ###
### ###

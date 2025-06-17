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
break_steps = 0
other = []
steps_for_win = []
no_way_out = False
while True:
    position = moves[-1]
    if position[0] == 0 or position[0] == len(maze)-1 or position[1] == 0 or position[1] == len(maze[0])-1:
        if other:
            steps_for_win.append(len(moves) + break_steps)
            moves = other[0]
            other.pop(0)
            continue
        else:
            steps_for_win.append(break_steps + len(moves))
            break
    current_moves = check_next(maze, moves[-1])
    if not current_moves:
        if not other:
            no_way_out = True
            break
        moves = other[0]
        other.pop(0)
        continue
    if len(current_moves) > 1:
        moves.append(current_moves[0])
        other.append(current_moves[1::])
        break_steps = len(moves)
    else:
        moves.append(current_moves[0])


if steps_for_win:
    print(f"Kate got out in {max(steps_for_win)} moves")
else:
    print("Kate cannot get out")


6
# #####
#  ####
## k
##  ###
### ###
#######

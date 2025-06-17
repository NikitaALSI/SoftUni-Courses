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
        k_position = [(i, row.index("k"))]


moves = [0]
moves.append(k_position)

print(moves[-1])
while True:
    for i in moves[-1]:
        if len(moves[-1]) > 1:
            for pos in i:
                current_moves = check_next(maze, pos)
                moves.append(current_moves)
        else:
            current_moves = check_next(maze, i)
            moves.append(current_moves)

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

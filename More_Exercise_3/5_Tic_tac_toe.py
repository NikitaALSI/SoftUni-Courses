board = [input().split(" ") for _ in range(3)]
winner = ''
draw = False
for index in range(3):
    if index == 0:
        if ((board[index][index] == board[index][index + 1] == board[index][index + 2]
                or board[index][index] == board[index + 1][index + 1] == board[index + 2][index + 2]
                or board[index][index] == board[index + 1][index] == board[index + 2][index])
                and board[index][index] != "0"):
            winner = board[index][index]
            break
    elif index == 1:
        if ((board[index - 1][index] == board[index][index] == board[index + 1][index]
                or board[index][index - 1] == board[index][index] == board[index][index + 1])
                and board[index][index] != "0"):
            winner = board[index][index]
            break
    elif index == 2:
        if ((board[index - 2][index] == board[index - 1][index] == board[index][index]
                or board[index][index - 2] == board[index][index - 1] == board[index][index])
                and board[index][index] != "0"):
            winner = board[index][index]
            break
        elif board[index - 2][index] == board[index - 1][index - 1] == board[index][index - 2] and board[index][index] != "0":
            winner = board[index - 2][index]
            break
else:
    draw = True

if not draw:
    if winner == "1":
        print("First player won")
    elif winner == "2":
        print("Second player won")
else:
    print("Draw!")

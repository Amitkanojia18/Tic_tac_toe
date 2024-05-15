from random import randrange


def display_board(board, turn):
    print(f'''+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+''')

    if (len(make_list_of_free_fields(board)) == 0):
        print("draw")

    elif turn == 0:
        enter_move(board)

    elif turn == 1:
        draw_move(board)

    elif turn == 3:
        print("You Won")
    elif turn == 4:
        print("cpu Won")


def enter_move(board):
    move = int(input("Enter your move: "))

    if (1 <= move <= 9) and move in make_list_of_free_fields(board):
        i, j = figure_index(move)

        board[i][j] = "O"

        victory_for(board, "O")

        if (victory_for(board, "O") == True):
            display_board(board, 3)

        else:
            display_board(board, 1)


    else:
        print("invalid input")
        enter_move(board)


def figure_index(move):
    if (1 <= move <= 3):
        bound = 1
    elif (4 <= move <= 6):
        bound = 2
    else:
        bound = 3

    match bound:
        case 1:
            i = 0
            j = move - 1
        case 2:
            i = 1
            j = move - 4
        case 3:
            i = 2
            j = move - 7

    return i, j


def make_list_of_free_fields(board):
    free_field = []

    for i in range(3):
        for j in range(3):

            if (board[i][j] != "O" and board[i][j] != "X"):
                free_field.append(board[i][j])

    return free_field


def victory_for(board, sign):
    Win = False
    horizontal = []
    vertical = []
    diagonal1 = []
    diagonal2 = []

    for i in range(3):
        horizontal = []
        vertical = []
        diagonal1 = []
        diagonal2 = []

        for j in range(3):
            if (sign == board[i][j]):
                horizontal.append(1)

            if (sign == board[j][i]):
                vertical.append(0)

            if (sign == board[j][j]):
                diagonal1.append(2)

            if (sign == board[j][2 - j]):
                diagonal2.append(3)

        if ((len(horizontal) == 3) or (len(vertical) == 3)):
            Win = True
            return Win

        elif (len(diagonal1) == 3) or (len(diagonal2) == 3):
            Win = True
            return Win

        # else:
        #     return Win

    else:
        return Win


def draw_move(board):
    cpu = randrange(1, 10)

    if cpu in make_list_of_free_fields(board):
        i, j = figure_index(cpu)
        board[i][j] = "X"

        victory_for(board, "X")

        if (victory_for(board, "X") == True):
            display_board(board, 4)

        else:
            display_board(board, 0)

    else:
        draw_move(board)


moveList = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

display_board(moveList, 0)



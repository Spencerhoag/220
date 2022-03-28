"""
Name: <Spencer Hoag>
<lab9>.py
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if board[position] == "x" or board[position] == "o" and 0 >= position >= 8:
        return False


def fill_spot(board, position, character):
    character = character.strip().lower()
    board[position - 1] = character


def winning_game(board):
    row1 = board[0:2]
    row2 = board[3:5]
    row3 = board[6:8]
    col1 = board[0:9:3]
    col2 = board[1:9:3]
    col3 = board[2:9:3]
    diag1 = board[0:9:4]
    diag2 = board[2:8:2]
    if row1[0] == row1[1] == row1[2]:
        return True
    elif row2[0] == row2[1] == row2[2]:
        return True
    elif row3[0] == row3[1] == row3[2]:
        return True
    elif col1[0] == col1[1] == col1[2]:
        return True
    elif col2[0] == col2[1] == col2[2]:
        return True
    elif col3[0] == col3[1] == col3[2]:
        return True
    elif diag1[0] == diag1[1] == diag1[2]:
        return True
    elif diag2[0] == diag2[1] == diag2[2]:
        return True
    else:
        return False


def game_over(board):
    tie = True
    for i in range(9):
        if board[i] != "x" or board[i] != "o":
            tie = False
    return winning_game(board) or tie


def get_winner(board):
    if winning_game(board):
        xcount = 0
        ocount = 0
        for position in board:
            if position == "x":
                xcount = xcount + 1
            elif position == "o":
                ocount = ocount + 1
        if xcount == ocount:
            return "o"
        else:
            return "x"
    else:
        return None


def play(board):
    xturn = 0
    oturn = 0
    while not game_over(board):
        print_board(board)
        if xturn == oturn:
            position = int(input("It's x's turn, enter position: "))
            if is_legal(board, position):
                fill_spot(board, position, "x")
                xturn = xturn + 1
        else:
            position = int(input("It's o's turn, enter position: "))
            if is_legal(board, position):
                fill_spot(board, position, "o")
                oturn = oturn + 1
    if winning_game(board):
        print(get_winner(board))
    else:
        print("Tie")
    msg = input("Do you want to play again? ")
    if msg[0] == "y":
        new_game = build_board()
        play(new_game)


if __name__ == '__main__':
    board1 = build_board()
    play(board1)

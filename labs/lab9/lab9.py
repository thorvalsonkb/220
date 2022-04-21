"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def build_board():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return numbers


def print_board(board):
    """ prints the values of baord """
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
    if board[position] != 'x' or 'o':
        return True
    else:
        return False


def fill_spot(board, position, character):
    character.strip().lowercase()
    board[position] = character


def winning_game(board):
    # row 1
    if board[0] == 'x':
        if board[1] == 'x':
            if board[2] == 'x':
                return True
    elif board[0] == 'o':
        if board[1] == 'o':
            if board[2] == 'o':
                return True
    # row 2
    elif board[3] == 'x':
        if board[4] == 'x':
            if board[5] == 'x':
                return True
    elif board[3] == 'o':
        if board[4] == 'o':
            if board[5] == 'o':
                return True
    # row 3
    elif board[6] == 'x':
        if board[7] == 'x':
            if board[8] == 'x':
                return True
    elif board[6] == 'o':
        if board[7] == 'o':
            if board[8] == 'o':
                return True
    # diagonal 1
    elif board[0] == 'x':
        if board[4] == 'x':
            if board[8] == 'x':
                return True
    elif board[0] == 'x':
        if board[4] == 'x':
            if board[8] == 'x':
                return True
    # diagonal 2
    elif board[2] == 'x':
        if board[4] == 'x':
            if board[6] == 'x':
                return True
    elif board[2] == 'o':
        if board[4] == 'o':
            if board[6] == 'o':
                return True
    else:
        return False


def game_over(board):
    for i in range(len(board)):
        if board.count(i) < 1:
            return False
        else:
            return True


def get_winner(board):
    # row 1
    if board[0] == 'x':
        if board[1] == 'x':
            if board[2] == 'x':
                return 'x'
    elif board[0] == 'o':
        if board[1] == 'o':
            if board[2] == 'o':
                return 'o'
    # row 2
    elif board[3] == 'x':
        if board[4] == 'x':
            if board[5] == 'x':
                return 'x'
    elif board[3] == 'o':
        if board[4] == 'o':
            if board[5] == 'o':
                return 'o'
    # row 3
    elif board[6] == 'x':
        if board[7] == 'x':
            if board[8] == 'x':
                return 'x'
    elif board[6] == 'o':
        if board[7] == 'o':
            if board[8] == 'o':
                return 'o'
    # diagonal 1
    elif board[0] == 'x':
        if board[4] == 'x':
            if board[8] == 'x':
                return 'x'
    elif board[0] == 'o':
        if board[4] == 'o':
            if board[8] == 'o':
                return 'o'
    # diagonal 2
    elif board[2] == 'x':
        if board[4] == 'x':
            if board[6] == 'x':
                return 'x'
    elif board[2] == 'o':
        if board[4] == 'o':
            if board[6] == 'o':
                return 'o'
    else:
        return None


def play(board):
    while game_over(board) is False:
        return True
    if get_winner(board) == 'x':
        print("x's win!")
        user_input = input('would you like to play again?')
        if user_input[0] == 'y':
            return True
        return False
    elif get_winner(board) == 'o':
        print("o's win!")
        user_input = input('would you like to play again?')
        if user_input[0] == 'y':
            return True
        return False
    else:
        print('tie')
        user_input = input('would you like to play again?')
        if user_input[0] == 'y':
            return True
        return False


def main():
    pass


if __name__ == '__main__':
    main()

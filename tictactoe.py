print("Welcome to Tic-Tac-Toe!")

#initializing board
board = [
    ' ',' ',' ',
    ' ',' ',' ',
    ' ',' ',' '
]


def board_full_check(board):
    for cell in board:
        if cell == ' ':
            return True
    return False


def win_state_check(board):
    winstates = [  # list of winning combinations
        {0, 1, 2}, # sets used because unordered
        {3, 4, 5},
        {6, 7, 8},
        {0, 3, 6},
        {1, 4, 7},
        {2, 5, 8},
        {0, 4, 8},
        {2, 4, 6}
    ]
    win_set = []
    win_state = ' '
    for cell_set in winstates:
        win_set = []
        win_set = [board[cell_index] for cell_index in cell_set]
        if all(ele == win_set[0] for ele in win_set):
            win_state = win_set[0]
            break
    return win_state


def is_empty(index, board):
    if board[index] != ' ':
        return False
    else:
        return True


def print_board(board):
    print("/---|---|---\\")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("|-----------|")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("|-----------|")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("/---|---|---\\")


# driver code
# game cycle runs on while loop
print_board(board)
while board_full_check(board) and win_state_check(board) == ' ':

    print('Player 1\'s turn.')
    while True:
        try:
            player1_input = int(input('Which cell do you want to play? '))
            if player1_input < 1 or player1_input > 9:
                print('Please enter a cell between 1-9.')
            elif not is_empty(player1_input - 1, board):
                print('That space is taken, please enter another space.')
            else:
                board[player1_input - 1] = 'X'
                break
        except ValueError:
            print('Please enter a number.')
    print_board(board)

    if board_full_check(board) and win_state_check(board) == ' ':
        print('Player 2\'s turn.')
        while True:
            try:
                player2_input = int(input('Which cell do you want to play? '))
                if player2_input < 1 or player2_input > 9:
                    print('Please enter a cell between 1 and 9.')
                elif not is_empty(player2_input - 1, board):
                    print('That space is taken, please enter another space.')
                else:
                    board[player2_input - 1] = 'O'
                    break
            except ValueError:
                print('Please enter a number.')
        print_board(board)

# once board is full or there is a winning combination, exits the loop
print('Game over.')
if win_state_check(board) == 'X':
    print('Player 1 wins!')
elif win_state_check(board) == 'O':
    print('Player 2 wins!')
else:
    print('It\'s a draw.')
print('Thank you for playing!')

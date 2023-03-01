from copy import deepcopy

def initial_state():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

def result(board, move):
    result = deepcopy(board)
    result[move[0]][move[1]] = player(board)
    return result

def player(board):
    return "X" if (
        board[0].count("X") + board[1].count("X") + board[2].count("X")
        == board[0].count("O") + board[1].count("O") + board[2].count("O")
    ) else "O"

def winner(board):
    for i in board + [[board[j][i] for j in range(len(board))] for i in range(len(board))]:
        if i.count("X") == 3:
            return "X"
        if i.count("O") == 3:
            return "O"

        if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
            return board[1][1]

def terminal(board):
    if winner(board) is not None or board[0].count(None) + board[1].count(None) + board[2].count(None) == 0:
        return True
    else:
        return False
    

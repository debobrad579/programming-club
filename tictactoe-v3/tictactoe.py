from copy import deepcopy

X, O, EMPTY = "X", "O", None

def initial_state():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]


def result(board, action):
    result = deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    for i in board + [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]:
        if i.count(X) == 3: return X
        if i.count(O) == 3: return O

    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]: return board[1][1]


def terminal(board):
    return (
        board[0].count(EMPTY) + board[1].count(EMPTY) + board[2].count(EMPTY) == 0 
        or winner(board) != None
    )


def player(board):
    return X if (
        board[0].count(X) + board[1].count(X) + board[2].count(X) 
        == board[0].count(O) + board[1].count(O) + board[2].count(O)
    ) else O
  

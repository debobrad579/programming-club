import tictactoe as ttt
from random import choice

def actions(board):
    legal_actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == ttt.EMPTY:
                legal_actions.add((i, j))

    return legal_actions


def utility(board):
    if ttt.winner(board) == ttt.X:
        return 1
    elif ttt.winner(board) == ttt.O:
        return -1
    return 0


def min_value(board):
    if ttt.terminal(board):
        return utility(board), None

    v = 2
    optimal_action = None

    for action in actions(board):
        maximum = max_value(ttt.result(board, action))[0]

        if maximum < v:
            optimal_action = action
            v = maximum

        if v < 0:
            return v, optimal_action

    return v, optimal_action


def max_value(board):
    if ttt.terminal(board):
        return utility(board), None

    v = -2
    optimal_action = None

    for action in actions(board):
        minimum = min_value(ttt.result(board, action))[0]

        if minimum > v:
            optimal_action = action
            v = minimum

        if v > 0:
            return v, optimal_action

    return v, optimal_action


def minimax(board):
    if board == ttt.initial_state():
        return choice(((0, 0), (0, 2), (2, 0), (2, 2), (1, 1)))
    if ttt.player(board) == ttt.X:
        return max_value(board)[1]
    elif ttt.player(board) == ttt.O:
        return min_value(board)[1]

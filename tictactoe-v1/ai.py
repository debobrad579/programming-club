import tictactoe as ttt
from random import choice, sample


def utility(board):
    game_winner = ttt.winner(board)
    return 1 if game_winner == ttt.X else -1 if game_winner == ttt.O else 0


def actions(board):
    moves = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == ttt.EMPTY:
                moves.add((i, j))

    return moves


def minimax(board):
    if ttt.terminal(board):
        return None

    if board == ttt.initial_state():
        return choice([(1, 1), (0, 0), (0, 2), (2, 0), (2, 2)])

    if ttt.player(board) == ttt.X:
        return max_value(board)[1]
    
    return min_value(board)[1]


def min_value(board):
    if ttt.terminal(board):
        return utility(board), None
    
    v = 2
    optimal_action = None
    possible_actions = actions(board)

    for action in sample(possible_actions, len(possible_actions)):
        maximum = max_value(ttt.result(board, action))[0]

        if maximum < v:
            optimal_action = action
        
        v = min(v, maximum)

        if v < 0:
            return v, optimal_action
    
    return v, optimal_action


def max_value(board):
    if ttt.terminal(board):
        return utility(board), None
    
    v = -2
    optimal_action = None
    possible_actions = actions(board)

    for action in sample(possible_actions, len(possible_actions)):
        minimum = min_value(ttt.result(board, action))[0]

        if minimum > v:
            optimal_action = action
        
        v = max(v, minimum)

        if v > 0:
            return v, optimal_action
    
    return v, optimal_action

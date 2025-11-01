"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_o = sum(row.count(X) for row in board)
    count_x = sum(row.count(O) for row in board)

    return X if count_x == count_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                 actions.add((i,j))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a valid action")
    board_copy = copy.deepcopy(board)
    p = player(board)
    i,j = action
    board_copy[i][j] = p
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows for a winner
    for row in board:
        if row[0] is not None and len(set(row)) == 1:
            return row[0]

    # Check columns for a winner
    for j in range(len(board)):
        col = [board[i][j] for i in range(len(board))]
        if col[0] is not None and len(set(col)) == 1:
            return col[0]

    # Check diagonals for a winner
    diag1 = [board[i][i] for i in range(len(board))]
    diag2 = [board[i][len(board) - 1 - i] for i in range(len(board))]
    if diag1[0] is not None and len(set(diag1)) == 1:
        return diag1[0]
    if diag2[0] is not None and len(set(diag2)) == 1:
        return diag2[0]

    # Return None if no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    w = winner(board)
    return w is not None or all(EMPTY not in row for row in board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    w = winner(board)
    if w == X:
          return 1
    elif w == O:
          return -1
    return 0

def max_value(state):
    if terminal(state):
        return utility(state)
    v = float("-inf")
    for action in actions(state):
        v = max(v, min_value(result(state, action)))
    return v

def min_value(state):
    if terminal(state):
        return utility(state)
    v = float("inf")
    for action in actions(state):
        v = min(v, max_value(result(state, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)
    if terminal(board):
        return None
    else:
        if p == X:
            best_value = float("-inf")
            best_move = None
            for action in actions(board):
                move_value = min_value(result(board, action))
                if move_value > best_value:
                    best_value = move_value
                    best_move = action
            return best_move
        if p == O:
            best_value = float("inf")
            best_move = None
            for action in actions(board):
                move_value = max_value(result(board, action))
                if move_value < best_value:
                    best_value = move_value
                    best_move = action
            return best_move




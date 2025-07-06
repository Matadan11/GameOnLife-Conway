import numpy as np
from numba import njit

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
        if initial_state is not None:
            self.board = np.array(initial_state, dtype=np.uint8)
        else:
            self.board = np.random.choice([0, 1], size=(rows, cols)).astype(np.uint8)

    def step(self):
        self.board = step_numba(self.board, self.rows, self.cols)

    def get_state(self):
        return self.board.copy()

@njit
def count_live_neighbors_numba(board, row, col, rows, cols):
    total = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i == row and j == col):
                continue
            if 0 <= i < rows and 0 <= j < cols:
                total += board[i, j]
    return total

@njit
def step_numba(board, rows, cols):
    new_board = board.copy()
    for row in range(rows):
        for col in range(cols):
            total = count_live_neighbors_numba(board, row, col, rows, cols)
            if board[row, col] == 1:
                if total < 2 or total > 3:
                    new_board[row, col] = 0
            elif total == 3:
                new_board[row, col] = 1
    return new_board
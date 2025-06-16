import numpy as np
# TODO: REVISAR LOGICA DE VECINOS

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
        if initial_state is not None:
            self.board = np.array(initial_state)
        else:
            self.board = np.random.choice([0, 1], size=(rows, cols))

    def step(self):
        new_board = np.zeros((self.rows, self.cols), dtype=int)
        for row in range(self.rows):
            for col in range(self.cols):
                # Extrae una submatriz de 3x3 centrada en (row, col)
                total = int(np.sum(self.board[max(row-1, 0):min(row+2, self.rows),
                                              max(col-1, 0):min(col+2, self.cols)]))
                total -= self.board[row, col]  # Quita la celda central

                if self.board[row, col] == 1:
                    if total == 2 or total == 3:
                        new_board[row, col] = 1
                else:
                    if total == 3:
                        new_board[row, col] = 1
        self.board = new_board

    def run(self, steps):
        for _ in range(steps):
            self.step()

    def get_state(self):
        return self.board

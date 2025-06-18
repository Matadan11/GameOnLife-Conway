
import numpy as np

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        """
        Inicializa el juego con una rejilla de tamaño rows x cols.
        Si no se proporciona estado inicial, se genera aleatoriamente.
        """
        self.rows = rows
        self.cols = cols
        if initial_state is not None:
            self.board = np.array(initial_state)
        else:
            self.board = np.random.choice([0, 1], size=(rows, cols))

    def step(self):
        """
        Aplica una generación del Juego de la Vida, actualizando el estado del tablero.
        """
        new_board = np.copy(self.board)
        for row in range(self.rows):
            for col in range(self.cols):
                total_vivos = self.count_live_neighbors(row, col)
                if self.board[row, col] == 1:
                    if total_vivos < 2 or total_vivos > 3:
                        new_board[row, col] = 0
                elif self.board[row, col] == 0:
                    if total_vivos == 3:
                        new_board[row, col] = 1
        self.board = new_board

    def count_live_neighbors(self, row, col):
        """
        Cuenta los vecinos vivos alrededor de una celda.
        """
        total = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i == row and j == col):
                    continue
                if 0 <= i < self.rows and 0 <= j < self.cols:
                    total += self.board[i, j]
        return total

    def run(self, steps=1):
        """
        Ejecuta múltiples generaciones del juego.
        """
        for _ in range(steps):
            self.step()

    def get_state(self):
        """
        Devuelve el estado actual del tablero.
        """
        return self.board

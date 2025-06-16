import matplotlib
import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np
# import numba as np
# from numba import jit, prange

class GameOfLife:

    def __init__(self, game):
        self.game = game
      
    def start(self):
        print("Starting main game...")
        # Additional game logic goes here
        
    def get_neighbors(self, row, col):
        """Get the number of live neighbors for a cell at (row, col)."""
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0):
                    continue
                r, c = row + i, col + j
                if (0 <= r < self.game.rows) and (0 <= c < self.game.cols):
                    neighbors += self.game.grid[r][c]
        return neighbors
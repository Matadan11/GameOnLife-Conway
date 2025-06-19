
import numpy as np
import matplotlib.pyplot as plt
from numba import njit
import time

@njit
def count_live_neighbors(board, row, col, rows, cols):
    total = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i == row and j == col):
                continue
            if 0 <= i < rows and 0 <= j < cols:
                total += board[i, j]
    return total

@njit
def step(board, rows, cols):
    new_board = board.copy()
    for row in range(rows):
        for col in range(cols):
            total = count_live_neighbors(board, row, col, rows, cols)
            if board[row, col] == 1:
                if total < 2 or total > 3:
                    new_board[row, col] = 0
            else:
                if total == 3:
                    new_board[row, col] = 1
    return new_board

def measure_performance(sizes, iterations=10):
    times = []
    for size in sizes:
        board = np.random.choice([0, 1], size=(size, size)).astype(np.uint8)
        # "Warm-up" call to compile Numba functions
        board = step(board, size, size)

        start = time.time()
        for _ in range(iterations):
            board = step(board, size, size)
        end = time.time()
        avg_time = (end - start) / iterations
        times.append(avg_time)
        print(f"Tamaño {size}x{size}: {avg_time:.6f} segundos por iteración")
    return times

def plot_performance(sizes, times):
    cells = [s * s for s in sizes]

    plt.figure()
    plt.plot(cells, times, marker='o', label='Tiempo Empírico')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Número de celdas (log)')
    plt.ylabel('Tiempo por iteración (segundos, log)')
    plt.title('Rendimiento del Juego de la Vida (log-log)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('loglog_plot.png')
    plt.show()

if __name__ == "__main__":
    sizes = [32, 64, 128, 256, 512]
    times = measure_performance(sizes)
    plot_performance(sizes, times)

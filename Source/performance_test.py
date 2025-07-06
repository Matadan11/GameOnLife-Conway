import numpy as np
import matplotlib.pyplot as plt
import time
import cProfile
import pstats
from GameOfLife import GameOfLife, step_numba

def step_python(board, rows, cols):
    new_board = board.copy()
    for row in range(rows):
        for col in range(cols):
            total = 0
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if (i == row and j == col):
                        continue
                    if 0 <= i < rows and 0 <= j < cols:
                        total += board[i, j]
            if board[row, col] == 1:
                if total < 2 or total > 3:
                    new_board[row, col] = 0
            elif total == 3:
                new_board[row, col] = 1
    return new_board

def measure_performance(sizes, iterations=10):
    times_python = []
    times_numba = []
    for size in sizes:
        board = np.random.choice([0, 1], size=(size, size)).astype(np.uint8)
        # Python puro
        start = time.time()
        for _ in range(iterations):
            board = step_python(board, size, size)
        elapsed_python = time.time() - start
        times_python.append(elapsed_python)
        
        board = np.random.choice([0, 1], size=(size, size)).astype(np.uint8)
        # Numba optimizado
        start = time.time()
        for _ in range(iterations):
            board = step_numba(board, size, size)
        elapsed_numba = time.time() - start
        times_numba.append(elapsed_numba)
        
        print(f"Tamaño: {size}x{size} | Python: {elapsed_python:.4f}s | Numba: {elapsed_numba:.4f}s")
    
    # Guardar gráfica de comparación
    plt.plot(sizes, times_python, label='Python puro', marker='o')
    plt.plot(sizes, times_numba, label='Numba optimizado', marker='s')
    plt.xlabel("Tamaño del tablero")
    plt.ylabel("Tiempo total (s)")
    plt.title("Comparación de rendimiento Juego de la Vida")
    plt.legend()
    plt.savefig("performance_plot.png")
    print("Gráfica guardada como 'performance_plot.png'")

def generate_profile():
    profiler = cProfile.Profile()
    profiler.enable()
    sizes = [50, 100, 200, 400]
    measure_performance(sizes)
    profiler.disable()
    profiler.dump_stats("Perfilado.prof")
    with open("Perfilado.txt", "w") as f:
        ps = pstats.Stats(profiler, stream=f)
        ps.sort_stats("cumulative")
        ps.print_stats()
    print("Perfilado guardado como 'Perfilado.txt' y 'Perfilado.prof'")

if __name__ == "__main__":
    generate_profile()
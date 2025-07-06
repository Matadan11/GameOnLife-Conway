import matplotlib.pyplot as plt
from GameOfLife import GameOfLife
import numpy as np
import time

def run_game():
    rows, cols = 20, 20
    init_state = np.zeros((rows, cols), dtype=np.uint8)
    init_state[5:15, 5:15] = 1
    steps = 10
    
    game = GameOfLife(rows, cols, initial_state=init_state)

    start_time = time.time()
    for _ in range(steps):
        game.step()
    elapsed_time = time.time() - start_time

    final_state = game.get_state()
    density = np.sum(final_state) / (rows * cols)
    print("Estado final tras 10 generaciones:")
    print(final_state)
    print(f"Densidad: {density:.3f}")
    print(f"Tiempo de ejecución: {elapsed_time:.6f} segundos")

    plt.imshow(final_state, cmap='binary')
    plt.title("Generación 10")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    run_game()
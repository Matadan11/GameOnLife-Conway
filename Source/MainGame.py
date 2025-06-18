
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from GameOfLife import GameOfLife

def animate_game(rows=32, cols=32, steps=100, interval=200):
    game = GameOfLife(rows, cols)
    fig, ax = plt.subplots()
    img = ax.imshow(game.get_state(), cmap='binary')
    def update(frame):
        game.step()
        img.set_data(game.get_state())
        return [img]
    ani = animation.FuncAnimation(fig, update, frames=steps, interval=interval, blit=True)
    plt.title("Juego de la Vida de Conway")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    animate_game()

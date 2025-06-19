import matplotlib.pyplot as plt
import matplotlib.animation as animation
from GameOfLife import GameOfLife

def animate_game(rows=32, cols=32, steps=100, interval=200, save_gif=False, gif_filename="conway.gif"):
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
    if save_gif:    
        ani.save(gif_filename, writer='pillow')
        print(f"Animación guardada como {gif_filename}")
    plt.show()

if __name__ == "__main__":
    # Cambia save_gif a True si quieres guardar el gif
    animate_game(save_gif=True)

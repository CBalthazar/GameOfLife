from tkinter import Tk

from game_of_life import GameOfLife


if __name__ == "__main__":  # Sert d'executable 
    game_of_life = GameOfLife(1200, 600, 10)
    game_of_life.title("The Game of Life")
    game_of_life.create_grid()
    game_of_life.create_ui()
    game_of_life.mainloop()

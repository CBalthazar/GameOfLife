from tkinter import Canvas, Button, Tk, TOP, LEFT


class GameOfLife(Tk):
    def __init__(self, width, height, cell_size) -> None:
        Tk.__init__(self)
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._canvas = Canvas(self, background='white', width=width, height=height)

    def change_state_cell(self, event):
        self._canvas.itemconfigure(self._canvas.find_closest(event.x, event.y), fill="black")
        print(self.get_number_of_neighbours(self._canvas.find_closest(event.x, event.y)))

    def create_grid(self):
        for pos_y in range(0, self._height, self._cell_size):
            for pos_x in range(0, self._width, self._cell_size):
                self._canvas.create_rectangle(
                    pos_x,
                    pos_y,
                    pos_x + self._cell_size,
                    pos_y + self._cell_size,
                    fill="white"
                )

        self._canvas.pack(side=LEFT)
        self._canvas.bind("<Button-1>", self.change_state_cell)

    def create_ui(self):
        button_start = Button(self, text="Start", command=self.start)
        button_start.pack(side=TOP)
        button_quit = Button(self, text="Quit", command=self.quit)
        button_quit.pack()
        button_clear = Button(self, text="Clear", command=self.clear_canvas)
        button_clear.pack()


    def clear_canvas(self):
        for cell in self._canvas.find_all():
            self._canvas.itemconfigure(cell, fill="white")
        
    def get_cell_neighbours_id(self, cell_id):
        coords = self._canvas.coords(cell_id)
        cell_id_west = self._canvas.find_closest(
            (self._width+coords[0]-self._cell_size)%self._width, coords[1]
        )
        cell_id_north_west = self._canvas.find_closest(
            (self._width+coords[0]-self._cell_size)%self._width,
            (self._height+coords[1]-self._cell_size)%self._height
        )
        cell_id_north = self._canvas.find_closest(
            coords[0],
            (self._height+coords[1]-self._cell_size)%self._height
        )
        cell_id_north_east = self._canvas.find_closest(
            (self._width+coords[0]+self._cell_size)%self._width,
            (self._height+coords[1]-self._cell_size)%self._height
        )
        cell_id_east = self._canvas.find_closest(
            (self._width+coords[0]+self._cell_size)%self._width, coords[1]
        )
        cell_id_south_east = self._canvas.find_closest(
            (self._width+coords[0]+self._cell_size)%self._width,
            (self._height+coords[1]+self._cell_size)%self._height
        )
        cell_id_south = self._canvas.find_closest(
            coords[0],
            (self._height+coords[1]+self._cell_size)%self._height
        )
        cell_id_south_west = self._canvas.find_closest(
            (self._width+coords[0]-self._cell_size)%self._width,
            (self._height+coords[1]+self._cell_size)%self._height
        )
        return [
            cell_id_west, cell_id_north_west, cell_id_north, cell_id_north_east, cell_id_east, cell_id_south_east, cell_id_south, cell_id_south_west
        ]
        # self._canvas.itemconfigure(cell_id_west, fill="purple")
        # self._canvas.itemconfigure(cell_id_north_west, fill="purple")
        # self._canvas.itemconfigure(cell_id_north, fill="purple")
        # self._canvas.itemconfigure(cell_id_north_east, fill="purple")
        # self._canvas.itemconfigure(cell_id_east, fill="purple")
        # self._canvas.itemconfigure(cell_id_south_east, fill="purple")
        # self._canvas.itemconfigure(cell_id_south, fill="purple")
        # self._canvas.itemconfigure(cell_id_south_west, fill="purple")

        # print(
        #     self._canvas.coords(cell_id_west),
        #     self._canvas.coords(cell_id_north_west),
        #     self._canvas.coords(cell_id_north),
        #     self._canvas.coords(cell_id_north_east),
        #     self._canvas.coords(cell_id_east),
        #     self._canvas.coords(cell_id_south_east),
        #     self._canvas.coords(cell_id_south),
        #     self._canvas.coords(cell_id_south_west),
        # )

    def get_number_of_neighbours(self, cell_id):
        return sum(
            self._canvas.itemcget(cell, "fill") == "black"
            for cell in self.get_cell_neighbours_id(cell_id)
        )
    
    def start(self):
        rules = []
        for cell_id in self._canvas.find_all():
            if self._canvas.itemcget(cell_id, "fill") == "white" and self.get_number_of_neighbours(cell_id) == 3 or self._canvas.itemcget(cell_id, "fill") == "black" and self.get_number_of_neighbours(cell_id) in (2, 3):
                rules.append("black") 
            else: 
                rules.append("white")
        
        for index_rule, cell_id in enumerate(self._canvas.find_all()):
            self._canvas.itemconfigure(cell_id, fill=rules[index_rule])

        self._canvas.after(100, self.start)
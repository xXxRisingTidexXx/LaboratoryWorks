"""
Проект №2
ІПЗ - 12, Петраківський Данило


Ping-pong

It's a simple implementation of the famous game, where player is to move his paddle in order to avoid ball's hit of
the abyss. After recosheets the ball has an acceleration; each recosheet scores 1 point. Move, protect and compete!

The game is started from console; if you wanna exit it, press "Shift+Esc"; use left and right arrows to move the
paddle; collect score points after border hits.
"""
from random import choice
from time import sleep
from tkinter import *
from yaml import load

PROPERTIES = 'res/properties.yaml'
TK = 'tk'
TITLE = 'title'
RESIZABLE = 'resizable'
WM_ATTRIBUTES = 'wm_attributes'
SHIFT_ESCAPE = 'shift_escape'
CANVAS = 'canvas'
WIDTH = 'width'
HEIGHT = 'height'
BD = 'bd'
HIGHLIGHTTHICKNESS = 'highlightthickness'
PADDLE = 'paddle'
X1 = 'x1'
Y1 = 'y1'
X2 = 'x2'
Y2 = 'y2'
COLOR = 'color'
X0 = 'x0'
Y0 = 'y0'
DXL = 'dxl'
DXR = 'dxr'
LEFT_ARROW = 'left_arrow'
RIGHT_ARROW = 'right_arrow'
ABYSS = 'abyss'
BALL = 'ball'
DX = 'dx'
DY = 'dy'
GAME = 'game'
DELAY = 'delay'


def load_data():
    """
    It loads all data from property file; later it will be saved in Game class.
    """
    with open(PROPERTIES) as stream:
        return load(stream)


class Game:
    """
    The main app class, which is similar to Java's Application class and usually is the program's entry point.
    Contains all info about game's state, processes and objects.
    """
    def __init__(self):
        self.data = load_data()
        self.tk = self.__prepare_tk()
        canvas = self.__prepare_canvas()
        self.paddle = Paddle(canvas, self.data[PADDLE])
        self.abyss = Abyss(canvas, self.data[ABYSS])
        self.ball = Ball(canvas, self.data[BALL], self.paddle.id, self.abyss.id)
        self.flag = True
        self.delay = self.data[GAME][DELAY]

    def __prepare_tk(self):
        data = self.data[TK]
        tk = Tk()
        tk.title(data[TITLE])
        tk.geometry(self.__prepare_geometry(tk.winfo_screenwidth(), tk.winfo_screenheight()))
        tk.resizable(data[RESIZABLE][0], data[RESIZABLE][1])
        tk.wm_attributes(data[WM_ATTRIBUTES][0], data[WM_ATTRIBUTES][1])
        tk.bind_all(data[SHIFT_ESCAPE], self.__end_game)
        return tk

    def __prepare_geometry(self, screen_width, screen_height):
        w = self.data[CANVAS][WIDTH]
        h = self.data[CANVAS][HEIGHT]
        return '{}x{}+{}+{}'.format(w, h, (screen_width - w) // 2, (screen_height - h) // 2)

    # noinspection PyUnusedLocal
    def __end_game(self, event):
        self.flag = False

    def __prepare_canvas(self):
        data = self.data[CANVAS]
        canvas = Canvas(self.tk, width=data[WIDTH], height=data[HEIGHT],
                        bd=data[BD], highlightthickness=data[HIGHLIGHTTHICKNESS])
        canvas.pack()
        return canvas

    def start(self):
        while self.flag:
            self.ball.move()
            self.tk.update_idletasks()
            self.tk.update()
            sleep(self.delay)


class Paddle:
    def __init__(self, canvas, data):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(data[X1], data[Y1], data[X2], data[Y2], fill=data[COLOR])
        self.dxl = data[DXL]
        self.dxr = data[DXR]
        self.canvas.move(self.id, data[X0], data[Y0])
        self.canvas.bind_all(data[LEFT_ARROW], self.__move_left)
        self.canvas.bind_all(data[RIGHT_ARROW], self.__move_right)

    # noinspection PyUnusedLocal
    def __move_left(self, event):
        self.canvas.move(self.id, self.dxl if self.canvas.coords(self.id)[0] > 0 else 0, 0)

    # noinspection PyUnusedLocal
    def __move_right(self, event):
        self.canvas.move(self.id, self.dxr if self.canvas.coords(self.id)[2] < self.canvas.winfo_width() else 0, 0)


class Abyss:
    def __init__(self, canvas, data):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(data[X1], data[Y1], data[X2], data[Y2], fill=data[COLOR])
        self.canvas.move(self.id, data[X0], data[Y0])


class Ball:
    def __init__(self, canvas, data, paddle_id, abyss_id):
        self.canvas = canvas
        self.id = self.canvas.create_oval(data[X1], data[Y1], data[X2], data[Y2], fill=data[COLOR])
        self.paddle_id = paddle_id
        self.abyss_id = abyss_id
        self.dx = choice(data[DX])
        self.dy = choice(data[DY])
        self.canvas.move(self.id, data[X0], data[Y0])

    def move(self):
        coords = self.canvas.coords(self.id)
        flag = self.__hit_abyss(coords)
        self.dx = 1 if self.__hit_left_border(coords) else \
            -1 if self.__hit_right_border(coords) else 0 if flag else self.dx
        self.dy = 1 if self.__hit_top_border(coords) else \
            -1 if self.__hit_paddle(coords) else 0 if flag else self.dy
        self.canvas.move(self.id, self.dx, self.dy)

    def __hit_abyss(self, coords):
        abyss_coords = self.canvas.coords(self.abyss_id)
        return coords[3] >= abyss_coords[3]

    # noinspection PyMethodMayBeStatic
    def __hit_left_border(self, coords):
        return coords[0] <= 0

    def __hit_right_border(self, coords):
        return coords[2] >= self.canvas.winfo_width()

    # noinspection PyMethodMayBeStatic
    def __hit_top_border(self, coords):
        return coords[1] <= 0

    def __hit_paddle(self, coords):
        paddle_coords = self.canvas.coords(self.paddle_id)
        return paddle_coords[1] <= coords[3] <= paddle_coords[3] and \
            coords[2] >= paddle_coords[0] and coords[0] <= paddle_coords[2]


if __name__ == '__main__':
    Game().start()

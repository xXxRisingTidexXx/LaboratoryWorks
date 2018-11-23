"""
Проект №2
ІПЗ - 12, Петраківський Данило
"""
from random import choice
from time import sleep
from tkinter import *
from yaml import load

PROPERTIES = 'res/properties.yaml'
TK = 'tk'
TITLE = 'title'
RESIZABLE = 'resizesable'
BALL = 'ball'
PADDLE = 'paddle'
GAME = 'game'
DELAY = 'delay'


class Game:
    def __init__(self):
        self.data = self.__prepare_data()
        self.tk = self.__prepare_tk()
        canvas = self.__prepare_canvas()
        self.ball = Ball(canvas, self.data['ball'])
        self.paddle = Paddle(canvas, self.data['paddle'])
        self.delay = self.data['game']['delay']

    @staticmethod
    def __prepare_data():
        with open(PROPERTIES) as stream:
            return load(stream)

    def __prepare_tk(self):
        data = self.data['tk']
        tk = Tk()
        tk.title(data['title'])
        tk.geometry(self.__prepare_geometry(tk.winfo_screenwidth(), tk.winfo_screenheight()))
        tk.resizable(data['resizable'][0], data['resizable'][1])
        tk.wm_attributes(data['wm_attributes'][0], data['wm_attributes'][1])
        return tk

    def __prepare_geometry(self, screen_width, screen_height):
        w = self.data['canvas']['width']
        h = self.data['canvas']['height']
        return '{}x{}+{}+{}'.format(w, h, (screen_width - w) // 2, (screen_height - h) // 2)

    def __prepare_canvas(self):
        data = self.data['canvas']
        canvas = Canvas(self.tk, width=data['width'], height=data['height'],
                        bd=data['bd'], highlightthickness=data['highlightthickness'])
        canvas.pack()
        return canvas

    def start(self):
        while True:
            self.ball.draw()
            self.paddle.draw()
            self.tk.update_idletasks()
            self.tk.update()
            sleep(self.delay)


class Ball:
    def __init__(self, canvas, data):
        self.canvas = canvas
        self.id = self.canvas.create_oval(data['x1'], data['y1'], data['x2'], data['y2'], fill=data['color'])
        self.canvas.move(self.id, data['x0'], data['y0'])
        self.dx = choice(data['dx'])
        self.dy = choice(data['dy'])

    def draw(self):
        coords = self.canvas.coords(self.id)
        self.dx = 1 if coords[0] <= 0 else -1 if coords[2] >= self.canvas.winfo_width() else self.dx
        self.dy = 1 if coords[1] <= 0 else -1 if coords[3] >= self.canvas.winfo_height() else self.dy
        self.canvas.move(self.id, self.dx, self.dy)


class Paddle:
    def __init__(self, canvas, data):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(data['x1'], data['y1'], data['x2'], data['y2'], fill=data['color'])
        self.canvas.move(self.id, data['x0'], data['y0'])
        self.dx = 0
        self.dxl = data['dxl']
        self.dxr = data['dxr']
        self.canvas.bind_all(data['left_arrow'], self.__move_left)
        self.canvas.bind_all(data['right_arrow'], self.__move_right)

    # noinspection PyUnusedLocal
    def __move_left(self, evt):
        self.dx = self.dxl

    # noinspection PyUnusedLocal
    def __move_right(self, evt):
        self.dx = self.dxr

    def draw(self):
        coords = self.canvas.coords(self.id)
        self.dx = 0 if coords[0] <= 0 or coords[2] >= self.canvas.winfo_width() else self.dx
        self.canvas.move(self.id, self.dx, 0)
        self.dx = 0


if __name__ == '__main__':
    Game().start()

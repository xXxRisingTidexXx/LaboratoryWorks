"""
Проект №2
ІПЗ - 12, Петраківський Данило
"""
from time import sleep
from tkinter import *
from yaml import load


STRINGS = 'res/strings.yaml'


class Game:
    def __init__(self):
        self.tk = prepare_tk()
        self.canvas = Canvas(self.tk, width=500, height=400, bd=0, highlightthickness=0)
        self.canvas.pack()


def prepare_tk():
    tk = Tk()
    with open(STRINGS) as stream:
        tk.title(load(stream)['tk']['title'])
    tk.resizable(0, 0)
    tk.wm_attributes('-topmost', 1)
    return tk


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        pass


class Paddle:
    pass


def start():
    tk = Tk()
    tk.title("Ping-pong")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()
    ball = Ball(canvas, 'red')
    while True:
        tk.update_idletasks()
        tk.update()
        sleep(0.01)


if __name__ == '__main__':
    start()

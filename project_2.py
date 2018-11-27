"""
Проект №2
ІПЗ - 12, Петраківський Данило
"""
from random import choice
from time import sleep
from tkinter import *
from tkinter.font import Font

from yaml import load

PROPERTIES = 'res/properties.yaml'
TK = 'tk'
CANVAS = 'canvas'
FRAME = ''
TITLE = 'title'
WIDTH = 'width'
HEIGHT = 'height'
RESIZABLE = 'resizable'
WM_ATTRIBUTES = 'wm_attributes'
DELAY = 'delay'
ANCHOR = 'anchor'
ALIGN = 'align'
BG = 'bg'
BD = 'bd'
HIGHLIGHTTHICKNESS = 'highlightthickness'
HIGHLIGHTBACKGROUND = 'highlightbackground'
HIGHLIGHTCOLOR = 'highlightcolor'
BACKGROUND = 'background'
BORDERWIDTH = 'borderwidth'
ACTIVEBACKGROUND = 'activebackground'
ACTIVEFOREGROUND = 'activeforeground'
OFFSET = 'offset'
RELIEF = 'relief'
FILL = 'fill'
OUTLINE = 'outline'
TEXT = 'text'
FG = 'fg'
RELX = 'relx'
RELY = 'rely'
MAIN_MENU = 'main_menu'
GAME = 'game'
SUMMARY_MENU = 'summary_menu'
INFO_MENU = 'info_menu'
HELP_MENU = 'help_menu'
PADDLE = 'paddle'
BALL = 'ball'
X1 = 'x1'
Y1 = 'y1'
X2 = 'x2'
Y2 = 'y2'
X0 = 'x0'
Y0 = 'y0'
DX = 'dx'
DY = 'dy'
DXL = 'dxl'
DXR = 'dxr'
LEFT_ARROW = 'left_arrow'
RIGHT_ARROW = 'right_arrow'


def prepare_data():
    with open(PROPERTIES) as stream:
        return load(stream)


class App:
    def __init__(self):
        self.data = prepare_data()
        self.tk = self.__prepare_tk()
        self.main_menu = MainMenu(self.data, self.tk)

    def __prepare_tk(self):
        data = self.data[TK]
        tk = Tk()
        tk.title(data[TITLE])
        tk.geometry(self.__prepare_geometry(tk.winfo_screenwidth(), tk.winfo_screenheight()))
        tk.configure(background=data[BACKGROUND])
        tk.resizable(data[RESIZABLE][0], data[RESIZABLE][1])
        tk.wm_attributes(data[WM_ATTRIBUTES][0], data[WM_ATTRIBUTES][1])
        return tk

    def __prepare_geometry(self, screen_width, screen_height):
        w = self.data[TK][WIDTH]
        h = self.data[TK][HEIGHT]
        return '{}x{}+{}+{}'.format(w, h, (screen_width - w) // 2, (screen_height - h) // 2)

    def start(self):
        while self.main_menu.checked():
            self.tk.update_idletasks()
            self.tk.update()
            sleep(self.data[DELAY])


class MainMenu:
    def __init__(self, data, tk):
        self.data = data
        self.flag = True
        self.frame = Frame(tk, width=300, height=400, bg='#000000', highlightbackground='#c868db',
                           highlightthickness=2, padx=30, pady=30)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        button = Button(self.frame, text='Exit', font=Font(family='Helvetica', size=14, weight='bold'),
                        width=20, height=30, bg='#000000', fg='#ffffff', highlightbackground='#c868db',
                        highlightthickness=1, activebackground='#c868db', activeforeground='#ffffff')
        button.pack()

    def __exit(self):
        self.flag = False

    def checked(self):
        return self.flag


# class Game:
#     """
#     All game processes occur at this class; session data is stored here as well.
#     The game is 2D, that's why there's an (xOy) coordinate system.
#     The beginning O(0, 0) is situated at the top left corner of the canvas, so Y axis is directed downwards, and X
#     axis is directed rightwards.
#     That's why if object's <dx> (horizontal shift) > 0, it moves rightwards; if <dx> < 0, it moves leftwards;
#     if <dy> (vertical shift) > 0, object moves downwards; if <dy> < 0, it moves upwards.
#     """
#     def __init__(self, data, canvas):
#         self.data = data
#         self.canvas = canvas
#         self.flag = True
#         self.paddle = Paddle(canvas, self.data[PADDLE])
#         self.ball = Ball(canvas, self.data[BALL], self.paddle.id)
#
#     def __prepare_canvas(self):
#         data = self.data[CANVAS]
#         canvas = Canvas(self.tk, width=data[WIDTH], height=data[HEIGHT], bg=data[BG],
#                         bd=data[BD], highlightthickness=data[HIGHLIGHTTHICKNESS])
#         canvas.pack()
#         canvas.update()
#         return canvas
#
#     def checked(self):
#         return self.flag
#
#
# class Paddle:
#     """
#     Paddle object class, order by the player.
#     Use left and right arrows to move this stuff and hit the ball.
#
#         canvas:  TKinter's object, where paddle's rectangle is created and moved.
#         id:  paddle's id in the list of canvas' objects
#         dxl:  paddle's left movement in pixels per 1 tact
#         dxr:  paddle's right movement in pixels per 1 tact
#     """
#     def __init__(self, canvas, data):
#         self.canvas = canvas
#         self.id = self.canvas.create_rectangle(data[X1], data[Y1], data[X2], data[Y2], fill=data[FILL])
#         self.dxl = data[DXL]
#         self.dxr = data[DXR]
#         self.canvas.move(self.id, data[X0], data[Y0])
#         self.canvas.bind_all(data[LEFT_ARROW], self.__move_left)
#         self.canvas.bind_all(data[RIGHT_ARROW], self.__move_right)
#
#     # noinspection PyUnusedLocal
#     def __move_left(self, event):
#         """
#         Moves the paddle by <dxl> pixes leftwards.
#         """
#         self.canvas.move(self.id, self.dxl if self.canvas.coords(self.id)[0] > 0 else 0, 0)
#
#     # noinspection PyUnusedLocal
#     def __move_right(self, event):
#         """
#         Moves the paddle by <dxr> pixels rightwards.
#         """
#         self.canvas.move(self.id, self.dxr if self.canvas.coords(self.id)[2] < self.canvas.winfo_width() else 0, 0)
#
#
# class Ball:
#     """
#     The main game's flywheel, which forces the player to hit it.
#     It's a round itself, which has a speed vector, defined by <dx> and <dy> coordinates; after each hit the ball
#     has a little acceleration according to the physical principles.
#     If it overcomes the canvas' bottom, the player loses.
#
#         canvas:  TKinter's object, where ball's wheel is created.
#         canvas_width:  canvas width in pixels
#         canvas_height: canvas height in pixels
#         id:  ball's id in the list of canvas' objects
#         paddle_id:  paddle's id  used for hit calculation
#         dx:  horizontal shift in pixels per 1 tact
#         dy:  vertical shift in pixels per 1 tact
#     """
#     def __init__(self, canvas, data, paddle_id):
#         self.canvas = canvas
#         self.canvas_width = self.canvas.winfo_width()
#         self.canvas_height = self.canvas.winfo_height()
#         self.id = self.canvas.create_oval(data[X1], data[Y1], data[X2], data[Y2], fill=data[FILL])
#         self.paddle_id = paddle_id
#         self.dx = choice(data[DX])
#         self.dy = choice(data[DY])
#         self.canvas.move(self.id, data[X0], data[Y0])
#
#     def move(self):
#         """
#         Moves the ball on the canvas via the speed vector {<dx>, <dy>}.
#         """
#         coords = self.canvas.coords(self.id)
#         self.dx = 1 if self.__hit_left_border(coords) else -1 if self.__hit_right_border(coords) else self.dx
#         self.dy = 1 if self.__hit_top_border(coords) else -1 if self.__hit_paddle(coords) else self.dy
#         self.canvas.move(self.id, self.dx, self.dy)
#
#     def flies(self):
#         """
#         Checks if the ball has overcome the canvas' bottom.
#         """
#         return self.canvas.coords(self.id)[1] <= self.canvas_height
#
#     # noinspection PyMethodMayBeStatic
#     def __hit_left_border(self, coords):
#         """
#         Checks if the ball hits the canvas' left border.
#         """
#         return coords[0] <= 0
#
#     def __hit_right_border(self, coords):
#         """
#         Checks if the ball hits the canvas' right border.
#         """
#         return coords[2] >= self.canvas_width
#
#     # noinspection PyMethodMayBeStatic
#     def __hit_top_border(self, coords):
#         """
#         Checks if the ball hits the canvas' top border.
#         """
#         return coords[1] <= 0
#
#     def __hit_paddle(self, coords):
#         """
#         Checks if the ball hits the paddle.
#         """
#         paddle_coords = self.canvas.coords(self.paddle_id)
#         return paddle_coords[1] <= coords[3] <= paddle_coords[3] and \
#             coords[2] >= paddle_coords[0] and coords[0] <= paddle_coords[2]
#
#
# class SummaryMenu:
#     def __init__(self, data, canvas):
#         pass
#
#
# class HelpMenu:
#     def __init__(self, data, canvas):
#         pass
#
#
# class InfoMenu:
#     def __init__(self, data, canvas):
#         pass


if __name__ == '__main__':
    App().start()

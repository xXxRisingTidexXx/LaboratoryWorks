"""
Проект №2
ІПЗ - 12, Петраківський Данило
"""
from time import sleep
from tkinter import *
from tkinter.font import Font
from yaml import load

PROPERTIES = 'res/properties.yaml'
TK = 'tk'
TITLE = 'title'
BACKGROUND = 'background'
RESIZABLE = 'resizable'
WIDTH = 'width'
HEIGHT = 'height'
WM_ATTRIBUTES = 'wm_attributes'
DELAY = 'delay'
MAIN_MENU = 'main_menu'
FRAME = 'frame'
BG = 'bg'
HIGHLIGHTTHICKNESS = 'highlightthickness'
HIGHLIGHTBACKGROUND = 'highlightbackground'
PADX = 'padx'
PADY = 'pady'
RELX = 'relx'
RELY = 'rely'
ANCHOR = 'anchor'
BUTTON = 'button'
TEXTS = 'texts'
FONT = 'font'
FAMILY = 'family'
SIZE = 'size'
WEIGHT = 'weight'
STYLE = 'style'
RELIEF = 'relief'
FG = 'fg'
ACTIVEBACKGROUND = 'activebackground'
ACTIVEFOREGROUND = 'activeforeground'
IPADX = 'ipadx'
IPADY = 'ipady'
FILL = 'fill'

HELP_MENU = 'help_menu'
HEADER = 'header'
TEXT = 'text'
WRAPPER = 'wrapper'

# FOREGROUND = 'foreground'
# CANVAS = 'canvas'
# BD = 'bd'
# HIGHLIGHTCOLOR = 'highlightcolor'
# BORDERWIDTH = 'borderwidth'
# OFFSET = 'offset'
# OUTLINE = 'outline'
# GAME = 'game'
# INFO_MENU = 'info_menu'
# SUMMARY = 'summary'
# PADDLE = 'paddle'
# BALL = 'ball'
# X1 = 'x1'
# Y1 = 'y1'
# X2 = 'x2'
# Y2 = 'y2'
# X0 = 'x0'
# Y0 = 'y0'
# DX = 'dx'
# DY = 'dy'
# DXL = 'dxl'
# DXR = 'dxr'
# LEFT_ARROW = 'left_arrow'
# RIGHT_ARROW = 'right_arrow'


class App:
    def __init__(self):
        self.data = self.prepare_data()
        self.tk = self.prepare_tk(self.data[TK])
        self.delay = self.data[DELAY]
        self.main_menu = MainMenu(self.data[MAIN_MENU], self.tk)

    # noinspection PyMethodMayBeStatic
    def prepare_data(self):
        with open(PROPERTIES) as stream:
            return load(stream)

    # noinspection PyMethodMayBeStatic
    def prepare_tk(self, data):
        tk = Tk()
        tk.title(data[TITLE])
        tk.geometry('{}x{}'.format(tk.winfo_screenwidth(), tk.winfo_screenheight()))
        tk.configure(background=data[BACKGROUND])
        tk.resizable(data[RESIZABLE][WIDTH], data[RESIZABLE][HEIGHT])
        tk.wm_attributes(data[WM_ATTRIBUTES][0], data[WM_ATTRIBUTES][1])
        return tk

    def start(self):
        while self.main_menu.active:
            self.tk.update_idletasks()
            self.tk.update()
            sleep(self.delay)


class Menu:
    def __init__(self, data, tk):
        self.data = data
        self.tk = tk
        self.hidden = False
        self.frame = self.prepare_frame(self.data[FRAME])
        self.frame_place_info = None

    def prepare_frame(self, data):
        frame = Frame(self.tk, bg=data[BG], highlightthickness=data[HIGHLIGHTTHICKNESS],
                      highlightbackground=data[HIGHLIGHTBACKGROUND], padx=data[PADX], pady=data[PADY])
        frame.place(relx=data[RELX], rely=data[RELY], anchor=data[ANCHOR])
        frame.update()
        return frame

    def prepare_button(self, data, command, text=None, font=None):
        text = self.check_text(data, text)
        font = self.check_font(data, font)
        style = data[STYLE]
        button = Button(self.frame, text=text, font=font, command=command, relief=style[RELIEF],
                        highlightthickness=style[HIGHLIGHTTHICKNESS], bg=style[BG], fg=style[FG],
                        activebackground=style[ACTIVEBACKGROUND], activeforeground=style[ACTIVEFOREGROUND])
        button.pack(padx=style[PADX], pady=style[PADY], ipadx=style[IPADX], ipady=style[IPADY], fill=style[FILL])
        button.update()
        return button

    # noinspection PyMethodMayBeStatic
    def check_text(self, data, text):
        return data[TEXT] if text is None else text

    def check_font(self, data, font):
        return self.prepare_font(data[FONT]) if font is None else font

    # noinspection PyMethodMayBeStatic
    def prepare_font(self, data):
        return Font(family=data[FAMILY], size=data[SIZE], weight=data[WEIGHT])

    def prepare_label(self, data, text=None, font=None):
        text = self.check_text(data, text)
        font = self.check_font(data, font)
        label = Label(self.frame, text=text, font=font, relief=data[RELIEF],
                      highlightthickness=data[HIGHLIGHTTHICKNESS], bg=data[BG], fg=data[FG])
        label.pack(padx=data[PADX], pady=data[PADY], ipadx=data[IPADX], ipady=data[IPADY])
        label.update()
        return label

    def hide(self):
        if not self.hidden:
            self.hidden = True
            self.frame_place_info = self.frame.place_info()
            self.frame.place_forget()

    def visualize(self):
        if self.hidden:
            self.hidden = False
            self.frame.place(self.frame_place_info)


class MainMenu(Menu):
    def __init__(self, data, tk):
        super().__init__(data, tk)
        self.buttons = self.prepare_buttons(self.data[BUTTON])
        self.help_menu = None
        self.active = True

    def prepare_buttons(self, data):
        texts = data[TEXTS]
        font = self.prepare_font(data[FONT])
        return self.prepare_button(data, self.__play, texts[0], font), \
            self.prepare_button(data, self.__info, texts[1], font), \
            self.prepare_button(data, self.__help, texts[2], font), \
            self.prepare_button(data, self.__exit, texts[3], font)

    def __play(self):
        pass

    def __info(self):
        pass

    def __help(self):
        self.help_menu = self.check_help_menu()
        self.hide()
        self.help_menu.visualize()

    def check_help_menu(self):
        return HelpMenu(self.data[HELP_MENU], self.tk, self) if self.help_menu is None else self.help_menu

    def __exit(self):
        self.active = False


class HelpMenu(Menu):
    def __init__(self, data, tk, main_menu):
        super().__init__(data, tk)
        self.header_label = self.prepare_label(self.data[HEADER])
        self.wrapper_label = self.prepare_label(self.data[WRAPPER])
        self.back_button = self.prepare_button(self.data[BUTTON], self.__back)
        self.main_menu = main_menu

    def __back(self):
        self.hide()
        self.main_menu.visualize()


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
#         self.active = True
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
#     def active(self):
#         return self.active
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


if __name__ == '__main__':
    App().start()

from math import *
from tkinter import *


class Turtle:
    x = 0.0
    y = 0.0
    a = 0.0
    pen = 1
    canvas = None

    def __init__(self, canvas):
        self.canvas = canvas

    def setpen(self, yes):
        self.pen = yes

    def rotate(self, g):
        self.a += g

    def move(self, sx, sy):
        self.x = sx
        self.y = sy

    def forward(self, length, color):
        new_x = self.x + cos(pi / 180 * self.a) * length
        new_y = self.y + sin(pi / 180 * self.a) * length
        cx = xsize / 2
        cy = ysize / 2
        if self.pen:
            self.canvas.create_line(cx + self.x, cy - self.y, cx + new_x, cy - new_y, fill=color)
        self.x = new_x
        self.y = new_y

root = Tk()

xsize = 500
ysize = 600

c = Canvas(width=xsize, height=ysize, bg='grey')
c.focus_set()
c.pack()

root.mainloop()

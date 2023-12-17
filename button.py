from text import Text
from turtle import Turtle
import time


class Button(Text):

    def __init__(self):
        super().__init__()
        self.button = Text()
        self.x_pos = 0
        self.y_pos = 0

    def animate(self):
        self.bg = Turtle
        self.bg.color("white")
        self.bg.penup()
        self.bg.ht()
        new_text = self.button
        new_text.color("black")
        self.bg.clear()


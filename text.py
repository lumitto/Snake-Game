from turtle import Turtle


class Scoreboard(Turtle):

    ALIGNMENT = 'center'
    font_type = 'Consolas'
    boldness = 'normal'
    FONT = (font_type, 14, boldness)

    def __init__(self):
        super().__init__()
        self.var = None
        self.text = None
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0, 275)

    def refresh(self, var):
        self.var = var
        self.text = f"Score: {self.var}"
        self.write(arg=self.text, align=self.ALIGNMENT, font=self.FONT)


class Gameover(Scoreboard):

    def __init__(self):
        super().__init__()

    def refresh(self, var, pos_x, pos_y, size):
        self.goto(pos_x, pos_y)
        self.text = var
        self.write(arg=self.text, align=self.ALIGNMENT, font=('Consolas', size, 'normal'))


class Text(Turtle):

    ALIGNMENT = 'center'
    font_type = 'Consolas'
    boldness = 'normal'
    size = 14
    FONT = (font_type, size, boldness)

    def __init__(self):
        super().__init__()
        self.ht()
        self.color("white")
        self.penup()

    def print_tx(self, position, text, size):
        self.goto(position)
        self.write(arg=text, align=self.ALIGNMENT, font=(self.font_type, size, self.boldness))

from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    MOVE_DISTANCE = 20
    STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self):
        self.segments = []
        for _ in range(3):
            self.segment = Turtle()
            self.segment.penup()
            self.segment.color("white")
            self.segment.shape("square")
            self.segments.append(self.segment)
            self.create_snake_body()
            self.head = self.segments[0]

    def create_snake_body(self):
        """Creates a Snake's 'starting' body.
        Takes a list of segment's(Snake.segments) created by constructor."""
        for one_time in range(len(self.segments)):
            self.segments[one_time].goto(self.STARTING_POSITION[one_time])

    def add_segment(self, position):
        """Adds a new segment to the snake"""
        self.segment = Turtle()
        self.segment.penup()
        self.segment.color("white")
        self.segment.shape("square")
        self.segment.goto(position)
        self.segments.append(self.segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_the_snake(self):
        """Moves the snake's head on 1 position and forces other segments to follow it."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_pos)
        self.head.forward(Snake.MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def clear(self):
        self.clear()

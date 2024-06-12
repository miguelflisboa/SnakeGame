from turtle import Turtle

STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segs = []
        self.create_snake()
        self.head = self.segs[0]

    # ---------------------------------------------------------------------
    # Iniciating snake
    def create_snake(self):
        for pos in STARTING_POS:
            seg = Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto(pos)
            self.segs.append(seg)

    # ---------------------------------------------------------------------
    # Moving the snake
    def move(self):
        for n in range(len(self.segs) - 1, 0, -1):
            new = self.segs[n - 1].pos()
            self.segs[n].goto(new)
        self.head.forward(MOVE_DISTANCE)

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



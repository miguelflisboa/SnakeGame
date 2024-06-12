from turtle import Screen, Turtle
import time

# Iniciating the Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# Iniciating the snake
starting_pos = [(0,0),(-20,0),(-40,0)]

segs = []

for pos in starting_pos:
    seg = Turtle("square")
    seg.color("white")
    seg.penup()
    seg.goto(pos)
    segs.append(seg)

print(len(segs))
screen.update()

# Moving the snake
game_on = True

while game_on:

    for n in range(len(segs)-1,0,-1):
        new = segs[n-1].pos()
        segs[n].goto(new)

    segs[0].forward(20)


    screen.update()
    time.sleep(0.5)


# End
screen.exitonclick()
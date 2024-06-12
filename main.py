from turtle import Screen
from snake import Snake
import time

#---------------------------------------------------------------------
# Iniciating the Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#---------------------------------------------------------------------
# Inicializing the game

snake = Snake()
game_on = True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


#---------------------------------------------------------------------
# Game runing
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

#---------------------------------------------------------------------
# End
screen.exitonclick()
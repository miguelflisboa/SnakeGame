from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
food = Food()
scoreboard = Scoreboard()
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

    # Detect collision with food
    if snake.head.distance(food) < 5:
        food.refresh()
        scoreboard.increase_score()
        snake.new_seg()

    # Detect collision with end of the board
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with himself
    for seg in snake.segs[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()

#---------------------------------------------------------------------
# End

screen.exitonclick()
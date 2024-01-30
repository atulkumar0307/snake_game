from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game!")
screen.tracer(0)     # it turned off the lapping of segments as animation, so without update the screen will be blank.

snake = Snake()     # Making an object snake from class Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()     # it just shows the animation picture without showing lapping animation.
    time.sleep(0.1)     # it will slow down the picture overlapping time.
    snake.move()        # object.method

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent_segment()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game_tick = 0.090

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

is_game_on = True
while is_game_on:
    screen.update()
    snake.move()
    time.sleep(game_tick)

    # Detect collision with food
    if snake.head.distance(food) <= 15:
        if game_tick > 0.050:
            game_tick -= 0.001
        food.place()
        snake.grow()
        scoreboard.increase_score()

    # Check wall collisions
    if snake.head.xcor() >= 300:
        snake.head.setx(-280)
    if snake.head.xcor() <= -300:
        snake.head.setx(280)
    if snake.head.ycor() >= 300:
        snake.head.sety(-280)
    if snake.head.ycor() <= -300:
        snake.head.sety(280)

    # Tail collision
    for seg in snake.segments[1:]:  # omit the head
        if snake.head.distance(seg) <= 10:
            scoreboard.game_over()
            is_game_on = False


screen.exitonclick()

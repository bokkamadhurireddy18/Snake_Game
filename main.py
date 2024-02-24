from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
score= ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    #detect snake and food collision
    if snake.head.distance(food) <15:
        snake.extend()
        food.refresh()
        score.increase_score()

    #detect collision with walls
    if snake.head.xcor()< -280 or snake.head.xcor() > 280 or snake.head.ycor()< -280 or snake.head.ycor() > 280:
        game_is_on= False
        score.game_over()

    #detect collision with itself
    for seg in snake.segments[1:]: #exclude head
        if snake.head.distance(seg)<10:
            game_is_on= False
            score.game_over()

screen.exitonclick()
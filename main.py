from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakey Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

# Control the snake with key presses
screen.listen()
screen.onkey(snake.go_up, "w")
screen.onkey(snake.go_down, "s")
screen.onkey(snake.go_left, "a")
screen.onkey(snake.go_right, "d")


def hide_objects():
    snake.disappear()
    food.hideturtle()
    screen.update()


game_is_live = True
while game_is_live:
    screen.update()
    snake.move()
    time.sleep(0.1)

    # Detect collision with food
    if snake.head.distance(food) < 30:
        food.refresh()
        score.update_score()
        snake.grow()

    # Detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_is_live = False
        hide_objects()
        score.game_over()

    # Detect collision with own body
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_live = False
            hide_objects()
            score.game_over()
            break


screen.exitonclick()

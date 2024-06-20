from turtle import Screen
from snake import Snake  # Assuming you saved the Snake class in a file named snake.py
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakey Snake")
screen.tracer(0)

snake = Snake()

# Control the snake with key presses
screen.listen()
screen.onkey(snake.go_up, "w")
screen.onkey(snake.go_down, "s")
screen.onkey(snake.go_left, "a")
screen.onkey(snake.go_right, "d")

game_is_live = True
while game_is_live:
    screen.update()
    snake.move()
    time.sleep(0.1)

screen.exitonclick()

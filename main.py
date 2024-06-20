from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakey Snake")
screen.tracer(0)

snake_segments = 3
snake = []
x_pos = 0
offset = 20

for _ in range(snake_segments):
    segment = Turtle(shape="square")
    segment.shapesize(1, 1)
    segment.color("white")
    segment.penup()
    segment.setx(x_pos)
    snake.append(segment)
    x_pos -= 20

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Loop through the segments of the snake in reverse order, starting from the last segment.
    for i in range(len(snake) - 1, 0, -1):
        # Get the x and y coordinates of the segment right before the current segment.
        new_x = snake[i - 1].xcor()
        new_y = snake[i - 1].ycor()
        # Move the current segment to the position of the previous segment.
        snake[i].goto(new_x, new_y)
    # Move the head of the snake forward.
    snake[0].forward(20)

screen.exitonclick()
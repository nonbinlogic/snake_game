from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.move_distance = None
        self.offset = None
        self.snake = []
        self.snake_segments = 3
        self.x_pos = 0
        self.segment_size = 1  # Default segment size
        self.create_snake()
        self.head = self.snake[0]
        self.update_move_distance()  # Set initial move distance based on segment size

    def create_snake(self):
        for _ in range(self.snake_segments):
            self.add_segment((self.x_pos, 0))
            # `self.offset` is not used here directly until it is dynamically set
            self.x_pos -= self.segment_size * 20  # Initial positioning

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.shapesize(self.segment_size)  # Set the shape size to the current segment size
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    def update_move_distance(self):
        # Retrieve the size of the shape to determine the move distance
        shape_size = self.snake[0].shapesize()
        self.offset = shape_size[0] * 20  # Assume the base unit is 20 pixels per shape size unit
        self.move_distance = self.offset

    def change_segment_size(self, size):
        self.segment_size = size
        for segment in self.snake:
            segment.shapesize(size)
        self.update_move_distance()

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].setposition(new_x, new_y)
        self.head.forward(self.move_distance)

    def go_up(self):
        if self.head.heading() != DOWN:  # Prevent moving directly backward
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

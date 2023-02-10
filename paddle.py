import turtle as t

from constants import STRETCH_WIDTH, STRETCH_LENGTH, PADDLE_Y_POS, WINDOW_WIDTH


class Paddle:
    def __init__(self):
        self.paddle = t.Turtle()
        self.paddle.speed(0)
        self.paddle.shape('square')
        self.paddle.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        self.paddle.color('white')
        self.paddle.penup()
        self.paddle.goto(0, PADDLE_Y_POS)
        self.paddle.dx = 30

    def move(self, direction):
        x = self.paddle.xcor()

        if direction == 'Right':
            if x < (WINDOW_WIDTH / 2) - 70:
                self.paddle.setx(x + self.paddle.dx)

        if direction == 'Left':
            if x > -((WINDOW_WIDTH / 2) - 70):
                self.paddle.setx(x - self.paddle.dx)

    def reset(self):
        self.paddle.goto(0, PADDLE_Y_POS)

    def get_state(self):
        return [self.paddle.xcor(), self.paddle.dx]

import turtle as t

from constants import STRETCH_WIDTH, STRETCH_LENGTH, PADDLE_Y_POS, WINDOW_WIDTH


class Paddle:
    def __init__(self):
        self.stepX = 30

        self.paddle = t.Turtle()
        self.paddle.speed(0)
        self.paddle.shape('square')
        self.paddle.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        self.paddle.color('white')
        self.paddle.penup()
        self.paddle.goto(0, PADDLE_Y_POS)

    def move(self, direction):
        # Get paddle x position
        x = self.paddle.xcor()

        # If directions is right
        if direction == 'Right':
            # If paddle is located at coordinates smaller than the right side of wall 
            if x < (WINDOW_WIDTH / 2) - 70:
                # Change paddle x direction
                self.paddle.setx(x + self.stepX)

        # If directions is left
        if direction == 'Left':
            # If paddle is located at coordinates smaller than the left side of wall 
            if x > -((WINDOW_WIDTH / 2) - 70):
                # Change paddle x direction
                self.paddle.setx(x - self.stepX)

    def reset(self):
        # Reset paddle position
        self.paddle.goto(0, PADDLE_Y_POS)

    def get_state(self):
        # Return paddle state
        return [self.paddle.xcor(), self.stepX]

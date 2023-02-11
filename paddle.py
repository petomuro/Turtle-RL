import turtle as t

from constants import STRETCH_LENGTH, PADDLE_Y_POS, WINDOW_WIDTH


class Paddle:
    def __init__(self):
        self.stepX = 30

        self.paddle = t.Turtle()
        self.paddle.speed(0)
        self.paddle.shape('square')
        self.paddle.shapesize(stretch_len=STRETCH_LENGTH)
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
            # If paddle is located at coordinates greater than the left side of wall
            if x > -((WINDOW_WIDTH / 2) - 70):
                # Change paddle x direction
                self.paddle.setx(x - self.stepX)

    def quadrant(self):
        # Get paddle x position
        x = self.paddle.xcor()

        # If paddle is located at coordinates smaller than the right side of wall and zero
        if 0 < x < (WINDOW_WIDTH / 2) - 70:
            # Return 1 (4. quadrant)
            return 1

        # If paddle is located at coordinates greater than the left side of wall and zero
        if 0 > x > -((WINDOW_WIDTH / 2) - 70):
            # Return -1 (3. quadrant)
            return -1

        # If paddle is located at coordinates smaller than the length of paddle and zero or coordinates greater than
        # the length of paddle and zero
        if (0 < x < 70) or (0 > x > -70):
            # Return 0 (between quadrants)
            return 0

    def reset(self):
        # Reset paddle step
        self.stepX = 30

        # Reset paddle position
        self.paddle.goto(0, PADDLE_Y_POS)

    def get_state(self):
        # Return paddle state
        return [self.paddle.xcor() * 0.01]  # [self.paddle.xcor(), self.stepX]

import math
import turtle as t

from constants import BALL_Y_POS, PADDLE_Y_POS
from constants import WINDOW_WIDTH, WINDOW_HEIGHT


class Ball:
    def __init__(self):
        self.stepX = 3
        self.stepY = -3

        self.ball = t.Turtle()
        self.ball.speed(0)
        self.ball.shape('circle')
        self.ball.color('red')
        self.ball.penup()
        self.ball.goto(0, BALL_Y_POS)

    def move(self, paddle):
        # Get previous euclidean distance of ball and paddle
        prev_distance = self.paddle_distance(paddle)

        # Move ball
        self.ball.setx(self.ball.xcor() + self.stepX)
        self.ball.sety(self.ball.ycor() + self.stepY)

        # Get new euclidean distance of ball and paddle
        new_distance = self.paddle_distance(paddle)

        return prev_distance, new_distance

    def wall_collision(self):
        # If ball collides with right side of wall
        if self.ball.xcor() > (WINDOW_WIDTH / 2) - 10:
            # Change ball x direction
            self.stepX *= -1

        # If ball collides with left side of wall
        if self.ball.xcor() < -((WINDOW_WIDTH / 2) - 10):
            # Change ball x direction
            self.stepX *= -1

        # If ball collides with top side of wall
        if self.ball.ycor() > (WINDOW_HEIGHT / 2) - 10:
            # Change ball y direction
            self.stepY *= -1

    def ground_collision(self):
        # If ball collides with ground
        if self.ball.ycor() < -((WINDOW_HEIGHT / 2) - 10):
            # Reset ball position
            self.reset()

            return True

    def paddle_collision(self, paddle):
        # If ball collides with paddle
        if abs(self.ball.ycor() - (PADDLE_Y_POS + 20)) < 3 and abs(paddle.xcor() - self.ball.xcor()) < 70:
            # Change ball y direction
            self.stepY *= -1

            return True

    def paddle_distance(self, paddle):
        # Return euclidean distance
        return math.dist([self.ball.xcor(), self.ball.ycor()], [paddle.xcor(), paddle.ycor()])

    def reset(self):
        # Reset ball position
        self.ball.goto(0, BALL_Y_POS)

    def get_state(self):
        # Return ball state
        return [self.ball.xcor(), self.ball.ycor(), self.stepX, self.stepY]

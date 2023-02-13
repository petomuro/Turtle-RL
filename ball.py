import math
import random
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

        # Return previous and new euclidean distance
        return prev_distance, new_distance

    def wall_collision(self):
        # If ball collides with right side of wall
        if self.ball.xcor() > ((WINDOW_WIDTH / 2) - 10):
            # Change ball x direction
            self.stepX *= -1

        # If ball collides with left side of wall
        if self.ball.xcor() < -((WINDOW_WIDTH / 2) - 10):
            # Change ball x direction
            self.stepX *= -1

        # If ball collides with top side of wall
        if self.ball.ycor() > ((WINDOW_HEIGHT / 2) - 10):
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
        if (abs(self.ball.ycor() - (PADDLE_Y_POS + 20)) < 3) and (abs(paddle.xcor() - self.ball.xcor()) < 90):
            # Change ball y direction
            self.stepY *= -1

            return True

    # def obstacle_collision(self, obstacle):
    #     # TODO: Fix and add documentation
    #     if (obstacle.xcor() - 20) < self.ball.xcor() < (obstacle.xcor() + 20):
    #         if (obstacle.ycor() - 20) < self.ball.ycor() < (obstacle.ycor() + 20):
    #             self.stepX *= random.choice([-1, 1])
    #             self.stepY *= random.choice([-1, 1])

    def paddle_distance(self, paddle):
        # Return euclidean distance
        return math.dist([self.ball.xcor(), self.ball.ycor()], [paddle.xcor(), paddle.ycor()])

    def quadrant(self):
        # Get ball positions
        x = self.ball.xcor()
        y = self.ball.ycor()

        # If ball is located at coordinates smaller than the right side of wall and zero
        if 0 < x < ((WINDOW_WIDTH / 2) - 10):
            # If ball is located at coordinates greater than the bottom side of wall and zero
            if 0 > y > -((WINDOW_HEIGHT / 2) - 10):
                # Return 1, -1 (4. quadrant)
                return 1, -1

        # If ball is located at coordinates greater than the left side of wall and zero
        if 0 > x > -((WINDOW_WIDTH / 2) - 10):
            # If ball is located at coordinates greater than the bottom side of wall and zero
            if 0 > y > -((WINDOW_HEIGHT / 2) - 10):
                # Return -1, -1 (3. quadrant)
                return -1, -1

        # If ball is located at coordinates smaller than the length of ball and zero or coordinates greater than
        # the length of ball and zero
        if (0 < x < 10) or (0 > x > -10):
            # If ball is located at coordinates greater than the bottom side of wall and zero or greater than the
            # bottom side of wall and zero
            if (0 > y > -((WINDOW_HEIGHT / 2) - 10)) or (0 > y > -((WINDOW_HEIGHT / 2) - 10)):
                # Return 0 (between quadrants)
                return 0

    def paddle_angle(self, paddle):
        # Return angle between ball and paddle in radians
        return math.atan2(self.ball.ycor() - paddle.ycor(), self.ball.xcor() - paddle.xcor()) / math.pi

    def reset(self):
        # Reset ball steps
        self.stepX *= random.choice([-1, 1])
        self.stepY = -3

        # Reset ball position
        self.ball.goto(0, BALL_Y_POS)

    def get_state(self, paddle):
        # Return ball state
        return [self.ball.xcor() * 0.01, self.ball.ycor() * 0.01, self.stepX, self.stepY,
                self.paddle_distance(paddle) * 0.01, self.paddle_angle(paddle)]

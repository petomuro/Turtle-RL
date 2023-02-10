import turtle as t

from constants import BALL_Y_POS, PADDLE_Y_POS
from constants import WINDOW_WIDTH, WINDOW_HEIGHT


class Ball:
    def __init__(self):
        self.ball = t.Turtle()
        self.ball.speed(0)
        self.ball.shape('circle')
        self.ball.color('red')
        self.ball.penup()
        self.ball.goto(0, BALL_Y_POS)
        self.ball.dx = 3
        self.ball.dy = -3

    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def wall_collision(self):
        if self.ball.xcor() > (WINDOW_WIDTH / 2) - 10:
            self.ball.dx *= -1

        if self.ball.xcor() < -((WINDOW_WIDTH / 2) - 10):
            self.ball.dx *= -1

        if self.ball.ycor() > (WINDOW_HEIGHT / 2) - 10:
            self.ball.dy *= -1

    def ground_collision(self):
        if self.ball.ycor() < -((WINDOW_HEIGHT / 2) - 10):
            self.ball.goto(0, BALL_Y_POS)

            return True

    def paddle_collision(self, paddle):
        if abs(self.ball.ycor() - (PADDLE_Y_POS + 20)) < 2 and abs(paddle.xcor() - self.ball.xcor()) < 70:
            self.ball.dy *= -1

            return True

    def reset(self):
        self.ball.goto(0, BALL_Y_POS)

    def get_state(self):
        return [self.ball.xcor(), self.ball.ycor(), self.ball.dx, self.ball.dy]

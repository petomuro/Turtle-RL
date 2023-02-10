import turtle as t

from ball import Ball
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from paddle import Paddle
from score import Score


class Environment:
    def __init__(self):
        self.done = False
        self.reward = 0

        self.win = t.Screen()
        self.win.title('Turtle-RL')
        self.win.bgcolor('black')
        self.win.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.win.tracer(0)

        self.paddle = Paddle()
        self.ball = Ball()
        self.score = Score()

    def reset(self):
        self.paddle.reset()
        self.ball.reset()
        # self.score.reset()

        return self.paddle.get_state() + self.ball.get_state()

    def run_frame(self):
        self.win.update()

        self.ball.move()
        self.ball.wall_collision()

        if self.ball.ground_collision():
            self.score.increment_miss()

            self.done = True
            self.reward -= 3

        if self.ball.paddle_collision(self.paddle.paddle):
            self.score.increment_hit()

            self.done = False
            self.reward += 20

    def step(self, action):
        self.done = False
        self.reward = 0

        if action == 0:
            self.paddle.move('Left')
            self.reward -= 0.1

        if action == 2:
            self.paddle.move('Right')
            self.reward -= 0.1

        self.run_frame()

        state = self.paddle.get_state() + self.ball.get_state()

        return self.done, self.reward, state

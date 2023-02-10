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
        # Reset paddle, ball and score
        self.paddle.reset()
        self.ball.reset()
        # self.score.reset()

        # Return paddle and ball state
        return self.paddle.get_state() + self.ball.get_state()

    def run_frame(self):
        # Update turtle screen
        self.win.update()

        # Get previous and new euclidean distance of ball and paddle
        prev_ball_distance, new_ball_distance = self.ball.move(self.paddle.paddle)
        # Ball wall collision
        self.ball.wall_collision()

        # If ball collide with ground
        if self.ball.ground_collision():
            # Increment miss
            self.score.increment_miss()

            # Game done
            self.done = True
            # Penalty
            self.reward -= 3

        # If ball collide with paddle
        if self.ball.paddle_collision(self.paddle.paddle):
            # Increment hit
            self.score.increment_hit()

            # Reward
            self.reward += 20

        # If new ball euclidean distance is lower than previous euclidian distance between ball and paddle
        if new_ball_distance < prev_ball_distance:
            # Reward
            self.reward += 0.5

    def step(self, action):
        # Game not done
        self.done = False
        # No reward
        self.reward = 0

        # If action is left
        if action == 0:
            # Move paddle left
            self.paddle.move('Left')
            # Penalty
            self.reward -= 0.1

        # If action is right
        if action == 2:
            # Move paddle right
            self.paddle.move('Right')
            # Penalty
            self.reward -= 0.1

        # Run frame
        self.run_frame()

        # Get paddle and ball state
        state = self.paddle.get_state() + self.ball.get_state()

        # Return game state, reward and paddle + ball state
        return self.done, self.reward, state

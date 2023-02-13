import random
import turtle as t

from constants import WINDOW_WIDTH, WINDOW_HEIGHT, OBSTACLE_SHAPE, OBSTACLE_COLOR


class Obstacle:
    def __init__(self):
        self.obstacle = t.Turtle()
        self.obstacle.speed(0)
        self.obstacle.shape(OBSTACLE_SHAPE)
        self.obstacle.color(OBSTACLE_COLOR)
        self.obstacle.penup()
        self.obstacle.goto(
            (10 * random.randint(int(-((WINDOW_WIDTH / 2) - 10) / 10), int(((WINDOW_WIDTH / 2) - 10) / 10))),
            (10 * random.randint(int(-((WINDOW_HEIGHT / 2) - 100) / 10), int(((WINDOW_HEIGHT / 2) - 100) / 10))))

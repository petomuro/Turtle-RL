import turtle as t

from constants import SCORE_Y_POS


class Score:
    def __init__(self):
        self.hit, self.miss = 0, 0

        self.score = t.Turtle()
        self.score.speed(0)
        self.score.color('white')
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(0, SCORE_Y_POS)
        self.score.write("Hit: {}\tMissed: {}".format(self.hit, self.miss), align='center',
                         font=('Courier', 24, 'normal'))

    def write(self):
        self.score.clear()
        self.score.write("Hit: {}\tMissed: {}".format(self.hit, self.miss), align='center',
                         font=('Courier', 24, 'normal'))

    # def reset(self):
    #     self.hit, self.miss = 0, 0

    def increment_miss(self):
        self.miss += 1
        self.write()

    def increment_hit(self):
        self.hit += 1
        self.write()

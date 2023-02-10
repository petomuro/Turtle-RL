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
                         font=('Courier', 14, 'normal'))

    def write(self):
        # Rewrite score
        self.score.clear()
        self.score.write("Hit: {}\tMissed: {}".format(self.hit, self.miss), align='center',
                         font=('Courier', 14, 'normal'))

    # def reset(self):
    #     # Reset ball position
    #     self.hit, self.miss = 0, 0
    #     self.score.goto(0, SCORE_Y_POS)

    def increment_miss(self):
        # Increment miss and rewrite score
        self.miss += 1
        self.write()

    def increment_hit(self):
        # Increment hit and rewrite score
        self.hit += 1
        self.write()

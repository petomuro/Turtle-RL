from datetime import date

import matplotlib.pyplot as plt
import numpy as np

from constants import TRAIN_DQN, EPISODES, MAX_STEPS_PER_EPISODE, STATE_SPACE
from dqn import DQN
from environment import Environment


def run_main(env):
    agent = DQN()

    if not TRAIN_DQN:
        agent.load_model()

    loss = []

    for e in range(EPISODES):
        state = env.reset(e)
        state = np.reshape(state, (1, STATE_SPACE))
        score = 0

        for i in range(MAX_STEPS_PER_EPISODE):
            action = agent.act(state)
            done, reward, next_state = env.step(action)
            score += reward
            next_state = np.reshape(next_state, (1, STATE_SPACE))

            if TRAIN_DQN:
                agent.remember(state, action, reward, next_state, done)

            state = next_state

            if TRAIN_DQN:
                agent.replay()

            if done:
                break

        print('Episode: {}/{}, Score: {}'.format((e + 1), EPISODES, score))

        loss.append(score)

    if TRAIN_DQN:
        agent.save_model()

    return loss


if __name__ == '__main__':
    environment = Environment()
    total_loss = run_main(environment)

    plt.plot([i for i in range(EPISODES)], total_loss)
    plt.xlabel('episodes')
    plt.ylabel('reward')
    # plt.show()
    plt.savefig(('train_progress{}' if TRAIN_DQN else 'test_progress{}').format(date.today()))

import matplotlib.pyplot as plt
import numpy as np

from dqn import DQN
from environment import Environment


def train_dqn(eps, env):
    action_space = 3
    state_space = 7

    agent = DQN(action_space, state_space)

    # max_steps = 1000
    loss = []

    for e in range(eps):
        state = env.reset(e, eps)
        state = np.reshape(state, (1, state_space))
        score = 0

        while True:  # for i in range(max_steps):
            action = agent.act(state)
            done, reward, next_state = env.step(action)
            score += reward
            next_state = np.reshape(next_state, (1, state_space))
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            agent.replay()

            if done:
                print("episode: {}/{}, score: {}".format(e, eps, score))

                break

        loss.append(score)

    return loss


if __name__ == '__main__':
    episodes = 100
    environment = Environment()

    total_loss = train_dqn(episodes, environment)

    plt.plot([i for i in range(episodes)], total_loss)
    plt.xlabel('episodes')
    plt.ylabel('reward')
    plt.show()

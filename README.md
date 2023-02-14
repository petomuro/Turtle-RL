# Turtle-RL

Turtle-RL - Simple Pong Game created in Python connected with neural network. Main tech stack used in this project:

- Python
- Keras
- Numpy
- Matplotlib
- Turtle

## Project setup

This project was developed and tested
on [Python version 3.10.10](https://www.python.org/downloads/release/python-31010/). It is really recommended to use
mentioned version of Python. Set up your virtual environment and run:

`pip install --no-cache-dir -r requirements.txt` (for macOS users -> instead of `tensorflow~=2.11.0`
use `tensorflow-macos~=2.11.0`)

then:

`python main.py`

## Train DQN

If you want to train DQN change `TRAIN_DQN` to `True` and run `main.py`. After training is
completed, the model and plot is saved to main directory. Change episodes and max steps in `constants.py` according to
your needs.

## Test DQN

If you want to test DQN, just change `TRAIN_DQN` to `False` and run `main.py`. After test is completed, the plot is
saved to main directory.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Filename: pendulum.py
# @Date: 2019-06-29-14-43
# @Author: Hany Abdulsamad
# @Contact: hany@robot-learning.de


import gym
from trajopt.elqr import eLQR

# pendulum task
env = gym.make('Pendulum-TO-v0')
env._max_episode_steps = 100

alg = eLQR(env, nb_steps=100,
           activation=range(-1, 0))

# run eLQR
trace = alg.run()

# plot forward pass
alg.plot()

# plot objective
import matplotlib.pyplot as plt

plt.figure()
plt.plot(trace)
plt.show()

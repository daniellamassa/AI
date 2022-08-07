# Writeup

For this assignment, I was able to implement a q-learning algorithm on the coffee game. I included several methods for my q-learning class, which included:

* initialize_qtable: resets the q table by filling it with zeros, size is determined by the observation space and the action space.

* render: loads the environment, render can be enabled/disabled to speed up learning.

* set_step_action: used to explore the environment, can either make a random or best guess decision. The .sample() function from the coffee game is used to make a random decision. Otherwise, to make a best guess decision, the maximum value from the current qtable is used (to indicate highest reward outcome).

* learn: performs q-learning in the coffee environment. Iterates through all episodes and steps per episode, and utilizes set_step_action to maximize reward. Also updates the qtable based on the action that is taken.

* behave: Tests if the q-learning algorithm has been successful (based off the learn method). Only chooses actions from the start state to end state that maximizes the reward. Need to run learn first to see what actions increase or decrease reward, and then behave can be used to actually solve the problem/move the player correctly.

* Analytics: I found that the per-episode reward does increase between the first 1000 episodes and the second.

* Decay Rates: Even with a decay rate of 0.005 (the exploration rate slowly decreases over epochs) the q-learning algorithm was still able to solve the coffee game. I also found that a decay rate of 0.01 still worked, but a decay rate of 0.1 did not. 

#interactive q learning on coffee game


import coffeegame
import numpy as np
import getch

def printQTable(qt):
    rows,cols  = qt.shape
    print("State ||    LEFT  |   DOWN  |   RIGHT  | UP     |")
    print("-------------------------------------------------")
    for row in range(rows):
        outstr = "   "+str(row)+"  "
        col = qt[row]
        for val in col:
            outstr+='    {:6.2f}'.format(val)
        print(outstr)


class QLearningAgent:

    def __init__(self, env, alpha=0.1, gamma=0.6, epsilon=0.5):

        self.alpha = alpha # learning rate
        self.gamma = gamma # discount rate
        self.epsilon = epsilon # exploration rate
        self.max_steps_per_episode = 100 ### CHANGE THIS
        self.num_episodes = 3000 ### CHANGE THIS
        self.environment = env
        self.current_state = self.environment.reset()
        self.action = None

        self.initialize_qtable()

    def initialize_qtable(self):
#         self.action_space_size = self.environment.action_space.n
#         self.state_space_size = self.environment.observation_space.n
        #fill with zeros of size
        self.qtable = np.zeros((self.environment.observation_space.n, self.environment.action_space.n))

    def render(self):
        #load enviroment
        self.environment.render()
        printQTable(self.qtable)

    def set_step_action(self):
        if np.random.random() < self.epsilon:
            # make a random decision (explore)
            self.action = self.environment.action_space.sample()
        else:
            # make a best-guess decision

#             actions = self.qtable[self.current_state]
#             self.action = max(actions)

            self.action = np.argmax(self.qtable[self.current_state, :])
#             self.action = np.argmax(self.qtable[self.current_state][:]) <-- slicing: make copy of array without modifying original


    def learn(self, render=False):
        # perform q-learning in the given environment
        rewards = []

        for episode in range(self.num_episodes):
            # reset environment for this episode
            self.current_state = self.environment.reset()
            episode_reward = 0

            # iterate through steps per episode
            for step in range(self.max_steps_per_episode):

                if render:
                    self.render()

                # set action that maxamizes reward
                self.set_step_action()
                next_state, reward, isDone, _ = self.environment.step(self.action)
                # _ is a throwaway variable, otherwise: error (ValueError: too many values to unpack)

                episode_reward += reward

                # update qtable
                self.qtable[self.current_state, self.action] = \
                    self.qtable[self.current_state,self.action] * (1 - self.alpha) + \
                    self.alpha * (reward + self.gamma * np.max(self.qtable[next_state, :]))

                self.current_state = next_state

                if isDone:
                    if render:
                        self.render()
                    break

            rewards.append(episode_reward)

        # ANALYTICS: the per-episode reward does increase between the first 1000 episodes and the second.
        print(f"First 1000 AVG: {sum(rewards[0:1000])/1000}")
        print(f"Second 1000 AVG: {sum(rewards[1000:2000])/1000}")

    def behave(self, render=False):
        # very similar to learn
        # test to see if learn has been sucessful: choose actions that maxamize reward
        self.current_state = self.environment.reset()

        for step in range(self.max_steps_per_episode):

            if render:
                self.render()

            # set action that maxamizes reward
            self.set_step_action()
            next_state, reward, isDone, info = self.environment.step(self.action)

            self.current_state = next_state

            if isDone:
                if render:
                    self.render()
                break





if __name__ == "__main__":
    environment = coffeegame.CoffeeEnv()
    agent = QLearningAgent(environment)

    agent.learn(render=False)
    agent.behave(render=True)


exit()

# interactive mode below
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

learning_rate = 0.1
discount_rate = 0.6
env = coffeegame.CoffeeEnv()

action_space_size = env.action_space.n
state_space_size = env.observation_space.n

#create the qtable
q_table = np.zeros((state_space_size, action_space_size))


#reset environment
state = env.reset()
while(True):
    #print some stuff
    env.render()
    printQTable(q_table)
    print('0: LEFT, 1: DOWN, 2: RIGHT, 3:UP')
    # get next action from user
    #you'll need to install getch in order to get this part to work
    # or comment out and replace with the line below it.
    # pip3 install --user getch
    action = int(getch.getch())%4
    #action = int(input('0: LEFT, 1: DOWN, 2: RIGHT, 3:UP'))
    new_state,reward,done, info = env.step(action)
    #the q learning magic happens here.
    q_table[state,action] = q_table[state, action] * (1 - learning_rate) + \
                            learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))
    if (done):
            #reset if game is over
        state = env.reset()
    else:
            #otherwise update state
        state = new_state

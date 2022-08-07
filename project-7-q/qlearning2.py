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


class QLearningAgent2:

    def __init__(self, env, alpha=0.1, gamma=0.6, epsilon=0.5):

        self.alpha = alpha # learning rate
        self.gamma = gamma # discount rate
        self.epsilon = epsilon # exploration rate
        self.max_steps_per_episode = 100 ### CHANGE THIS
        self.num_episodes = 3000 ### CHANGE THIS
        self.environment = env
        self.current_state = self.environment.reset()
        self.action = None

        ### DIFFERENCE HERE
        self.epsilon_decay = 0.005

        self.initialize_qtable()

    def initialize_qtable(self):
        self.action_space_size = self.environment.action_space.n
        self.state_space_size = self.environment.observation_space.n
        self.qtable = np.zeros((self.state_space_size, self.action_space_size))

    def render(self):
        self.environment.render()
        printQTable(self.qtable)

    def set_step_action(self):
        if np.random.random() < self.epsilon:
            # make a random decision (explore)
            self.action = self.environment.action_space.sample()
        else:
            # make a best-guess decision
            self.action = np.argmax(self.qtable[self.current_state, :])


    def learn(self, render=False):

        rewards = []

        for episode in range(self.num_episodes):
            # reset environment for this episode
            self.current_state = self.environment.reset()
            episode_reward = 0

            for step in range(self.max_steps_per_episode):
                if render:
                    self.render()

                self.set_step_action()
                next_state, reward, isDone, _ = self.environment.step(self.action)

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
            ### DIFFERENCE HERE
            self.epsilon = self.epsilon * (1 - self.epsilon_decay) ### DIFFERENCE HERE
            rewards.append(episode_reward)

        print(f"First 1000 AVG: {sum(rewards[0:1000])/1000}")
        print(f"Second 1000 AVG: {sum(rewards[1000:2000])/1000}")

    def behave(self, render=False):
        self.current_state = self.environment.reset()

        for step in range(self.max_steps_per_episode):

            if render:
                self.render()

            self.set_step_action()
            next_state, reward, isDone, _ = self.environment.step(self.action)

            self.current_state = next_state

            if isDone:
                if render:
                    self.render()
                break



if __name__ == "__main__":
    environment = coffeegame.CoffeeEnv()
    agent = QLearningAgent2(environment)

    print("hello")
    agent.learn(render=False)
    agent.behave(render=True)

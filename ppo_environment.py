import gym
from gym import spaces
import numpy as np


class StudentPerformanceEnv(gym.Env):
    def __init__(self, data, target):
        super(StudentPerformanceEnv, self).__init__()
        self.data = data
        self.target = target
        self.current_index = 0

        # Define action and observation spaces
        # Number of possible interventions (one for each class)
        self.action_space = spaces.Discrete(7)  # Adjust based on the number of classes or interventions

        # Observation space: Adjust based on total number of features
        self.observation_space = spaces.Box(low=-1, high=1, shape=(data.shape[1],), dtype=np.float32)

        self.reset()

    def reset(self):
        self.current_index = 0
        self.state = self.data.iloc[self.current_index].values
        return self.state

    def step(self, action):
        tutoring_effectiveness = 0.1

        # Extract the grades for Year 3 from the state
        # Assuming class interventions affect grades for specific classes
        initial_grades = self.state[2:9]  # Adjust indices according to your state structure

        # Apply tutoring intervention
        class_index = action
        new_grades = initial_grades.copy()
        new_grades[class_index] = min(new_grades[class_index] * (1 + tutoring_effectiveness), 100)

        # Calculate the average before and after tutoring
        initial_average = np.mean(initial_grades)
        new_average = np.mean(new_grades)

        # Calculate reward
        reward = (new_average - initial_average) / 100  # Normalize reward

        # Update the state and determine if we're done
        self.current_index += 1
        done = self.current_index >= len(self.data)

        if done:
            self.state = np.zeros(self.data.shape[1])
        else:
            self.state = self.data.iloc[self.current_index].values

        return self.state, reward, done, {}

    def render(self, mode='human'):
        pass

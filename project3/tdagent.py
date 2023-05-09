from abstractagent import AbstractAgent
from blackjack import BlackjackObservation, BlackjackEnv
from carddeck import *


class TDAgent(AbstractAgent):
    """
    Implementation of an agent that plays the same strategy as the dealer.
    This means that the agent draws a card when sum of cards in his hand
    is less than 17.

    Your goal is to modify train() method to learn the state utility function.
    I.e. you need to change this agent to a passive reinforcement learning
    agent that learns utility estimates using temporal diffrence method.
    """

    def train(self):
        for i in range(self.number_of_epochs):
            print(i)
            observation = self.env.reset()
            terminal = False
            reward = 0
            while not terminal:
                # render method will print you the situation in the terminal
                # self.env.render()
                action = self.make_step(observation, reward, terminal)
                observation, reward, terminal, _ = self.env.step(action)
                # TODO your code will be very likely here
            # self.env.render()

    def make_step(self, observation: BlackjackObservation, reward: float, terminal: bool) -> int:
        return 1 if observation.player_hand.value < 17 else 0

    def get_u_value(self, observation: BlackjackObservation) -> float:
        """
        Implement this method so that I can test your code. This method is supposed to return your learned U value for
        particular observation.

        :param observation: The observation as in the game. Contains information about what the player sees - player's
        hand and dealer's hand.
        :return: The learned U-value for the given observation.
        """
        pass

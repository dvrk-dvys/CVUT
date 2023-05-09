import itertools
from collections import defaultdict
from typing import Any

from abstractagent import AbstractAgent
from blackjack import BlackjackEnv, BlackjackObservation
from carddeck import *
import random


class Qsave():
    def __init__(self):
        self.Qt = defaultdict(float)


class SarsaAgent(AbstractAgent, Qsave):
    """
    Here you will provide your implementation of SARSA method.
    You are supposed to implement train() method. If you want
    to, you can split the code in two phases - training and
    testing, but it is not a requirement.

    For SARSA explanation check AIMA book or Sutton and Burton
    book. You can choose any strategy and/or step-size function
    (learning rate).
    """



    def train(self):
        Q = defaultdict(float)
        # self.playerstates = list(range(1, 22))
        # self.dealerstates = list(range(1, 11))
        # for each in self.playerstates:
        #     for _ in self.dealerstates:
        #         Q[(each, _), 0] = 0
        #         Q[(each, _), 1] = 0

        # Q = defaultdict(list)
        # # [player sum] + dealer sum = 12~0 -> 12~9
        # for _ in range(6, 17):
        #     for x in range(5, 21):
        #         code = int('%d%d' % (_, x))
        #         Q[code, 0] = 0
        #         Q[code, 1] = 0

        # 200 = player card 6 and below with Ace
        # Q[200, 0] = 0
        # Q[200, 1] = 0
        #
        # # player card and ace = 2
        # for _ in range(8, 21):
        #     for x in range(18):
        #         code = int('%d%d' % (_, x))
        #         Q[code, 0] = 0
        #         Q[code, 1] = 0

        for i in range(self.number_of_epochs):
            print(i)

            observation = self.env.reset()
            self.player = observation.player_hand.value()
            self.dealer = observation.dealer_hand.value()
            self.encoding = None
            # self.usableAce = 0
            self.gamma = 0.97
            self.alpha = 0.01

            code = self.make_step(observation)
            if Q[code, 0] > Q[code, 1]:
                action = 0
            elif Q[code, 0] < Q[code, 1]:
                action = 1
            else:
                action = 0
            if i < self.number_of_epochs * 0.5:
                if self.decision(.50) == True:
                    action = random.randint(0, 1)
                    # action = 0

            # TODO your code here
            terminal = False
            reward = 0
            while not terminal:
                next_observation, reward, terminal, _ = self.env.step(action)

                next_code = self.make_step(next_observation)
                if Q[next_code, 0] > Q[next_code, 1]:
                    next_action = 0
                elif Q[next_code, 0] < Q[next_code, 1]:
                    next_action = 1
                else:
                    next_action = 0

                # try:
                # if i > 75:
                #     self.gamma = .50
                # self.gamma = 0
                target = float(reward) + (self.gamma * Q[next_code, next_action])
                # except ValueError:
                #     return ('oops')
                Q[code, action] = Q[code, action] + (self.alpha * (target - Q[code, action]))
                self.get_q_value(Q[code, action], observation, action)
                # print(Q[code, action])

                code = next_code
                action = next_action
        print('test')

    def make_step(self, observationMS: BlackjackObservation) -> int:
        self.player = observationMS.player_hand.value()
        self.dealer = observationMS.dealer_hand.value()

        code = (self.player, self.dealer)

        try:
            # print(code)
            return code
        except ValueError:
            print('oops')
            print(str(observationMS.dealer_hand.cards[0].rank.name))
            return ('oops')

    def decision(self, probability):
        return random.random() < probability

    def get_q_value(self, update: None, observation: BlackjackObservation, action: int) -> float:
        """
        Implement this method so that I can test your code. This method is supposed to return your learned Q value for
        particular observation and action.

        :param observation: The observation as in the game. Contains information about what the player sees - player's
        hand and dealer's hand.
        :param action: Action for Q-value.
        :return: The learned Q-value for the given observation and action.

        """

        # Q = defaultdict(float)
        self.player = observation.player_hand.value()
        self.dealer = observation.dealer_hand.value()
        code = (self.player, self.dealer)

        if update != None:
            self.Qt[code, action] = update

        return self.Qt[code, action]

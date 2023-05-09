# import itertools
# from collections import defaultdict
#
# from abstractagent import AbstractAgent
# from blackjack import BlackjackEnv, BlackjackObservation
# from carddeck import *
# import random
#
#
# class SarsaAgent(AbstractAgent):
#     """
#     Here you will provide your implementation of SARSA method.
#     You are supposed to implement train() method. If you want
#     to, you can split the code in two phases - training and
#     testing, but it is not a requirement.
#
#     For SARSA explanation check AIMA book or Sutton and Burton
#     book. You can choose any strategy and/or step-size function
#     (learning rate).
#     """
#
#
#
#
#     def train(self):
#         Q = defaultdict(list)
#         self.playerstates = list(range(1, 22))
#         self.dealerstates = list(range(1, 11))
#         for each in self.playerstates:
#             for _ in self.dealerstates:
#                 Q[(each, _), 0] = 0
#                 Q[(each, _), 1] = 0
#
#
#
#         for i in range(self.number_of_epochs):
#             print(i)
#
#
#             observation = self.env.reset()
#             self.player = observation.player_hand.value()
#             self.dealer = observation.dealer_hand.value()
#             self.encoding = None
#             # self.usableAce = 0
#             self.gamma = 0.87
#             self.alpha = 0.05
#
#             code = self.make_step(observation)
#             if Q[code, 0] > Q[code, 1]:
#                 action = 0
#             elif Q[code, 0] < Q[code, 1]:
#                 action = 1
#             else:
#                 action = 0
#
#             if self.decision(.01) == True:
#                 action = random.randint(0, 1)
#                 # action = 0
#
#
#             # TODO your code here
#             terminal = False
#             reward = 0
#             while not terminal:
#                 next_observation, reward, terminal, _ = self.env.step(action)
#
#                 next_code = self.make_step(next_observation)
#                 if Q[next_code, 0] > Q[next_code, 1]:
#                     next_action = 0
#                 elif Q[next_code, 0] < Q[next_code, 1]:
#                     next_action = 1
#                 else:
#                     next_action = 0
#
#                 # try:
#                 if i > 85:
#                     # self.gamma = .50
#                     self.gamma = 0
#                 target = float(reward) + (self.gamma * Q[next_code, next_action])
#                 # except ValueError:
#                 #     return ('oops')
#                 Q[code, action] = Q[code, action] + (self.alpha * (target - Q[code, action]))
#                 # print(Q[code, action])
#
#     def make_step(self, observationMS: BlackjackObservation) -> int:
#         self.player = observationMS.player_hand.value()
#         self.dealer = observationMS.dealer_hand.value()
#
#         # Player sum
#         if self.player >= 21:
#             if self.dealer >= 10:
#                 code = (21, 10)
#             else:
#                 code = (21, self.dealer)
#         else:
#             if self.dealer >= 10:
#                 code = (self.player, 10)
#             else:
#                 code = (self.player, self.dealer)
#
#
#         try:
#             # print(code)
#             return code
#         except ValueError:
#             print('oops')
#             print(str(observationMS.dealer_hand.cards[0].rank.name))
#             return ('oops')
#
#     def decision(self, probability):
#         return random.random() < probability
#
#     def get_q_value(self, observation: BlackjackObservation, action: int) -> float:
#         """
#         Implement this method so that I can test your code. This method is supposed to return your learned Q value for
#         particular observation and action.
#
#         :param observation: The observation as in the game. Contains information about what the player sees - player's
#         hand and dealer's hand.
#         :param action: Action for Q-value.
#         :return: The learned Q-value for the given observation and action.
#
#         """
#         pass
#
#
# def train(self):
#     Q = defaultdict(list)
#
#     # 100 = player sum 8 and below
#     for x in range(18):
#         code = int('%d%d' % (10, x))
#         Q[code, 0] = 0
#         Q[code, 1] = 0
#
#     # [player sum] + dealer sum = 12~0 -> 12~9
#     for _ in range(9, 18):
#         for x in range(18):
#             code = int('%d%d' % (_, x))
#             Q[code, 0] = 0
#             Q[code, 1] = 0
#
#     # 200 = player card 6 and below with Ace
#     Q[200, 0] = 0
#     Q[200, 1] = 0
#
#     # player card and ace = 2*
#     for _ in range(27, 29):
#         for x in range(18):
#             code = int('%d%d' % (_, x))
#             Q[code, 0] = 0
#             Q[code, 1] = 0
#
#     for i in range(self.number_of_epochs):
#         print(i)
#
#         observation = self.env.reset()
#         self.player = observation.player_hand.value()
#         self.dealer = observation.dealer_hand.value()
#         self.encoding = None
#         self.usableAce = 0
#         self.gamma = 0.85
#         self.alpha = 0.05
#         self.next = 1
#
#         code = self.make_step(observation)
#         if Q[code, 0] > Q[code, 1]:
#             action = 0
#         elif Q[code, 0] < Q[code, 1]:
#             action = 1
#         else:
#             action = 1
#
#         # print((self.player, self.dealer, self.usableAce))
#         # TODO your code here
#         terminal = False
#         reward = 0
#         while not terminal:
#             # action = self.make_step(observation, reward, terminal)
#             next_observation, reward, terminal, _ = self.env.step(action)
#             # self.player = observation.player_hand.value()
#             # self.dealer = observation.dealer_hand.value()
#             next_code = self.make_step(next_observation)
#             if Q[next_code, 0] > Q[next_code, 1]:
#                 action = 0
#             elif Q[next_code, 0] < Q[next_code, 1]:
#                 action = 1
#             else:
#                 action = 1
#
#             # if reward == 0:
#             try:
#                 target = float(reward) + (self.gamma * Q[next_code, action])
#             except ValueError:
#                 return ('oops')
#             Q[code, action] = Q[code, action] + (self.alpha * (target - Q[code, action]))
#
#
# def make_step(self, observationMS: BlackjackObservation) -> int:
#     self.player = observationMS.player_hand.value()
#     self.dealer = observationMS.dealer_hand.value()
#     if self.dealer >= 17:
#         print()
#
#     for each in observationMS.player_hand.cards:
#         if each.rank == Rank.ACE:
#             self.usableAce = 1
#
#     if self.usableAce == 0:
#         if self.player >= 17:
#             if observationMS.dealer_hand.cards[0].rank == Rank.ACE:
#                 code = int('%d%d' % (17, 0))
#             else:
#                 if self.dealer >= 17:
#                     code = int('%d%d' % (17, 17))
#                 else:
#                     code = int('%d%d' % (17, self.dealer - 1))
#         elif self.player <= 8:
#             if observationMS.dealer_hand.cards[0].rank == Rank.ACE:
#                 code = int('%d%d' % (10, 0))
#             else:
#                 if self.dealer >= 17:
#                     code = int('%d%d' % (10, 17))
#                 else:
#                     code = int('%d%d' % (10, self.dealer - 1))
#         else:
#             if observationMS.dealer_hand.cards[0].rank == Rank.ACE:
#                 code = int('%d%d' % (self.player, 0))
#             else:
#                 if self.dealer >= 17:
#                     code = int('%d%d' % (self.player, 17))
#                 else:
#                     code = int('%d%d' % (self.player, self.dealer - 1))
#     if self.usableAce == 1:
#         if self.player == 17:
#
#             if observationMS.dealer_hand.cards[0].rank == Rank.ACE:
#                 code = int('%d%d' % (27, 0))
#             elif self.dealer >= 17:
#                 code = int('%d%d' % (17, 17))
#             else:
#                 code = int('%d%d' % (27, self.dealer - 1))
#         if self.player >= 18:
#             if observationMS.dealer_hand.cards[0].rank == Rank.ACE:
#                 code = int('%d%d' % (28, 0))
#             elif self.dealer >= 17:
#                 code = int('%d%d' % (17, 17))
#             else:
#                 code = int('%d%d' % (28, self.dealer - 1))
#
#         elif self.player >= 6:
#             if observationMS.dealer_hand.cards[0].rank == Rank.ACE:
#                 code = int('%d%d' % (10, 0))
#             elif self.dealer >= 17:
#                 code = int('%d%d' % (17, 17))
#             else:
#                 code = int('%d%d' % (10, self.dealer - 1))
#
#     try:
#         return code
#     except ValueError:
#         print('oops')
#         print(str(observationMS.dealer_hand.cards[0].rank.name))
#         return ('oops')
#
#
# def get_q_value(self, observation: BlackjackObservation, action: int) -> float:
#     """
#     Implement this method so that I can test your code. This method is supposed to return your learned Q value for
#     particular observation and action.
#
#     :param observation: The observation as in the game. Contains information about what the player sees - player's
#     hand and dealer's hand.
#     :param action: Action for Q-value.
#     :return: The learned Q-value for the given observation and action.
#
#     """
#     pass

from collections import defaultdict

import itertools


class Agent:
    """
    The API for the Agent is the following:

    The method receiveSample(cards) is called on the agent infroming which cards have been dealt.
    It should return the number of the player which has won according to the Agent's hypothesis.

    Then the method receiveReward(reward) is called informing the agent whether the answer was correct or not.
    reward = 1 for correct answer and 0 for incorrect. The method receiveReward() should return a boolean value
    indicating whether more samples are desired
    """

    def __init__(self):
        # Initialize your hypothesis.
        # 0 == False, 1 == True
        #  Domain: Two Players
        self.player_1 = 0
        self.player_2 = 1

        # LABEL SET
        self.winner = 1
        self.dimension = 32
        self.iteration = 0
        self.pos_lits = list(range(16))
        self.neg_lits = list(range(100, 116))
        self.combinations = list(self.pos_lits + self.neg_lits)
        prep = list(itertools.combinations_with_replacement(self.combinations, 2))
        self.hypothesis = []
        for each in prep:
            self.hypothesis.append(list(each))

        self.last_observation = defaultdict(list)

        self.prev_cards = None
        self.prev_mistake = []

        self.correct = 0
        # self.max = self.learnability(self.hypothesis)


    def receiveSample(self, cards):
        # Do something with dealt cards.
        # Return the number of player that you expect to have won.
        # Hearts Bells Acorns Leaves // 7, 8, 9, 10, Unter, Ober, King, Ace // 0-32
        self.winner = 1

        self.prev_cards = cards

        eval = []
        for each in cards:
            if each[1] == 0:
                # Player One does have a card
                eval.append(int(each[0]))

            if each[1] == 1:
                # Player Two does have a card
                eval.append(int(each[0]) + 8)

        self.last_observation = eval
        for comb in self.hypothesis:
            count = 0
            for both in comb:
                if both <= 15:
                    if both in self.last_observation:
                        count += 1
                        continue

                elif both >= 100:
                    if both - 100 not in self.last_observation:
                        count += 1
                        continue

            if count == 0:
                self.winner = 0
        return self.winner


    # def learnability(self, hypothesis):
    #     epsilon = 0.1
    #     lamb = 0.1
    #     lnH = float("{0:.2f}".format(np.log((2**(64))/lamb)))
    #     m = (1/epsilon) * (lnH)
    #
    #     return m

    def receiveReward(self, reward):
        # Update your hypothesis according to the reward.
        self.iteration += 1
        if reward == 0:
            self.correct += 1

        if self.iteration == 725:
            return False

        if reward == -1:
            self.correct = 0
            assert (self.iteration != 0), "No last observation. Negative first reward?"

            for each in list(self.hypothesis):
                count = 0
                for both in each:
                    if both <= 15:
                        if both in self.last_observation:
                            count += 1
                            continue
                    elif both >= 100:
                        if both - 100 not in self.last_observation:
                            count += 1
                            continue

                if count == 0:
                    del self.hypothesis[self.hypothesis.index(each)]

        return self.iteration < 10000

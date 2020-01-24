import os

import constant
from player import Player
from shoe import Shoe


class Blackjack:
    def play(self):
        self.shoe = Shoe(1)
        self.dealer = Player()
        self.player = Player()
        while True:
            self.play_round()

    def __str__(self):
        return str(self.dealer) + os.linesep + str(self.player)

    def play_round(self):
        self.deal()
        while True:
            print(self)
            if not self.player.act(self.shoe):
                print(self)
                break

        self.shoe.collect(self.dealer.dispose() + self.player.dispose())
        input()

    def deal(self):
        self.player.hit(self.shoe.draw())
        self.dealer.hit(self.shoe.draw(), True)
        self.player.hit(self.shoe.draw())
        self.dealer.hit(self.shoe.draw())

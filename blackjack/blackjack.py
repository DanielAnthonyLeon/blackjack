import os

import constant
from dealer import Dealer
from player import Player
from shoe import Shoe


class Blackjack:
    def play(self):
        self.shoe = Shoe(1)
        self.dealer = Dealer()
        self.player = Player()
        while True:
            self.round()

    def __str__(self):
        return str(self.dealer) + os.linesep + str(self.player)

    def round(self):
        self.deal()
        while True:
            print(self)
            action = input("action: ")
            if action == constant.HIT:
                self.player.hit(self.shoe.draw())
            elif action == constant.STAND:
                break

        self.shoe.collect(self.dealer.dispose() + self.player.dispose())
        input()

    def deal(self):
        self.player.hit(self.shoe.draw())
        self.dealer.hit(self.shoe.draw())
        self.player.hit(self.shoe.draw())
        self.dealer.hit(self.shoe.draw())

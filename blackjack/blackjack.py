import os

from dealer import Dealer
from player import Player
from shoe import Shoe


class Blackjack:
    def play(self):
        self.shoe = Shoe(1)
        self.dealer = Dealer()
        self.player = Player()
        while True:
            self.deal()
            print(self)

    def __str__(self):
        return str(self.dealer) + os.linesep + str(self.player)

    def deal(self):
        self.player.hit(self.shoe.draw())
        self.dealer.hit(self.shoe.draw())
        self.player.hit(self.shoe.draw())
        self.dealer.hit(self.shoe.draw())

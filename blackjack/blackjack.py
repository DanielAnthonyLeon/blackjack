import os

from action import Action
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
        print(self)
        input()
        self.shoe.collect(self.dealer.dispose() + self.player.dispose())

    def deal(self):
        self.player.hit(self.shoe.draw())
        self.dealer.hit(self.shoe.draw())
        self.player.hit(self.shoe.draw())
        self.dealer.hit(self.shoe.draw())

    def action(self):
        print("actions: " + ", ".join(x.value for x in Action))

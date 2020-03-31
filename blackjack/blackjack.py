import os

import constant
from dealer import Dealer
from player import Player
from shoe import Shoe


class Blackjack:
    def play(self):
        self.dealer = Dealer()
        self.player = Player()
        while True:
            self.play_round()

    def __str__(self):
        return str(self.dealer) + os.linesep + str(self.player)

    def play_round(self):
        self.dealer.deal(self.player)
        while True:
            print(self)
            if not self.act():
                print(self)
                break

        self.dealer.collect(self.player.dispose())
        input()

    def act(self):
        action = input("action: ")
        if action == constant.HIT:
            self.dealer.hit(self.player)
        elif action == constant.STAND:
            return False

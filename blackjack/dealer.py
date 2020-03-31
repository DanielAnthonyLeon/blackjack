from player import Player
from shoe import Shoe


class Dealer(Player):
    def __init__(self):
        super().__init__()
        self._shoe = Shoe(1)

    def hit(self, player, facedown=False):
        card = self._shoe.draw()
        card.facedown = facedown
        player.receive(card)

    def collect(self, cards):
        self._shoe.receive(self.dispose() + cards)

    def deal(self, player):
        self.hit(player)
        self.hit(self)
        self.hit(player)
        self.hit(self)

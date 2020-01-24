import constant
from hand import Hand


class Player:
    def __init__(self):
        self.hand = Hand()

    def __str__(self):
        return str(self.hand)

    def hit(self, card, facedown=False):
        self.hand.hit(card)
        card.facedown = facedown

    def dispose(self):
        cards = self.hand.cards
        self.hand = Hand()
        return cards

    def act(self, shoe):
        action = input("action: ")
        if action == constant.HIT:
            self.hit(shoe.draw())
            return self.hand.value < constant.WIN_VALUE
        elif action == constant.STAND:
            return False

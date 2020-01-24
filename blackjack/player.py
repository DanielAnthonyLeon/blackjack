from hand import Hand


class Player:
    def __init__(self):
        self.hand = Hand()

    def __str__(self):
        return str(self.hand)

    def hit(self, card):
        self.hand.hit(card)

    def dispose(self):
        cards = self.hand.cards
        self.hand = Hand()
        return cards

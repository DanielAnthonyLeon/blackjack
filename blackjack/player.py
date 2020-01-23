from hand import Hand


class Player:
    def __init__(self):
        self._hand = Hand()

    def __str__(self):
        return str(self._hand)

    def hit(self, card):
        self._hand.hit(card)

    def dispose(self):
        cards = self._hand.cards
        self._hand = Hand()
        return cards

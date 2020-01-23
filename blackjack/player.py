from hand import Hand


class Player:
    def __init__(self):
        self._hand = Hand()

    def __str__(self):
        return str(self._hand)

    def deal(self, card):
        self._hand.deal(card)

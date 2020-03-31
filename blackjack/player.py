import constant
from hand import Hand


class Player:
    def __init__(self):
        self._hand = Hand()

    def __str__(self):
        return str(self._hand)

    def dispose(self):
        return self._hand.dispose()

    def receive(self, card):
        self._hand.receive(card)

    def under(self):
        self._hand.value < constant.WIN_VALUE

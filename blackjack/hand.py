import constant
from face import Face


class Hand:
    def __init__(self):
        self._cards = []

    def __str__(self):
        return " ".join(str(x) for x in self._cards) + " -> " + str(self.value)

    @property
    def value(self):
        value = sum(x.value for x in self._cards)
        if value > constant.WIN_VALUE:
            for ace in [x for x in self._cards if x.face == Face.ACE]:
                value -= ace.value - constant.ALT_ACE_VALUE
                if value <= constant.WIN_VALUE:
                    return value

        return value

    def receive(self, card):
        self._cards.append(card)

    def dispose(self):
        cards, self._cards = self._cards, []
        return cards

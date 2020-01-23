import constant
from face import Face


class Hand:
    def __init__(self):
        self._cards = []

    @property
    def value(self):
        value = sum(x.value for x in self._cards)
        if value > constant.WIN_VALUE:
            for ace in [x for x in self._cards if x.face == Face.ACE]:
                value -= ace.value - constant.ALT_ACE_VALUE
                if value <= constant.WIN_VALUE:
                    return value

        return value

    def deal(self, card):
        self._cards.append(card)

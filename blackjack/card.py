import constant
from face import Face
from suit import Suit


class Card:
    def __init__(self, face, suit=Suit.SPADES, visible=True):
        self.face = face
        self.suit = suit
        self._visible = visible

    def __str__(self):
        if not self._visible:
            return "__"

        return self.suit.value + self.face.value

    @property
    def value(self):
        if not self._visible:
            return 0

        return constant.CARD_VALUES[self.face]

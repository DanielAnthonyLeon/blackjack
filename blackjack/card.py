import constant
from face import Face
from suit import Suit


class Card:
    def __init__(self, face, suit=Suit.SPADES):
        self.face = face
        self.suit = suit
        self.facedown = False

    def __str__(self):
        if self.facedown:
            return "__"

        return self.suit.value + self.face.value

    @property
    def value(self):
        if self.facedown:
            return 0

        return constant.CARD_VALUES[self.face]

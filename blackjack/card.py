import constant
from face import Face
from suit import Suit


class Card:
    def __init__(self, face, suit=Suit.SPADES, visible=False):
        self.face = face
        self.suit = suit
        self.visible = visible

    def __str__(self):
        if not self.visible:
            return "🂠"

        return constant.CARD_CHARS[self.suit, self.face]

    @property
    def value(self):
        return constant.CARD_VALUES[self.face]

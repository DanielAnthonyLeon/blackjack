from enum import auto, Enum
import sys


class Card:
    class Face(Enum):
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10
        JACK = 10
        QUEEN = 10
        KING = 10
        ACE = 11

    class Suit(Enum):
        CLUBS = auto()
        DIAMONDS = auto()
        HEARTS = auto()
        SPADES = auto()

    def __init__(self, face, suit, visible):
        self.face = face
        self.suit = suit
        self.visible = visible
        self.value = self.face.value

    def __str__(self):
        if not self.visible:
            return "🂠"

        if self.suit == Card.Suit.SPADES:
            if self.face == Card.Face.ACE:
                return "🂡"
            elif self.face == Card.Face.TWO:
                return "🂢"
            elif self.face == Card.Face.THREE:
                return "🂣"
            elif self.face == Card.Face.FOUR:
                return "🂤"
            elif self.face == Card.Face.FIVE:
                return "🂥"
            elif self.face == Card.Face.SIX:
                return "🂦"
            elif self.face == Card.Face.SEVEN:
                return "🂧"
            elif self.face == Card.Face.EIGHT:
                return "🂨"
            elif self.face == Card.Face.NINE:
                return "🂩"
            elif self.face == Card.Face.TEN:
                return "🂪"
            elif self.face == Card.Face.JACK:
                return "🂫"
            elif self.face == Card.Face.QUEEN:
                return "🂭"
            elif self.face == Card.Face.KING:
                return "🂮"
        elif self.suit == Card.Suit.HEARTS:
            if self.face == Card.Face.ACE:
                return "🂱"
            elif self.face == Card.Face.TWO:
                return "🂲"
            elif self.face == Card.Face.THREE:
                return "🂳"
            elif self.face == Card.Face.FOUR:
                return "🂴"
            elif self.face == Card.Face.FIVE:
                return "🂵"
            elif self.face == Card.Face.SIX:
                return "🂶"
            elif self.face == Card.Face.SEVEN:
                return "🂷"
            elif self.face == Card.Face.EIGHT:
                return "🂸"
            elif self.face == Card.Face.NINE:
                return "🂹"
            elif self.face == Card.Face.TEN:
                return "🂺"
            elif self.face == Card.Face.JACK:
                return "🂻"
            elif self.face == Card.Face.QUEEN:
                return "🂽"
            elif self.face == Card.Face.KING:
                return "🂾"
        elif self.suit == Card.Suit.DIAMONDS:
            if self.face == Card.Face.ACE:
                return "🃁"
            elif self.face == Card.Face.TWO:
                return "🃂"
            elif self.face == Card.Face.THREE:
                return "🃃"
            elif self.face == Card.Face.FOUR:
                return "🃄"
            elif self.face == Card.Face.FIVE:
                return "🃅"
            elif self.face == Card.Face.SIX:
                return "🃆"
            elif self.face == Card.Face.SEVEN:
                return "🃇"
            elif self.face == Card.Face.EIGHT:
                return "🃈"
            elif self.face == Card.Face.NINE:
                return "🃉"
            elif self.face == Card.Face.TEN:
                return "🃊"
            elif self.face == Card.Face.JACK:
                return "🃋"
            elif self.face == Card.Face.QUEEN:
                return "🃍"
            elif self.face == Card.Face.KING:
                return "🃎"
        elif self.suit == Card.Suit.CLUBS:
            if self.face == Card.Face.ACE:
                return "🃑"
            elif self.face == Card.Face.TWO:
                return "🃒"
            elif self.face == Card.Face.THREE:
                return "🃓"
            elif self.face == Card.Face.FOUR:
                return "🃔"
            elif self.face == Card.Face.FIVE:
                return "🃕"
            elif self.face == Card.Face.SIX:
                return "🃖"
            elif self.face == Card.Face.SEVEN:
                return "🃗"
            elif self.face == Card.Face.EIGHT:
                return "🃘"
            elif self.face == Card.Face.NINE:
                return "🃙"
            elif self.face == Card.Face.TEN:
                return "🃚"
            elif self.face == Card.Face.JACK:
                return "🃛"
            elif self.face == Card.Face.QUEEN:
                return "🃝"
            elif self.face == Card.Face.KING:
                return "🃞"

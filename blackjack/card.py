from face import Face
from suit import Suit


class Card:
    def __init__(self, face, suit, visible=False):
        self.face = face
        self.suit = suit
        self.visible = visible

    def __str__(self):
        if not self.visible:
            return "🂠"

        if self.suit == Suit.SPADES:
            if self.face == Face.ACE:
                return "🂡"
            elif self.face == Face.TWO:
                return "🂢"
            elif self.face == Face.THREE:
                return "🂣"
            elif self.face == Face.FOUR:
                return "🂤"
            elif self.face == Face.FIVE:
                return "🂥"
            elif self.face == Face.SIX:
                return "🂦"
            elif self.face == Face.SEVEN:
                return "🂧"
            elif self.face == Face.EIGHT:
                return "🂨"
            elif self.face == Face.NINE:
                return "🂩"
            elif self.face == Face.TEN:
                return "🂪"
            elif self.face == Face.JACK:
                return "🂫"
            elif self.face == Face.QUEEN:
                return "🂭"
            elif self.face == Face.KING:
                return "🂮"
        elif self.suit == Suit.HEARTS:
            if self.face == Face.ACE:
                return "🂱"
            elif self.face == Face.TWO:
                return "🂲"
            elif self.face == Face.THREE:
                return "🂳"
            elif self.face == Face.FOUR:
                return "🂴"
            elif self.face == Face.FIVE:
                return "🂵"
            elif self.face == Face.SIX:
                return "🂶"
            elif self.face == Face.SEVEN:
                return "🂷"
            elif self.face == Face.EIGHT:
                return "🂸"
            elif self.face == Face.NINE:
                return "🂹"
            elif self.face == Face.TEN:
                return "🂺"
            elif self.face == Face.JACK:
                return "🂻"
            elif self.face == Face.QUEEN:
                return "🂽"
            elif self.face == Face.KING:
                return "🂾"
        elif self.suit == Suit.DIAMONDS:
            if self.face == Face.ACE:
                return "🃁"
            elif self.face == Face.TWO:
                return "🃂"
            elif self.face == Face.THREE:
                return "🃃"
            elif self.face == Face.FOUR:
                return "🃄"
            elif self.face == Face.FIVE:
                return "🃅"
            elif self.face == Face.SIX:
                return "🃆"
            elif self.face == Face.SEVEN:
                return "🃇"
            elif self.face == Face.EIGHT:
                return "🃈"
            elif self.face == Face.NINE:
                return "🃉"
            elif self.face == Face.TEN:
                return "🃊"
            elif self.face == Face.JACK:
                return "🃋"
            elif self.face == Face.QUEEN:
                return "🃍"
            elif self.face == Face.KING:
                return "🃎"
        elif self.suit == Suit.CLUBS:
            if self.face == Face.ACE:
                return "🃑"
            elif self.face == Face.TWO:
                return "🃒"
            elif self.face == Face.THREE:
                return "🃓"
            elif self.face == Face.FOUR:
                return "🃔"
            elif self.face == Face.FIVE:
                return "🃕"
            elif self.face == Face.SIX:
                return "🃖"
            elif self.face == Face.SEVEN:
                return "🃗"
            elif self.face == Face.EIGHT:
                return "🃘"
            elif self.face == Face.NINE:
                return "🃙"
            elif self.face == Face.TEN:
                return "🃚"
            elif self.face == Face.JACK:
                return "🃛"
            elif self.face == Face.QUEEN:
                return "🃝"
            elif self.face == Face.KING:
                return "🃞"

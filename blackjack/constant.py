from face import Face
from suit import Suit

CARD_VALUES = {Face.TWO: 2, Face.THREE: 3, Face.FOUR: 4, Face.FIVE: 5, Face.SIX: 6, Face.SEVEN: 7,
               Face.EIGHT: 8, Face.NINE: 9, Face.TEN: 10, Face.JACK: 10, Face.QUEEN: 10, Face.KING: 10, Face.ACE: 11}

CARD_CHARS = {
    Suit.SPADES: {
        Face.ACE: "🂡", Face.TWO: "🂢", Face.THREE: "🂣", Face.FOUR: "🂤", Face.FIVE: "🂥", Face.SIX: "🂦", Face.SEVEN: "🂧", Face.EIGHT: "🂨", Face.NINE: "🂩", Face.TEN: "🂪", Face.JACK: "🂫", Face.QUEEN: "🂭", Face.KING: "🂮"},
    Suit.HEARTS: {
        Face.ACE: "🂱", Face.TWO: "🂲", Face.THREE: "🂳", Face.FOUR: "🂴", Face.FIVE: "🂵", Face.SIX: "🂶", Face.SEVEN: "🂷", Face.EIGHT: "🂸", Face.NINE: "🂹", Face.TEN: "🂺", Face.JACK: "🂻", Face.QUEEN: "🂽", Face.KING: "🂾"},
    Suit.DIAMONDS: {
        Face.ACE: "🃁", Face.TWO: "🃂", Face.THREE: "🃃", Face.FOUR: "🃄", Face.FIVE: "🃅", Face.SIX: "🃆", Face.SEVEN: "🃇", Face.EIGHT: "🃈", Face.NINE: "🃉", Face.TEN: "🃊", Face.JACK: "🃋", Face.QUEEN: "🃍", Face.KING: "🃎"},
    Suit.CLUBS: {
        Face.ACE: "🃑", Face.TWO: "🃒", Face.THREE: "🃓", Face.FOUR: "🃔", Face.FIVE: "🃕", Face.SIX: "🃖", Face.SEVEN: "🃗", Face.EIGHT: "🃘", Face.NINE: "🃙", Face.TEN: "🃚", Face.JACK: "🃛", Face.QUEEN: "🃝", Face.KING: "🃞"}}

ALT_ACE_VALUE = 1
WIN_VALUE = 21

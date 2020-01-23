import random

from card import Card
from face import Face
from suit import Suit


class Shoe:
    def __init__(self, num_decks):
        self.cards = []
        for face in Face:
            for suit in Suit:
                self.cards += num_decks * [Card(face, suit)]

    def draw(self):
        return self.cards.pop(random.randint(0, len(self.cards) - 1))

    def collect(self, cards):
        self.cards += cards

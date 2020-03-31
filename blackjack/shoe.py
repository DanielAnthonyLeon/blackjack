import random

from card import Card
from face import Face
from suit import Suit


class Shoe:
    def __init__(self, num_decks):
        self._cards = []
        for face in Face:
            for suit in Suit:
                self._cards += num_decks * [Card(face, suit)]

    def draw(self):
        return self._cards.pop(random.randint(0, len(self._cards) - 1))

    def receive(self, cards):
        self._cards += cards

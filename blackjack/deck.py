from card import Card
import random


class Deck:
    def __init__(self, num_decks):
        self.cards = []
        for face in Card.Face:
            for suit in Card.Suit:
                self.cards += num_decks * [Card(face, suit)]

    def draw(self):
        return self.cards.pop(random.randint(0, len(self.cards) - 1))

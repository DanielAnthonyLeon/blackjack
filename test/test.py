import unittest

import init
from card import Card
from deck import Deck
from face import Face


class Test(unittest.TestCase):
    def test_four_of_each_face(self):
        deck = Deck(1)
        for face in Face:
            self.assertEqual(len([x for x in deck.cards if x.face == face]), 4)

    def test_deal(self):
        deck = Deck(1)
        self.assertEqual(len(deck.cards), 52)
        card1 = deck.draw()
        card2 = deck.draw()
        self.assertEqual(len(deck.cards), 50)
        self.assertNotIn(card1, deck.cards)
        self.assertNotIn(card2, deck.cards)
        deck.collect([card1, card2])
        self.assertEqual(len(deck.cards), 52)


if __name__ == "__main__":
    unittest.main()

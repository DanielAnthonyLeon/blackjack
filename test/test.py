import unittest

import init
from card import Card
from face import Face
from hand import Hand
from shoe import Shoe


class Test(unittest.TestCase):
    def test_four_of_each_face(self):
        shoe = Shoe(1)
        for face in Face:
            self.assertEqual(len([x for x in shoe._cards if x.face == face]), 4)

    def test_deal(self):
        shoe = Shoe(1)
        self.assertEqual(len(shoe._cards), 52)
        card1 = shoe.draw()
        card2 = shoe.draw()
        self.assertEqual(len(shoe._cards), 50)
        self.assertNotIn(card1, shoe._cards)
        self.assertNotIn(card2, shoe._cards)
        shoe.receive([card1, card2])
        self.assertEqual(len(shoe._cards), 52)

    def test_hand_value(self):
        hand = Hand()
        hand.receive(Card(Face.THREE))
        self.assertEqual(hand.value, 3)
        hand.receive(Card(Face.ACE))
        self.assertEqual(hand.value, 14)
        hand.receive(Card(Face.ACE))
        self.assertEqual(hand.value, 15)
        hand.receive(Card(Face.JACK))
        self.assertEqual(hand.value, 15)
        hand.receive(Card(Face.ACE))
        self.assertEqual(hand.value, 16)


if __name__ == "__main__":
    unittest.main()

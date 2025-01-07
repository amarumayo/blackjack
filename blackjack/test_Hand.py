from classes import Hand, Card
import unittest

class TestHand(unittest.TestCase):
    def test_has_blackjack(self):
        hand_1 = Hand(is_dealer = False)  
        hand_1.cards = [Card("A", "Spades"), Card("10", "Clubs")]
        self.assertTrue(hand_1.has_blackjack())

if __name__ == "__main__":
    unittest.main()


# # test that a black jack is not detected with 3 cards that equal 21
# player = Hand(is_dealer = False)    
# player.cards = [Card("A", "Spades"), Card("8", "Clubs"), Card("2", "clubs")]
# player.value
# player.has_blackjack()

# # test that a black jack is not detected with 2 cards that do not equal 21
# player = Hand(is_dealer = False)    
# player.cards = [Card("A", "Spades"), Card("8", "Clubs")]
# player.value
# player.has_blackjack()

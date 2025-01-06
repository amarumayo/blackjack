
import pdb
import random

class Card:
# card class
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
    def __repr__(self):
        rep = "_".join((str(self.rank), self.suit))
        return(rep)
       


class Deck():
    def __init__(self):
        self.cards = []

    def fill_deck(self):
        suits = ["C", "D", "S", "H"]    
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(r, s) for r in ranks for s in suits]
        
    def clear_deck(self):
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return(self.cards.pop())


class Hand:

    def __init__(self, is_dealer):
        self.cards = []
        self.is_dealer = is_dealer

    def add_card(self, card):
        self.cards.append(card)

    def clear_hand(self):
        self.cards = []

    def has_blackjack(self):
        blackjack = False
        if len(self.cards) == 2 and self.value == 21:
            blackjack = True
        return(blackjack)



    @property
    def value(self):
        '''Calculate the value of the cards in a hand instance'''
        val = 0
        num_aces = 0

        for card in self.cards:
            if card.rank.isnumeric():
                val += int(card.rank)
            elif card.rank == "A":
                num_aces += 1
                val += 11
            else:
                val += 10
        while num_aces > 0 and val > 21:
            val -= 10
            num_aces -= 1

        return val


card = Card("5", "C")

deck = Deck()
deck.fill_deck()
deck.shuffle()
deck.cards[1]



# test Hand.has_blackjack method
# test that a black jack is detected
player = Hand(is_dealer = False)    
player.cards = [Card("A", "Spades"), Card("10", "Clubs")]
player.value
player.has_blackjack()

# test that a black jack is not detected with 3 cards that equal 21
player = Hand(is_dealer = False)    
player.cards = [Card("A", "Spades"), Card("8", "Clubs"), Card("2", "clubs")]
player.value
player.has_blackjack()

# test that a black jack is not detected with 2 cards that do not equal 21
player = Hand(is_dealer = False)    
player.cards = [Card("A", "Spades"), Card("8", "Clubs")]
player.value
player.has_blackjack()


dealer = Hand(is_dealer = True)



player.add_card(deck.deal())
dealer.add_card(deck.deal())

player.cards 
dealer.cards
player.value

class Game:
    deck = Deck()
    deck.fill_deck()
    deck.shuffle()
    deck.clear_deck()
    x = deck.deal()
    print("hi")


game = Game()

deck = Deck()
deck.fill_deck()
deck.shuffle()
len(deck.cards)


import random
from classes import Card, Hand, Deck, Game

# create a card
test_card = Card('A', 'D')
print(test_card)
repr(test_card)
str(test_card)

# create a test dealer and player hand
test_deck = Deck()
print(test_deck)
print(test_deck.deal())

test_deck.fill_deck()
test_deck.shuffle()
print(test_deck)



player = Hand(is_dealer = False)
player.cards.append(Card("A", "D"))
print(player)
print(player.cards)

print(player.cards[0])
player.cards.append(Card("5", "D"))
dealer = Hand(is_dealer = True)
dealer.cards.append(Card("10", "D"))
dealer.cards.append(Card("15", "D"))
hands = [dealer, player]

blackjack = [hand.has_blackjack() for hand in hands]
high = [hand.value for hand in hands]
high = [score == max(high) for score in high]
bust = [hand.is_bust for hand in hands]

blackjack
high
bust

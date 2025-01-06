# tests

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

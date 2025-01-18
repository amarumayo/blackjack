
import random
import sys

class Card:
    # card classes 53w5
    def __init__(self, rank, suit):

        if rank not in [
            '1', '2', '3', '4', '5', '6',
            '7', '8', '9', '10', 'A', 'J', 'Q', 'K', 'X']:
                raise ValueError("Invalid rank")

        valid_suits = ['D', 'S', 'C', 'H', 'X']
        if suit not in valid_suits:
            raise ValueError(f"Invalid suit. Valid suits are {valid_suits}")

        self.suit = suit
        self.rank = rank

    # unicode value to print suit symbols
    suit_lu = {
        "C": "\u2663",
        "H": "\u2665",
        "D": "\u2666",
        "S": "\u2660"
    }    
    def __repr__(self):
        string = "".join((str(self.rank), self.suit_lu[self.suit]))
        return(string)

    # def __repr__(self):
    #     rep = "Card({}, {})".format(self.rank, self.suit)
    #     return(rep)    


       
class Deck():
    def __init__(self):
        self.cards = []
        self.fill_deck()
        self.shuffle()

    def fill_deck(self):
        self.clear_deck()
        suits = ["C", "D", "S", "H"]    
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(r, s) for r in ranks for s in suits]
        
    def clear_deck(self):
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return(self.cards.pop(0))

    def __repr__(self):
        rep = "Deck({})".format(self.cards)
        return(rep)

    def __str__(self):
        info = f"{str(len(self.cards))} cards remaining in the deck"
        first_card = f"next card is {str(self.cards[0])}"

        return(info + '\n' + first_card)


class Hand:

    def __init__(self, is_dealer):
        self.cards = []
        self.is_dealer = is_dealer

    def add_card(self, card):
        self.cards.append(card)

    def clear_hand(self):
        self.cards = []

    @property
    def has_blackjack(self):
        blackjack = False
        if len(self.cards) == 2 and self.value == 21:
            blackjack = True
        return(blackjack)

    @property
    def is_bust(self):
        bust = False
        if self.value > 21:
            bust = True
        return(bust)

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

    def show_hand(self, dealer_hide = False):
        
        if (self.is_dealer and dealer_hide):
            dealer_display = self.cards[:] 
            dealer_display[0] = Card('X', 'X')
            print(f"Dealer: {str(dealer_display)}")
        elif (self.is_dealer and not dealer_hide):
            print(f"Dealer: {str(self.cards)}")
        elif(not self.is_dealer):
            print(f"Player: {str(self.cards)}")

    def message_hand_win(self):
        if self.is_dealer:
            print("Dealer wins!")
        elif not self.is_dealer:
            print("Player wins!")


class Game:
    
    def __init__(self):
        self.hands = []
        self.deck = []
        self.player_turn = True

    def check_winner(self):
        pass

    def end(self):
        print("Goodbye")
        sys.exit()


    def play(self):
        # self = Game()
        self.deck = Deck()
        self.deck.fill_deck()
        self.deck.shuffle()

        player = Hand(is_dealer = False)
        dealer = Hand(is_dealer = True)
        self.hands = [player, dealer]

        # deal 2 cards to each player
        for i in range(2):
            for p in self.hands:
                # p = player
                p.add_card(self.deck.deal())

        dealer.show_hand()
        player.show_hand()

        # check for any blackjacks
        if dealer.has_blackjack:
            print('Blackjack!')
            dealer.message_hand_win()
            self.end()
 
        if player.has_blackjack and not dealer.has_blackjack:
            print('Blackjack!')
            player.message_hand_win()
            self.end()



        # deck = Deck()
        # deck.fill_deck()
        # deck.shuffle()

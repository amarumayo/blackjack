
import random
import sys
import time

class Card:
    # card class
    def __init__(self, rank, suit):

        if rank not in [
            '1', '2', '3', '4', '5', '6',
            '7', '8', '9', '10', 'A', 'J', 'Q', 'K']:
                raise ValueError("Invalid rank")

        valid_suits = ['D', 'S', 'C', 'H']
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
    def __str__(self):
        string = "".join((str(self.rank), self.suit_lu[self.suit]))
        return(string)

    def __repr__(self):
        rep = "Card({}, {})".format(self.rank, self.suit)
        return(rep)    


       
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

    def __init__(self, is_dealer, is_active = False):
        self.cards = []
        self.is_dealer = is_dealer
        self.is_active = is_active

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

    def player_choice(self, deck):
        '''Prompt player to hit or stand with a hand instance'''

        answer = ''
        while answer not in ['h', 's']:
            answer = input("Hit or Stand? H/S: ")
            if answer.lower() == "h":
                self.add_card(deck.deal())
            if answer.lower() == "s":
                print(f"Player stands with hand of {str(self.value)}\n")
                self.is_active = False
    
    def __str__(self):
        n_cards = f"number of cards: {len(self.cards)}"
        hand_value = f"hand value: {str(self.value)}"
        is_dealer = f"is dealer: {str(self.is_dealer)}"
        is_active = f"is active: {str(self.is_active)}"

        return(n_cards + '\n' + hand_value + '\n' + is_dealer + '\n' + is_active)

    def __repr__(self):
        rep = "Hand({}, {}, {})".format(self.cards, self.is_dealer, self.is_active)
        return(rep)


class Game:
    
    def __init__(self):
        self.hands = []
        self.deck = []
        self.player_turn = True

    def check_winner(self):
        #list(map())
        # print("here")

        # for i in self.hands:
        #     print(i.value)
        pass

    def end(self):
        print("Goodbye")
        sys.exit()

    
    def play(self):
        # self = Game()
        self.deck = Deck()
        self.deck.fill_deck()
        self.deck.shuffle()

        player = Hand(is_dealer = False, is_active = True)
        dealer = Hand(is_dealer = True)
        self.hands = [player, dealer]

        # deal 2 cards to each player
        for i in range(2):
            for p in self.hands:
                # p = player
                p.add_card(self.deck.deal())


        # check for any blackjacks
        if dealer.has_blackjack:
            player.show_hand()
            dealer.show_hand()
            print('Blackjack!')
            dealer.message_hand_win()
            self.end()
 
        if player.has_blackjack and not dealer.has_blackjack:
            player.show_hand()
            dealer.show_hand()
            print('Blackjack!')
            player.message_hand_win()
            self.end()


        dealer.show_hand(dealer_hide = True)

        while player.is_active:
            player.show_hand()

            player.player_choice(deck = self.deck)

            if player.is_bust:
                print("Player busts. You lose!")
                player.is_active = False
                self.end()
        
        # dealer turn
        dealer.is_active = True

        while dealer.is_active:

            while dealer.value <= 16:
                
                print("Dealer Hits")
                dealer.add_card(self.deck.deal())
                dealer.show_hand()
                time.sleep(2)

                if dealer.is_bust:
                    print("Dealer busts. You win!")
                    dealer.is_active = False
                    self.end()
            
            dealer.is_active = False
            print(print(f"Dealer stands with hand of {str(dealer.value)}\n"))

             
#TODO add messages that say dealer (and player) hits with 14


        # deck = Deck()
        # deck.fill_deck()
        # deck.shuffle()

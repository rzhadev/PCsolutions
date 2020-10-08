import random
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def __str__(self):
        deck_content = ''
        count = 0
        for card in self.deck:
            count = count + 1
            deck_content += '\n' + card.__str__() + f':{count}'
        return 'The deck has: ' + deck_content

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.values = self.values - 10
            self.aces = self.aces - 1


class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def show_chips(self):
        print(f'you currently have {self.total} chips')


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How much would you like to bet? :'))
        except ValueError:
            print('please input a valid amount')
        else:
            if chips.bet > chips.total:
                print('Sorry, you have exceeded your chip total')
            else:
                break


def hit(deck, hand):
    hand.add_cards(deck.deal())
    hand.adjust_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        answer = input('Do you want to hit or stand?: type hit or stand :')
        if answer.lower() == 'hit':
            hit(deck, hand)
        elif answer.lower() == 'stand':
            print('player stands, dealer is playing')
            playing = False
        else:
            print('try again')
            continue
        break


def show_cards(hand, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *hand.cards, sep='\n ')
    print("Player's Hand =", hand.value)


def show_all(hand, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *hand.cards, sep='\n ')
    print("Player's Hand =", hand.value)


def player_bust(player, dealer, chips):
    print('player busts')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('player wins')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('dealer busts')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('dealer wins')
    chips.lose_bet()


def push(player, dealer):
    print('player and dealer tie')


while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())
    player_chips = Chips()
    player_chips.show_chips()
    take_bet(player_chips)
    show_cards(player_hand, dealer_hand)
    while playing:
        hit_or_stand(deck, player_hand)
        show_cards(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        show_all(player_hand, dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
    print(f'Player winnings are currently: {player_chips.total}')
    new_game = input('Do you want to play again? Enter yes or no :')
    if new_game.lower() == 'yes':
        playing = True
        continue
    else:
        print('thanks for playing')
        break

import random
import sys

#Code to create deck of cards


class card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def showcard(self):
        if self.value <= 10:
            print(str(self.value) + ' of ' + self.suit)
        if self.value == 11:
            print('Jack' + ' of ' + self.suit)
        if self.value == 12:
            print('Queen' + ' of ' + self.suit)
        if self.value == 13:
            print('King' + ' of ' + self.suit)


class deck:
    def __init__(self):
        self.cards = []

    def construct(self):
        for suit in ['Spades', 'Diamonds', 'Clubs', 'Hearts']:
            for value in range(1, 14):
                (self.cards).append(card(value, suit))

    def shuffle(self):
        for i in range(52):
            a, b = random.randint(0, 51), random.randint(0, 51)
            self.cards[a], self.cards[b] = self.cards[b], self.cards[a]


def check_hand(hand):
    total = 0

    for cards in hand:
        if cards.value < 10:
            current_value = cards.value
        if cards.value >= 10:
            current_value = 10
        total += current_value

    if total > 21:
        return 'Broke!', total

    if total == 21:
        return 'BlackJack!', total

    return 'Clear', total


#Code to create the player hand

while True:  #The main loop

    play_req = input(f'Would you like to play? (y/n): ')

    if play_req == 'y':

        print("-" * 10)

        deck1 = deck()
        deck1.construct()
        deck1.shuffle()

        dealerhand = []
        playerhand = []
        card_taken = 0

        dealerhand.append(deck1.cards[card_taken])
        dealerhand.append(deck1.cards[card_taken + 1])

        card_taken += 2

        playerhand.append(deck1.cards[card_taken])
        playerhand.append(deck1.cards[card_taken + 1])

        card_taken += 2

        print('Your cards are: ')

        for cards in playerhand:
            cards.showcard()

        print("-" * 10)

        while True:  #Fold/Break loop
            play_req = input(
                'Would you like to put or get another card? (fold/tap): ')

            print('-' * 10)

            if play_req == 'tap':

                playerhand.append(deck1.cards[card_taken])
                card_taken += 1
                result, total = check_hand(playerhand)

                print('Your cards are: ')

                for cards in playerhand:
                    cards.showcard()

                if result == 'BlackJack!':
                    print(f'Your total is: {total}')

                print("-" * 10)

                if result == 'Broke!':
                    print(f'Broke! The dealer wins. \n {"-"*10}')
                    break

            elif play_req == 'fold':
                print('You have chosen to fold, revealing dealers hand!' +
                      '\n' + '-' * 10)

                #Code to compare to the dealer's hand

                break

            else:
                print(f'Please enter a valid input. {"-"*10}')

    #Exit code
    elif play_req == 'n':
        sys.exit()

    #Input Validation code
    else:
        print(f'Please enter a valid input. {"-"*10} ')
#Code to create the dealer hand
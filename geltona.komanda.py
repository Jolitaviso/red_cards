import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.sign = f"{rank} {suit}"
        self.weight = self.calculate_weight()

    def calculate_weight(self):
        weights = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        if self.rank in weights:
            return weights[self.rank]
        else:
            return int(self.rank)

class CardDeck:
    def __init__(self):
        ranks = [str(i) for i in range(2, 11)] + ['T', 'J', 'Q', 'K', 'A']
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def take_from_top(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            print("Deck is empty.")

    def take_from_bottom(self):
        if self.cards:
            return self.cards.pop()
        else:
            print("Deck is empty.")

    def take_random(self):
        if self.cards:
            return self.cards.pop(random.randint(0, len(self.cards)-1))
        else:
            print("Deck is empty.")

def initialize_hands():
    shared_deck = CardDeck()
    shared_deck.shuffle()

    player1_hand = CardDeck()
    player2_hand = CardDeck()

    for _ in range(28):
        player1_hand.cards.append(shared_deck.take_from_top())
        player2_hand.cards.append(shared_deck.take_from_top())

    return player1_hand, player2_hand

def play_war(player1_hand, player2_hand):
    player1_card = player1_hand.take_from_top()
    player2_card = player2_hand.take_from_top()

    print(f"\nPlayer 1 plays: {player1_card.sign}")
    print(f"Player 2 plays: {player2_card.sign}")

    if player1_card.weight > player2_card.weight:
        print("Player 1 wins the round!")
        player1_hand.cards.extend([player1_card, player2_card])
    elif player1_card.weight < player2_card.weight:
        print("Player 2 wins the round!")
        player2_hand.cards.extend([player1_card, player2_card])
    else:
        print("It's a tie!")

def print_decks(player1_hand, player2_hand):
    print(f"\nPlayer 1 Hand: {len(player1_hand.cards)} cards")
    print(f"Player 2 Hand: {len(player2_hand.cards)} cards")

def main():
    print("Welcome to the War Card Game!")
    player1_hand, player2_hand = initialize_hands()

    while True:
        user_input = input("\n1. Play the next round.\n2. Display hands.\n3. Quit.\nChoose your action: ")

        if user_input == '1':
            play_war(player1_hand, player2_hand)
        elif user_input == '3':
            print("\nThanks for playing! Goodbye!")
            break
        elif user_input == '2':
            print_decks(player1_hand, player2_hand)
        else:
            print("Invalid input. Please enter '1', '2', or '3'.")

if __name__ == "__main__":
    main()

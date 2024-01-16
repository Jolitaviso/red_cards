import random

class Card:
    def __init__(self, rank, suit, weights):
        self.rank = rank
        self.suit = suit
        self.sign = suit + rank
        self.weights = weights[rank]

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        weights = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit, weights))

    def shuffle(self):
        random.shuffle(self.cards)

    def take_from_top(self):
        return self.cards.pop() if self.cards else None
    
    def take_from_bottom(self):
        return self.cards.pop(0) if self.cards else None
    
    def take_random(self):
        return random.choice(self.cards) if self.cards else None
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self):
        return self.hand.pop(0) if self.hand else None

    def add_to_hand(self, *cards):
        self.hand.extend(cards)

    def has_cards(self):
        return bool(self.hand)

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.deck = Deck()

    def deal_initial_cards(self):
        for _ in range(5):
            self.player.add_to_hand(self.deck.take_from_top())
            self.computer.add_to_hand(self.deck.take_from_top())

    def play_round(self):
        player_card = self.player.play_card()
        computer_card = self.computer.play_card()

        print(f"\n{self.player.name}'s card:", player_card.sign)
        print("Computer's card:", computer_card.sign)

        if player_card.weights > computer_card.weights:
            print(f"{self.player.name} wins this round!")
            self.player.add_to_hand(player_card, computer_card)
        elif player_card.weights < computer_card.weights:
            print("Computer wins this round.")
            self.computer.add_to_hand(computer_card, player_card)
        else:
            print("Card values are equal. No points.")

    def play_game(self):
        print("Welcome to the War Card Game!")
        self.deck.shuffle()
        self.deal_initial_cards()

        while self.player.has_cards() and self.computer.has_cards():
            print("\n--- New Round ---")
            self.play_round()

        print("\n--- Game Over ---")
        print("Results:")
        print(f"{self.player.name}'s cards:", [card.sign for card in self.player.hand])
        print("Computer's cards:", [card.sign for card in self.computer.hand])

if __name__ == "__main__":
    player = Player("Player")
    computer = Player("Computer")
    game = Game(player, computer)
    game.play_game()

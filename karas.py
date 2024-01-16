import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.sign = suit + rank

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        return [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def take_from_top(self):
        return self.cards.pop(0)

class Game:
    def __init__(self):
        self.player_points = 0
        self.computer_points = 0
        self.deck = Deck()

    def deal_initial_cards(self):
        player_cards = [self.deck.take_from_top()]
        computer_cards = [self.deck.take_from_top()]
        return player_cards, computer_cards

    def draw_card(self):
        print("Choose where to draw a card:")
        print("1. From the top")
        print("2. From the bottom")
        print("3. Random")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            return self.deck.take_from_top()
        elif choice == '2':
            return self.deck.cards.pop()
        elif choice == '3':
            return self.deck.cards.pop(random.randint(0, len(self.deck.cards)-1))
        else:
            print("Invalid choice. Drawing from the top.")
            return self.deck.take_from_top()

    def play_round(self):
        player_card = self.draw_card()
        computer_card = self.deck.take_from_top()

        print("\nYour card:", player_card.sign)
        print("Computer's card:", computer_card.sign)

        if player_card.rank > computer_card.rank:
            print("You win this round!")
            self.player_points += 1
        elif player_card.rank < computer_card.rank:
            print("Computer wins this round.")
            self.computer_points += 1
        else:
            print("Card values are equal. No points.")

    def play_game(self):
        self.deck.shuffle()
        while len(self.deck.cards) > 1:
            print("\n--- New Round ---")
            self.play_round()

        print("\n--- Game Over ---")
        print(f"RESULTS: \nPlayer: {self.player_points}, \nComputer: {self.computer_points}")

        if self.player_points > self.computer_points:
            print("Winner: Player!")
        elif self.player_points < self.computer_points:
            print("Winner: Computer!")
        else:
            print("It's a DRAW!")

if __name__ == "__main__":
    print("Welcome to War!")
    game = Game()
    game.play_game()

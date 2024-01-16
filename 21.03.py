import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.sign = suit + rank
        self.weight = self.calculate_weight()

    def calculate_weight(self):
        if self.rank.isdigit():
            return int(self.rank)
        elif self.rank in ['T', 'J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # For simplicity, Aces are always 11

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        return [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def take_from_top(self):
        return self.cards.pop(0)

    def take_from_bottom(self):
        return self.cards.pop()

    def take_random(self):
        return self.cards.pop(random.randint(0, len(self.cards) - 1))

class Game:
    def __init__(self):
        self.deck = Deck()

    def deal_initial_cards(self):
        player_cards = [self.deck.take_from_top(), self.deck.take_from_top()]
        computer_cards = [self.deck.take_from_top(), self.deck.take_from_top()]
        return player_cards, computer_cards

    def display_hand_and_value(self, player_cards, computer_cards):
        player_value = sum(card.weight for card in player_cards)
        computer_value = sum(card.weight for card in computer_cards)

        print("\nYour hand:", [card.sign for card in player_cards])
        print("Your hand value:", player_value)
        print("\nComputer's hand:", [card.sign for card in computer_cards])
        print("Computer's hand value:", computer_value)

    def play_game(self):
        self.deck.shuffle()
        player_hand, computer_hand = self.deal_initial_cards()

        while True:
            self.display_hand_and_value(player_hand, computer_hand)

            if sum(card.weight for card in player_hand) == 21:
                print("Congratulations! You got Blackjack!")
                break
            elif sum(card.weight for card in player_hand) > 21:
                print("Busted! You went over 21. You lose.")
                break

            action = input("Do you want to 'hit' or 'stand'? ").lower()

            if action == 'hit':
                player_hand.append(self.deck.take_from_top())
            elif action == 'stand':
                while sum(card.weight for card in computer_hand) < 17:
                    computer_hand.append(self.deck.take_from_top())

                self.display_hand_and_value(player_hand, computer_hand)

                if sum(card.weight for card in computer_hand) > 21:
                    print("Computer busted! You win!")
                elif sum(card.weight for card in computer_hand) > sum(card.weight for card in player_hand):
                    print("Computer wins!")
                elif sum(card.weight for card in computer_hand) < sum(card.weight for card in player_hand):
                    print("You win!")
                else:
                    print("It's a tie!")

                break
            else:
                print("Invalid action. Please enter 'hit' or 'stand'.")

if __name__ == "__main__":
    print("Welcome to Blackjack!")
    game = Game()
    game.play_game()

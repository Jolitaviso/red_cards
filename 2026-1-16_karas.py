import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.sign = self.get_card_symbol() + rank
        self.weight = self.calculate_weight()

    def calculate_weight(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return ranks.index(self.rank) + 2

    def get_card_symbol(self):
        suits = {'hearts': '\n\u2665 ', 'diamonds': '\n\u2666 ', 'clubs': '\n\u2663 ', 'spades': '\n\u2660 '}
        return suits.get(self.suit, '')

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def take_from_top(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self):
        if len(self.hand) > 0:
            return self.hand.pop(0)
        else:
            return None

    def collect_cards(self, cards):
        self.hand.extend(cards)

def ask_to_continue():
    user_input = input("Do you want to continue the game? (y/n): ").lower()
    return user_input == 'y'

def play_war_game(player1, player2):
    deck = Deck()
    deck.shuffle()

    players = [Player(player1), Player(player2)]

    for _ in range(len(deck.cards) // len(players)):
        for player in players:
            player.collect_cards([deck.take_from_top()])

    while all(len(player.hand) > 0 for player in players):
        played_cards = []

        for player in players:
            played_card = player.play_card()
            played_cards.append(played_card)
            print(f"{player.name}: {played_card.sign}")

        max_weight = max(card.weight for card in played_cards)
        winners = [player for player, card in zip(players, played_cards) if card.weight == max_weight]

        if len(winners) == 1:
            winner = winners[0]
            winner.collect_cards(played_cards)
            print(f"{winner.name} wins the war!\n")
        else:
            print("It's a war!\n")
            for player in players:
                if len(player.hand) > 1:
                    played_cards.extend([player.play_card(), player.play_card()])
            for card in played_cards:
                winners[random.randint(0, len(winners) - 1)].collect_cards([card])

        if not ask_to_continue():
            break

    if len(players[0].hand) > len(players[1].hand):
        print(f"{players[0].name} wins the game!")
    elif len(players[1].hand) > len(players[0].hand):
        print(f"{players[1].name} wins the game!")
    else:
        print("It's a TIE!")

if __name__ == "__main__":
    player1 = input("Enter the name of Player 1: ")
    player2 = input("Enter the name of Player 2: ")
    play_war_game(player1, player2)

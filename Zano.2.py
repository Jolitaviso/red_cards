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
        elif self.rank == 'A':
            return 14
        else:
            return 13

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

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
    
    def take_from_bottom(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
    
class Player:
    def __init__(self):
        self.hand = []

    def add_to_hand(self, card):
        self.hand.append(card)

class AI(Player):
    def play_card(self):
        if len(self.hand) > 0:
            return self.hand.pop(0)
        else:
            return None
    
def play_war_game():
    deck = Deck()
    deck.shuffle()

    player = Player()
    ai = AI()

    for _ in range(26):
        player.add_to_hand(deck.take_from_top())
        ai.add_to_hand(deck.take_from_top())

    while True:
        player_card = player.add_to_hand(deck.take_from_bottom())
        ai_card = ai.play_card()

        if player_card is None or ai_card is None:
            break

        print(f"Player: {player_card.sign} vs AI: {ai_card.sign}")

        if player_card.weight > ai_card.weight:
            player.add_to_hand(player_card)
            player.add_to_hand(ai_card)
        elif ai_card.weight > player_card.weight:
            ai.add_to_hand(player_card)
            ai.add_to_hand(ai_card)

    if len(player.hand) > len(ai.hand):
        print("Player wins!")
        return "Player wins!"
    elif len(ai.hand) > len(player.hand):
        print("AI wins!")
        return "AI wins!"
    else:
        print("It's a TIE!")
        return "TIE"


if __name__ == "__main__":
    result = play_war_game()
    print(f"The game result is: {result}")

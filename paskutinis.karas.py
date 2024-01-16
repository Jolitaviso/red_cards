import random

class Card:
    def __init__(self, rank, suit, weight):
        self.rank = rank
        self.suit = suit
        self.sign = suit + rank
        self.weight = weight

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        weights = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit, weights[rank]))

    def shuffle(self):
        self.cards = random.sample(self.cards, len(self.cards))

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

class AI(Player):
    def __init__(self, name):
        super().__init__(name)

class WarGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.ai = AI("AI")
        self.result = None

    def play_round(self):
        round_cards = []

        player_card = self.player.play_card()
        ai_card = self.ai.play_card()

        if player_card is not None and ai_card is not None:
            print(f"{self.player.name}: {player_card.sign} vs {self.ai.name}: {ai_card.sign}")

            if player_card.weight > ai_card.weight:
                self.player.collect_cards([player_card, ai_card])
                self.player.collect_cards(round_cards)
            elif ai_card.weight > player_card.weight:
                self.ai.collect_cards([player_card, ai_card])
                self.ai.collect_cards(round_cards)
            else:
                print("War!")

                for _ in range(3):
                    war_player_card = self.player.play_card()
                    war_ai_card = self.ai.play_card()

                    if war_player_card is not None and war_ai_card is not None:
                        round_cards.extend([war_player_card, war_ai_card])
                        print(f"War - {self.player.name}: {war_player_card.sign} vs {self.ai.name}: {war_ai_card.sign}")

                self.play_round()

    def play_game(self):
        self.deck.shuffle()

        for _ in range(26):
            self.player.collect_cards([self.deck.take_from_top()])
            self.ai.collect_cards([self.deck.take_from_top()])
            
        round_count = 0  # Nauja eilutė
        while len(self.player.hand) > 0 and len(self.ai.hand) > 0 and round_count < 26:  # Pridėtas naujas sąlygos dalykas
            round_count += 1  # Nauja eilutė
            self.play_round()

        if len(self.player.hand) > len(self.ai.hand):
            self.result = f"{self.player.name} wins!"
        elif len(self.ai.hand) > len(self.player.hand):
            self.result = f"{self.ai.name} wins!"
        else:
            self.result = "It's a TIE!"

        print(self.result)
        return self.result

if __name__ == "__main__":
    war_game = WarGame()
    war_game.play_game()

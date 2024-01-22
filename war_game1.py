

import random

suits = ['♣', '♦', '♥', '♠']  # Clubs, Diamonds, Hearts, Spades
ranks = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

random.shuffle(deck)

player1_deck = deck[:len(deck)//2]
player2_deck = deck[len(deck)//2:]

player1_score = 0
player2_score = 0

rank_values = {rank: value for value, rank in enumerate(ranks, start=2)}

def get_card_score(card):
    return rank_values[card['rank']]

def card_to_str(card):
    return f"{card['rank']} of {card['suit']}"

while player1_deck and player2_deck: # Zaidziame iki kol baigiasi kortu kalade
    card1 = player1_deck.pop()
    card2 = player2_deck.pop()

    score1 = get_card_score(card1)
    score2 = get_card_score(card2)

    card1_str = card_to_str(card1)
    card2_str = card_to_str(card2)

    if score1 > score2:
        player1_score += 1
        print(f"Player 1 wins this round! (Card: {card1_str} vs {card2_str})")
    elif score1 < score2:
        player2_score += 1
        print(f"Player 2 wins this round! (Card: {card2_str} vs {card1_str})")
    else:
        print(f"It's a tie this round! (Card: {card1_str} vs {card2_str})")

# Laimetojas
if player1_score > player2_score:
    print(f"Player 1 wins the game with a score of {player1_score} to {player2_score}!")
elif player2_score > player1_score:
    print(f"Player 2 wins the game with a score of {player2_score} to {player1_score}!")
else:
    print(f"The game is a tie with a score of {player1_score} to {player2_score}!")
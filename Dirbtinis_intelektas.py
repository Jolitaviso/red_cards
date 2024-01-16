import random

def generate_deck():
    suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suite) for suite in suites for rank in ranks]
    random.shuffle(deck)
    return deck

def play_war(deck):
    player1 = deck[:len(deck)//2]
    player2 = deck[len(deck)//2:]

    round_number = 1
    while player1 and player2:
        card1 = player1.pop(0)
        card2 = player2.pop(0)

        print(f"\nRound {round_number}:")
        print(f"Player 1 plays {card1[0]} of {card1[1]}")
        print(f"Player 2 plays {card2[0]} of {card2[1]}")

        if ranks.index(card1[0]) > ranks.index(card2[0]):
            print("Player 1 wins the round!")
            player1.extend([card1, card2])
        elif ranks.index(card1[0]) < ranks.index(card2[0]):
            print("Player 2 wins the round!")
            player2.extend([card1, card2])
        else:
            print("It's a tie! War begins!")

            war_cards1 = [card1]
            war_cards2 = [card2]

            while True:
                if len(player1) < 4 or len(player2) < 4:
                    print("Not enough cards for war. Game over.")
                    return

                for _ in range(4):
                    war_cards1.append(player1.pop(0))
                    war_cards2.append(player2.pop(0))

                print("War cards are drawn!")

                last_war_card1 = war_cards1[-1]
                last_war_card2 = war_cards2[-1]

                print(f"Player 1 plays {last_war_card1[0]} of {last_war_card1[1]}")
                print(f"Player 2 plays {last_war_card2[0]} of {last_war_card2[1]}")

                if ranks.index(last_war_card1[0]) > ranks.index(last_war_card2[0]):
                    print("Player 1 wins the war!")
                    player1.extend(war_cards1 + war_cards2)
                    break
                elif ranks.index(last_war_card1[0]) < ranks.index(last_war_card2[0]):
                    print("Player 2 wins the war!")
                    player2.extend(war_cards1 + war_cards2)
                    break
                else:
                    print("It's still a tie! War continues!")

        round_number += 1

if __name__ == "__main__":
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = generate_deck()
    play_war(deck)

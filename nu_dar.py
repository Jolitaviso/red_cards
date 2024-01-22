import random

def generate_deck():
    suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suite) for suite in suites for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        rank = card[0]
        if rank.isdigit():
            value += int(rank)
        elif rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            num_aces += 1
            value += 11

    # Adjust for Aces
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

def add_card_to_hand(hand, deck):
    new_card = deck.pop()
    hand.append(new_card)
    print("You drew:", new_card)

def play_blackjack():
    deck = generate_deck()
    player_hand = [deck.pop(), deck.pop()]
    computer_hand = [deck.pop(), deck.pop()]

    while True:
        print("\nYour hand:", player_hand)
        print("Computer's hand:", [computer_hand[0]])

        player_value = calculate_hand_value(player_hand)
        computer_value = calculate_hand_value(computer_hand)

        if player_value == 21:
            print("Congratulations! You got Blackjack!")
            break
        elif player_value > 21:
            print("Busted! You went over 21. You lose.")
            break

        action = input("Do you want to 'hit' or 'stand'? ").lower()

        if action == 'hit':
            add_card_to_hand(player_hand, deck)
        elif action == 'stand':
            while computer_value < 17:
                add_card_to_hand(computer_hand, deck)
                computer_value = calculate_hand_value(computer_hand)

            print("\nYour hand:", player_hand)
            print("Your hand value:", player_value)
            print("\nComputer's hand:", computer_hand)
            print("Computer's hand value:", computer_value)

            if computer_value > 21:
                print("Computer busted! You win!")
            elif computer_value > player_value:
                print("Computer wins!")
            elif computer_value < player_value:
                print("You win!")
            else:
                print("It's a tie!")

            break
        else:
            print("Invalid action. Please enter 'hit' or 'stand'.")

if __name__ == "__main__":
    print("Welcome to Blackjack!")
    play_blackjack()
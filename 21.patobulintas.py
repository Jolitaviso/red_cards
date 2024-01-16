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

def display_hand_and_value(player_hand, computer_hand):
    player_value = calculate_hand_value(player_hand)
    computer_value = calculate_hand_value(computer_hand)

    print("\nYour hand:", player_hand)
    print("Your hand value:", player_value)
    print("\nComputer's hand:", computer_hand)
    print("Computer's hand value:", computer_value)

def play_blackjack():
    deck = generate_deck()
    player_hand = [deck.pop(), deck.pop()]
    computer_hand = [deck.pop(), deck.pop()]

    while True:
        display_hand_and_value(player_hand, computer_hand)

        if calculate_hand_value(player_hand) == 21:
            print("Congratulations! You got Blackjack!")
            break
        elif calculate_hand_value(player_hand) > 21:
            print("Busted! You went over 21. You lose.")
            break

        action = input("Do you want to 'hit' or 'stand'? ").lower()

        if action == 'hit':
            player_hand.append(deck.pop())
        elif action == 'stand':
            while calculate_hand_value(computer_hand) < 17:
                computer_hand.append(deck.pop())

            display_hand_and_value(player_hand, computer_hand)

            if calculate_hand_value(computer_hand) > 21:
                print("Computer busted! You win!")
            elif calculate_hand_value(computer_hand) > calculate_hand_value(player_hand):
                print("Computer wins!")
            elif calculate_hand_value(computer_hand) < calculate_hand_value(player_hand):
                print("You win!")
            else:
                print("It's a tie!")

            break
        else:
            print("Invalid action. Please enter 'hit' or 'stand'.")

if __name__ == "__main__":
    print("Welcome to Blackjack!")
    play_blackjack()

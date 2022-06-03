import random

while True:
    user_action = input("Enter a choice (R, P, S): ")
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    print(f"\nPlayer {user_action}, CPU {computer_action}.\n")

    if user_action == computer_action:
        print(f"the computer and player pick the same move {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print("You win!")
        else:
            print("You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("You win!")
        else:
            print("You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("You win!")
        else:
            print("You lose.")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
import random

while True:
    choice = ["rock", "paper", "scissors"]

    computer = random.choice(choice)
    player = None
    while player not in choice:  # keeps asking until we provide input that we should
        player = input("rock, paper , scissors?: ").lower()

    print("Computer:", computer)
    print("Player:", player)

    if player == computer:
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("You Lose")
        if computer == "scissor":
            print("You Win")

    elif player == "scissors":
        if computer == "rock":
            print("You Lose")
        if computer == "paper":
            print("You Win")

    elif player == "paper":
        if computer == "scissor":
            print("You Lose")
        if computer == "rock":
            print("You Win")

    play_again = input("Play again?: ").lower()

    if play_again != "yes":
        break

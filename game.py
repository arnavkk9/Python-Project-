import random

print("Welcome to Rock, Paper, Scissors!")
print("Player vs Mike")
print("-------------------------")

choices = ["rock", "paper", "scissors"]

while True:
    player = input("Player, enter rock, paper, or scissors: ").lower()

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    mike = random.choice(choices)

    print("Mike chose:", mike)

    if player == mike:
        print("It's a tie!")

    elif player == "rock" and mike == "scissors":
        print("Player wins! Rock smashes scissors.")

    elif player == "paper" and mike == "rock":
        print("Player wins! Paper covers rock.")

    elif player == "scissors" and mike == "paper":
        print("Player wins! Scissors cut paper.")

    else:
        print("Mike wins!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Game Over. Thanks for playing!")
        break

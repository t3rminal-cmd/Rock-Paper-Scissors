# ROCK-PAPER-SCISSORS GAME
import random

print("Let's play rock, paper, scissors!")

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Choose: rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU LOOSE!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU WIN!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU LOOSE!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU WIN!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU LOOSE!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU WIN!")

    play_again = input("Play again? y/n: ").lower()

    if play_again != "y":
        break

print("Good Bye!")

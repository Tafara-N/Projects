#!/usr/bin/python

import random

"""
A rock, paper, scissors game
"""

while True:

    player = None
    draw = ['rock', 'paper', 'scissors']
    computer = random.choice(draw)

    while player not in draw:
        player = input("\nRock, paper or scissors: ").lower()

        if player not in draw:  # Checks if user input is correct.
            print("\n(Pick rock, paper or scissors only.)")
            continue

    if player == computer:  # Ties if both player and computer pick the same option
        print("\nComputer picked:", computer)
        print("You picked:", player)
        print("It's a tie!!")

    elif player == "rock":
        if computer == "paper":
            print("\nComputer picked:", computer)
            print("You picked:", player)
            print("You lose!!")

        if computer == "scissors":
            print("\nComputer picked:", computer)
            print("You picked:", player)
            print("You win!!")

    elif player == "scissors":
        if computer == "rock":
            print("\nComputer picked:", computer)
            print("You picked:", player)
            print("You lose!!")

        if computer == "paper":
            print("\nComputer picked:", computer)
            print("You picked:", player)
            print("You win!!")

    elif player == "scissors":
        if computer == "rock":
            print("\nComputer picked:", computer)
            print("You picked:", player)
            print("You lose!!")

        if computer == "rock":
            print("\nComputer picked:", computer)
            print("You picked:", player)
            print("You win!!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\nThank's for playing, Bye!!")

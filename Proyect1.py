2# Rock, Paper, Scissors, Lizard, Spock is the geek version of the classic Rock, Paper, Scissors game.
# Rules: 
# Scissors cuts Paper. Paper covers Rock. Rock crushes Lizard. Lizard poisons Spock. 
# Spock smashes Scissors. Scissors decapitates Lizard. Lizard eats Paper. Paper disproves Spock.
# Spock vaporizes Rock. (and as it always has) Rock crushes Scissors.

import random

rock = '''🪨'''
paper = '''🧻'''
scissors = '''✂️'''
lizard = '''🦎'''
spock = '''🖖'''

game_images = [rock, paper, scissors, lizard, spock]

print("ROCK, PAPER, SCISSORS, LIZARD, SPOCK GAME!\n")

user_choice = int(input("What do you choose? Type 0 for rock 🪨 , 1 for paper 🧻, 2 for scissors ✂️ , 3 for lizard 🦎 and 4 for spock 🖖.\n"))
if user_choice >= 5 or user_choice < 0:
    print("You typed an invalid number, you lose!💩")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 4)
    print("Computer chose:")
    print(game_images[computer_choice])

    if computer_choice == user_choice:
        print("It's a draw")
    elif user_choice == 2 or user_choice == 4 and computer_choice == 0:
        print("You win!🎊")
    elif user_choice == 2 or user_choice == 3 and computer_choice == 1:
        print("You win!🎊")    
    elif user_choice == 0 or user_choice == 4 and computer_choice == 2:
        print("You win!🎊")
    elif user_choice == 0 or user_choice == 2 and computer_choice == 3:
        print("You win!🎊")
    elif user_choice == 1 or user_choice == 3 and computer_choice == 4:
        print("You win!🎊")
    else:
        print("You lose!💩")
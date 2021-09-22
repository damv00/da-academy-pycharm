import random
import time

user_points=0
computer_points=0
play_again="YES"
while play_again in ("YES","Y"):
    print("WELCOME TO THE ROCK,PAPER AND SCISSORS GAME")
    weapon= ""
    while weapon not in ["ROCK", "PAPER", "SCISSORS"]:
        weapon = input("Choose your weapon (Rock,paper,scissors): ")
        weapon = weapon.upper()
        if weapon not in ["ROCK", "PAPER", "SCISSORS"]:
            print("Enter a valid option,try again")
            clear()

    print("LET´S PLAY")
    time.sleep(.5)
    print("ROCK")
    time.sleep(.5)
    print("PAPER")
    time.sleep(.5)
    print("SCISSORS")
    time.sleep(.5)

    computer_weapon=random.choice(["ROCK","PAPER","SCISSORS"])
    print(f"You chose: '{weapon}' and the computer chose: '{computer_weapon}'")

    if weapon==computer_weapon:
        print("TIE GAME")
    else:
        if weapon== "ROCK" and computer_weapon== "SCISSORS":
            print("The user wins")
            user_points+=1
        elif weapon== "ROCK" and computer_weapon== "PAPER":
            print("The computer wins")
            computer_points+=1
        elif weapon== "PAPER" and computer_weapon== "ROCK":
            print("The user wins")
            user_points += 1
        elif weapon== "PAPER" and computer_weapon== "SCISSORS":
            print("The computer wins")
            computer_points += 1
        elif weapon== "SCISSORS" and computer_weapon== "PAPER":
            print("The user wins")
            user_points += 1
        elif weapon== "SCISSORS" and computer_weapon== "ROCK":
            print("The computer wins")
            computer_points += 1
    print(f"You have: {user_points} points vs {computer_points} points from the machine")
    play_again=input("Do you want to play again? (Enter: YES or NO): ").upper()

print("Game finished")

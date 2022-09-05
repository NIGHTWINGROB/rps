import random

while True:
    picks = ["rock", "paper", "scissors"]

    computer = random.choice(picks)
    player = None

    while player not in picks:
        player = input("rock, paper, or scissors cuh chill...").lower()
        if player == computer:
            print('computer: ', computer)
            print('player: ', player)
            print("It's a tie, don't quit!!")
        elif player == "rock":
            if computer == 'paper':
                print('computer: ', computer)
                print('player: ', player)
                print("You lose, Trash!!")
            if computer == 'scissors':
                print('computer: ', computer)
                print('player: ', player)
                print("You win Gee!!")
        elif player == "paper":
            if computer == 'scissors':
                print('computer: ', computer)
                print('player: ', player)
                print("You lose, Trash!!")
            if computer == 'rock':
                print('computer: ', computer)
                print('player: ', player)
                print("You win Gee!!")
        elif player == "scissors":
            if computer == 'rock':
                print('computer: ', computer)
                print('player: ', player)
                print("You lose, Trash!!")
            if computer == 'paper':
                print('computer: ', computer)
                print('player: ', player)
                print("You win Gee!!")
    Play_Again = input('Wanna play again (yes/no): ')
    
    if Play_Again != 'yes':
        break
        print('Later you idiot')
        

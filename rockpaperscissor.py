import random

print("Welcome to Rock, Paper, Scissors Game ")
listChoice = []
inputChoice = input("Enter your choice(Rock, Paper, Scissors): ")
listChoice.append(inputChoice)


def computerChoice():
    computerInput = random.choice(listChoice)
    return computerInput


def userChoice():
    return inputChoice


while True:
    if userChoice() == computerChoice():
        print("Draw")
    elif userChoice() == "Rock" and computerChoice() == "Scissors":
        print("You win")
    elif userChoice() == "Paper" and computerChoice() == "Rock":
        print("You win")
    elif userChoice() == "Scissors" and computerChoice() == "Paper":
        print("You win")
    else:
        print("Computer win")
    break

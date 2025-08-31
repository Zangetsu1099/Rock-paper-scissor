## Hello seniors ,I am Mohit Kumar Mandal from SRM University Ktr (Branch).This is a rock paper scissors
# game with a little gambling. I will demonstrate it to u, when I do that I will just change the odd to
# get the desired output so plz don't mind that.Thank You

import random

base_option = ("rock", "paper", "scissor")
updated_option = ("rock", "paper", "scissor", "golden_hand")
player = 0
win = 0
loss = 0
tie = 0
running = True
computer = random.choices(base_option)

print("Welcome to Rock Paper Scissor Game (with gambling)")
while running:
    computer = random.choices(base_option)
    # Player has 1 in 100 chance to get golden hand option which he can pick and get a guarantee win
    if random.random() < 0.01:
        print("WOW!!....You got lucky & Unlocked Golden Hand....")
        player = input("Enter your choice('rock', 'paper', 'scissor', 'golden_hand'): ").lower()
        while player not in updated_option:
            print("Invalid Choice please choose from given options!")
            player = input("Enter your choice('rock', 'paper', 'scissor', 'golden_hand'): ").lower()

    else:
        player = base_option
        while player not in base_option:
            player = input("Enter your choice('rock', 'paper', 'scissor'): ").lower()
            if player not in base_option:
                print("Invalid Choice please choose from given options!")
            # Computer has also 1 in 100 chance to get a guarantee win
    if random.random() < 0.01:
        print("Well....Luck is not on your side....")
        computer_option = "golden_hand"
        computer = computer_option
        print(f"player:{player}")
        print(f"computer:{computer}")
        print("------------------")
    else:
        computer_option = base_option
        computer = random.choice(base_option)
        print(f"player:{player}")
        print(f"computer:{computer}")
        print("------------------")
        # Here are the possible outcome for the option u can choose
    if player != "golden_hand" and computer == "golden_hand":
        print("Computer used Golden Hand... You Lose!")
        loss += 1
    elif player == "golden_hand" and computer != "golden_hand":
        print("Golden Hand beats everything! You Win!")
        win += 1
    elif player == "golden_hand" and computer == "golden_hand":
        print("--It's a Tie--")
        tie += 1
    elif player == computer:
        print("--It's a Tie--")
        tie += 1
    elif player == "rock" and computer == "paper":
        print("----You Lose!----")
        loss += 1
    elif player == "rock" and computer == "scissor":
        print("----You Win!----")
        win += 1
    elif player == "scissor" and computer == "rock":
        print("----You Lose----!")
        loss += 1
    elif player == "scissor" and computer == "paper":
        print("----You win!----")
        win += 1
    elif player == "paper" and computer == "scissor":
        print("----You Lose!----")
        loss += 1
    elif player == "paper" and computer == "rock":
        print("----You Win----")
        win += 1
    print("------------------")
    # Y = yes(To Continue the game)
    # N = No(To Exit the game)
    # S = Scoreboard(To See the scoreboard)
    choice = 0
    answers = ("Y", "N", "S")
    answer = ("Y", "N")
    while choice not in answers:
        choice = input("Play Again?(Y/N/S(scoreboard)): ").upper()
        if choice not in answers:
            print("Please Enter the valid Option ")
        if choice == "S":
            print(f"Wins = {win}" "|" f"Losses = {loss}" "|" f"Tie = {tie}")
            while choice not in answer:
                choice = input("Play Again?(Y/N): ").upper()
                if choice not in answer:
                    print("Please Enter the valid Option ")

        if choice == "N":
            running = False
            print("Thanks for playing!!....")












# Rock Paper simulator, will play best out of three.

import random

keep_going = 0
your_score = 0
pc_score = 0
play_again = True


def pc_roll():
    pc_options = (random.choice(['rock', 'paper', 'scissors']))
    return pc_options

def who_won(user_choice, pc_chose):
    #rock vs logic
    if user_choice == 'rock' and pc_chose == 'paper':
        message = ("Paper covers Rock, you lost!\n")
        print(message)
        global pc_score
        pc_score += 1
        return (message, pc_score)
    
    if user_choice == 'rock' and pc_chose == 'scissors':
        message = ("Rock smashes Scissors, you won!\n")
        print(message)
        global your_score
        your_score += 1
        return (message, your_score)

    if user_choice == 'rock' and pc_chose == 'rock':
        message = ("Draw, go again...\n")
        print(message)
        global keep_going
        keep_going -= 1
        return (message, keep_going)

    # Paper vs logic
    if user_choice == 'paper' and pc_chose == 'scissors':
        message = ("Scissors cuts Paper, you lost!\n")
        print(message)
        pc_score += 1
        return (message, pc_score)
    
    if user_choice == 'paper' and pc_chose == 'rock':
        message = ("Paper covers Rock, you won!\n")
        print(message)
        your_score += 1
        return (message, your_score)

    if user_choice == 'paper' and pc_chose == 'paper':
        message = ("Draw, go again...\n")
        print(message)
        keep_going -= 1
        return (message, keep_going)

    # Scissors vs logic
    if user_choice == 'scissors' and pc_chose == 'rock':
        message = ("Rock smashes Scissors, you lost!\n")
        print(message)
        pc_score += 1
        return (message, pc_score)
    
    if user_choice == 'scissors' and pc_chose == 'paper':
        message = ("Scissors cuts Paper, you won!\n")
        print(message)
        your_score += 1
        return (message, your_score)

    if user_choice == 'scissors' and pc_chose == 'scissors':
        message = ("Draw, go again...\n")
        print(message)
        keep_going -= 1
        return (message, keep_going)



while play_again == True:
    while keep_going <= 2:

        print('\nRock, Paper,Scissors! Will you win?')
        print('You can choose Rock, Paper, or Scissors')
        user_choice = str.lower(input("What do you choose? : "))

        pc_chose = pc_roll()

        print(f'\nYou chose {user_choice} :: The PC chose: {pc_chose}\n')
    
        play = who_won(user_choice, pc_chose)

        print(f"Your score is: {your_score} :::: PC score is: {pc_score}")

        keep_going += 1
        if your_score == 2 or pc_score == 2:
            break

    print("\nThe final score was:")
    print(f"You: {your_score} :::: PC: {pc_score}\n")

    if your_score > pc_score:
        print("You Won!\n")

    else:
        print("You Lost...\n")

    again = input("Would you like to play again? (y or n): ")
    if again == 'y' or again == 'yes':
        play_again == True
        your_score = 0
        pc_score = 0
        keep_going = 0

    if again == 'n' or again == 'no':
        play_again == False
        print("\nGoodbye...\n")
        break

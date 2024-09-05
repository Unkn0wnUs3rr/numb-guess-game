import random
import sys
import time
import csv
import tabulate
print('Welcome to the Number Guessing Game!\n')
name = input('What is your name? ')
        

def game(timer):
    
    chances = 0
    difficulty = ''
    #When the game starts, it should display a welcome message along with the rules of the game.
    print('''I'm thinking of a number between 1 and 100.
    ''')
    print('''Please select the difficulty level to begin:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    ''')
    
    #User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.
    chosen  = input('Enter your choice: ')
    if chosen == '1':
        difficulty = 'Easy'
        chances = 10
    elif chosen == '2':
        difficulty = 'Medium'
        chances = 5
    elif chosen== '3':
        difficulty = 'Hard'
        chances = 3
    else:
        while chosen not in ['1','2','3']:
            print('Please select a number between 1 and 3.')
            chosen  = input('Enter your choice: ')
        if chosen == '1':
            difficulty = 'easy'
            chances = 10
        elif chosen == '2':
            difficulty = 'Medium'
            chances = 5
        elif chosen == '3':
            difficulty = 'Hard'
            chances = 3
    #The computer should randomly select a number between 1 and 100.
    number =  random.randint(1,100)

    print(f'Great! You have selected the {difficulty} difficulty level.')
    print('Let\'s start the game!')
    if timer == True:
        start_time = time.time()
    counter = 0
    guess = None
    while counter != chances and guess != number:
        while True:
            try: 
                guess = int(input('Enter your guess: '))
                break
            except ValueError:
                print('Please provide a number')
        counter += 1
        if guess > number and chances != counter:
            print(f'Incorrect! The number is less than {guess}')
        elif guess < number and chances != counter:
            print(f'Incorrect! The number is larger than {guess}')
    #The user should be able to enter their guess.
    if guess == number:
        if timer == True:
             totaltime = round((time.time() - start_time), 2)
             print(f'Congratulations {name}! You guessed the correct number in {totaltime} minutes and {counter} attemps!')
        else:
            print(f'Congratulations {name}! You guessed the correct number in {counter} attemps!')
    else:
        print(f'Unlucky! You ran out of chances. The number was {number}.')
    #If the user’s guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.
    #If the user’s guess is incorrect, the game should display a message indicating whether the number is greater or less than the user’s guess.
    #The game should end when the user guesses the correct number or runs out of chances

while True:
    if (timed := input('Would you like to play against time? (y/n) ').strip().lower()) == 'y':
        game(True)
    elif timed == 'n':
        game(False)
    playAgain = input('Would you like to play again? (y/n) ').strip().lower()
    if playAgain == 'n':
        break



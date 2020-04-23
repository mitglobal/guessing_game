# This is a guessing the number game.
#import random :the random function brings out random numbers for the game
def easy():
    #generates a random number between 1-10 and stores it in number
    number = random.randint(1,10)
    #print(number)
    guess_count = 0
    guess_limit = 6

    while guess_count < guess_limit:
        guess = int(input('Take a guess: '))
        guess_count += 1

        if guess == number:
            print(f'Good job {myName}, You got it right!')
            break

        elif guess < number:
            print('Your guess is too low, wrong guess.')
            if guess_count == 5:
                print('You have one last chance')
            if guess_count == guess_limit:
                print('''
That was wrong!!!
Game over
                      ''')

        else:
            print('Your guess is too high.')
            if guess_count == 5:
                print('You have one last chance')
            if guess_count == guess_limit:
                print('''
That was wrong!!!
Game over
                      ''')

def medium():
    #generates a random number between 1-20 and stores it in number
    number = random.randint(1,20)
    #print(number)
    guess_count = 0
    guess_limit = 4

    while guess_count < guess_limit:
        guess = int(input('Take a guess: '))
        guess_count += 1

        if guess == number:
            print(f'Good job {myName}, You got it right!')
            break

        elif guess < number:
            print('Your guess is too low, wrong guess.')
            if guess_count == 3:
                print('You have one last chance')
            if guess_count == guess_limit:
                print('''
That was wrong!!!
Game over
                      ''')

        else:
            print('Your guess is too high.')
            if guess_count == 3:
                print('You have one last chance')
            if guess_count == guess_limit:
                print('''
That was wrong!!!
Game over
                      ''')

def hard():
    #generates a random number between 1-50 and stores it in number
    number = random.randint(1,50)
    #print(number)
    guess_count = 0
    guess_limit = 3

    while guess_count < guess_limit:
        guess = int(input('Take a guess: '))
        guess_count += 1

        if guess == number:
            print(f'Good job {myName}, You got it right!')
            break

        elif guess < number:
            print('Your guess is too low, wrong guess.')
            if guess_count == 2:
                print('You have one last chance')
            if guess_count == guess_limit:
                print('''
That was wrong!!!
Game over
                      ''')

        else:
            print('Your guess is too high.')
            if guess_count == 2:
                print('You have one last chance')
            if guess_count == guess_limit:
                print('''
That was wrong!!!
Game over
                      ''')

import random

print('Welcome to my guessing game 😻 !!!')
print('There are 3 levels: easy, medium and hard')
print('Easy: Pick a number from 1-10. You have 6 guessses')
print('Medium: Pick a number from 1-20. You have 4 guessses')
print('Hard: Pick a number from 1-50. You have 3 guessses')

# This statement will allow the options for playing and quiting the game.
play = True

while play:
    #user's name and levels are asked
    myName = input('Hello! What is your name? ')
    level = int(input('Pick a level of difficulty 1(easy), 2(medium), 3(hard): '))

    if level == 1:
        print ( f'{myName} You have choosen easy. You have 6 guesses.')
        easy()

    elif level == 2:
        print (f'{myName} You have choosen medium. You have 4 guesses.')
        medium()

    elif level == 3:
        print (f'{myName} You have choosen hard. You have 3 guesses.')
        hard()

    elif level != 1 and level != 2 and level != 3:
        print ("Invalid input!")

    # Play again loop that allows user to quit or play again.
    count=1
    again=str(input("Do you want to play again, type yes or no "))
    if again == "no":
        play = False

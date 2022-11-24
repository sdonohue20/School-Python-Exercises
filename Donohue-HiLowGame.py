#programmed by Sarah Donohue
#11/6/22
#Donohue-HiLoGame.py
#this program will generate a number from 1-max value the user enters, to which 
#the computer will generate random number that must be guessed by the user
import random

play_again = True

while play_again == True:
    maxnum = int(input('What should the maxmimmum number be for this game? '))
    number = random.randint(1, maxnum)
    guess = int(input('Guess my number: '))

    while guess != number:
        if guess < number:
            print('Your guess is too low!\n')
        elif guess > number:
            print('Your guess is too high!\n')
        guess = int(input('Guess my number: '))

    print('You guessed my number!\n')
    play_again = input('Do you wish to play again? (Y/N): ')
    if play_again.lower() == 'y':
        play_again = True
        
print('Thank you for playing!')
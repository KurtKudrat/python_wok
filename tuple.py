'''buffet_manue = ('sushi','taco','spiyce chken')
buffet_manue = ('sushi','beef','chken')



for item in buffet_manue:
    print(item)


'''



# this is a guess the number game.

import random
name = input()

print('Hi, ' + ', ' + "I'm thinking of a number between 1 and 20. Can you guess which one.")
secretNumber = random.randint(1,20)


for tekenGuesses in range(1,7):
    print("Take a guess.")
    guess = int(input())


    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too hight. ')
    else:
        print('that is right.')

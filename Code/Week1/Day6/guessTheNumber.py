import random


guess=False
rand_numb=random.randint(1,20)
counter =1
while guess==False:
    print('\nI am thinking of a number between 1 and 20.')
    number=input('Take a guess.\n')
    number=int(number)
    if rand_numb==number:
        print('Good job! You guessed my number in {} guesses!'.format(counter))
        break
    elif number>rand_numb:
        print('Too high!')
    elif number<rand_numb:
        print('Too low')
    counter+=1

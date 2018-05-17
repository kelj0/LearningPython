#!/usr/bin/python3
#!/usr/bin/python3
import random

rnd = random.Random()
number = rnd.randint(1,1000)
guesses = 0
msg = ""

while True:
    guess = int(input(msg+"\nGuess my number between 1 and 1000: "))
    guesses +=1
    if guess>number:
        msg+=str(guess) + ' is too high.\n'
    elif guess<number:
        msg+=str(guess)+ ' is too low.\n'
    else:
        break
print("Nois, you guessed it in {} guesses".format(guesses))
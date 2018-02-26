number = 23
guess = int(input('Enter an integer :'))

if guess==number:
    print("Your guessed it")
elif guess<number:
    print("Too low")
elif guess>number:
    print("Too high")

print("Done")
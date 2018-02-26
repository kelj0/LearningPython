number = 20
running=True

while running:
    guess=int(input('Enter your guess: '))

    if guess==number:
        print('Ez katka you guess it.')
        running = False
    elif guess<number:
        print('Too low.')
    else:
        print('Too high')
else:
    print('Loop is over')
print('Done')
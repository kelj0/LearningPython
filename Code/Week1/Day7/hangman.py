import random

names=("auto","tomtom","hangman")
choosing_name = random.randint(0,2)

guess_word=names[choosing_name]
game_over=False

play_name=[]
print('Wellcome to hangman!\n\n')
for i in range(0,len(guess_word)):
     print('_',  end=' ')
     play_name.append("_")
trys=0
while game_over==False:
    guess=input("\nType char: ")
    hit=False
    for i in guess_word:
        if i==guess:
            hit=True
            break

    for i in range(0,len(guess_word)):
        if ((hit==True) and (guess_word[i]==str(guess))):
            play_name[i]=guess
    temp_string=' '.join(play_name)
    print(temp_string)
    temp_string=""
    temp_string=''.join(play_name)
    guess_word=str(guess_word)
    if(temp_string==guess_word):
        game_over=True
    trys+=1
print("\n\nThank you for playing hangman by kegl you guess it in {} guesses".format(trys))
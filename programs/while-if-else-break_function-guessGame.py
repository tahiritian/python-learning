#Create a random number
#store
#give user input
#program hint (low/high value)

#use builtin library module

import random
r = random.randint(0,100)
print("I have thought of a number. Its your time to guess")

guesses = []
while True:
    ui = int(input("Enter your guess [0,100] : "))
    guesses.append(ui)
    if ui < r:
        print("Low")
    elif ui > r:
        print("High")
    else:
        print("Bingo! You guessed it right")
        print("You took", len(guesses), "guesses")
        print("These were your guesses ->", guesses)
        break


#OUTPUT
#$ python3 while-if-else-break_function-guessGame.py
#I have thought of a number. Its your time to guess
#Enter your guess [0,100] : 50
#Low
#Enter your guess [0,100] : 70
#Low
#Enter your guess [0,100] : 80
#Low
#Enter your guess [0,100] : 90
#Low
#Enter your guess [0,100] : 94
#High
#Enter your guess [0,100] : 91
#Bingo! You guessed it right
#You took 6 guesses
#These were your guesses -> [50, 70, 80, 90, 94, 91]


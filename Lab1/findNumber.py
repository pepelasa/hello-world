import random

value = random.randint(1,30)
print("Guess the value between 1 and 30")
numGuess = 0
cont = True

while cont:
    guess = input()
    numGuess +=1

    if guess == "exit":
        cont = False
    elif value == int(guess):
        print("Your guess is correct")
        cont = False
    elif value < int(guess):
        print("Your guess is too high")
        print("Guess again")
    elif value > int(guess):
        print("Your guess is too low")
        print("Guess again")

f = open("GuessingSteps.txt", "w+")

f.write("Number of guesses were %d\n" % numGuess)
f.close

print("Number of guesses were %d" % numGuess)
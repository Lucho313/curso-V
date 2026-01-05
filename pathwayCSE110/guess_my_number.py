

# my creativity made some things diferent like messges and variable names like mistery_number and more small things


import random


print("Welcome to 'The guess my number' game!")
print()

play_again = True

while play_again :

    guessed_wrong = True
    mistery_number = random.randint(1,20,)
    guesses = 0

    while guessed_wrong:
        guessed_number = int(input("What is your guess? "))
        guesses = guesses + 1


        if mistery_number < guessed_number:
            print("Lower!")
        elif mistery_number > guessed_number:
            print("Higher!")
        else:
            print()
            print("You got it!")
            guessed_wrong = False
            print()
            print(f"you took {guesses} guesses to get the number {mistery_number}")
            print()

    play_again = input("Do you want to play again? (yes/no) ")

    if play_again.lower() == "yes":
        play_again = True

    else:
        play_again = False
        print()
        print("Thanks for playing! Goodbye.")
        print()


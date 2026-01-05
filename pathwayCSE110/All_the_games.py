#this is a listo of games.


def get_game_1(user_choose):
        
        import random 
        play_again = True
        print("Welcome to 'The guess my number' game!")
        print()



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
                play_again = input("Do you want to play again? (yes/no) ")

                if play_again.lower() == "yes":
                    play_again = True

                else:
                 play_again = False
                 print()
                 print("Thanks for playing! Goodbye.")
                 print()
def get_game_2(user_choose):
    secret_word = "world"
    
    print("Welcome to the World puzzle game!")
    print()
    
    hint = "_ " * len(secret_word)
    print(f"Your hint is: {hint.strip()}")
    
    guess_count = 0

    while True:
        guess = input("What is your guess? ").lower()  
        guess_count = guess_count + 1  

        if len(guess) != len(secret_word):
            print(f"Sorry, the guess must have the same number of letters as the secret word.")
            continue  
        
        if guess == secret_word:
            print()
            print(f"Congratulations you got it!")
            print(f"You guessed the word in {guess_count} attempts!")
            break  
        
        new_hint = ["_"] * len(secret_word)
        
        remaining_secret_word = list(secret_word)

        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                new_hint[i] = guess[i].upper()  
                remaining_secret_word[i] = None 

        for i in range(len(secret_word)):
            if new_hint[i] == "_":  
                if guess[i] in remaining_secret_word:
                    new_hint[i] = guess[i].lower()  
                    remaining_secret_word[remaining_secret_word.index(guess[i])] = None 

        print(f"Your hint is: {' '.join(new_hint)}")
def get_game_3(user_choose):
    print("Zombie Survival Story")
    print("")
    print("Try to survive. The options will appear in capital letters as (EXAMPLE).")
    print("")
    input("Ready? ")

    print("Start…")
    print("")
    print("You wake up alone in a forest in the early morning. Not far away "
        "you see a cabin to the south, and to the north, a road leading to a bridge that takes you to a nearby city…")

    desciption_1 = input("You get up and must decide whether to go to the CABIN or the CITY or RUN through the forest. Where will you go?:  ").upper()

    # Cabin scenario

    if desciption_1 == "CABIN":
        print("")
        print("Once you're standing, you approach the cabin…")
        bag_option = input("At the entrance, you see a bag next to the door… Do you want to check the bag?... YES or NO : ").upper()
        if bag_option == "YES":
            print("")
            desciption_1_2 = input("Great, you got a rusty weapon... You're standing in front of the cabin door and you hear a strange noise not far away..." 
            " You have two options to go INSIDE the cabin or to INVESTIGATE the noise. What will you do? : ").upper()
        
            if desciption_1_2 == "INSIDE":
                print("")
                print("You rush into the cabin and as you close the door, you are struck by something unknown and devoured by zombies…. THE END")
            elif desciption_1_2 == "INVESTIGATE":
                print("")
                print("As you approach stealthily through the trees, you encounter some zombies… when you turn around, you see that you are surrounded…" 
                " you draw your weapon, but it jams when you try to fire, and you are tragically bitten and turned into a zombie")
            else:
                print("")
                print("You hadn't even decided what to do and a zombie dog ate you... THE END")
                print("Try again using the correct options marked in capital letters (EXAMPLE).")
        elif bag_option == "NO": 
            print("")
            desciption_1_2 = input("You're standing in front of the cabin door and you hear a strange noise not far away..." 
            " You have two options to go INSIDE the cabin or to INVESTIGATE the noise. What will you do? : ").upper()
            if desciption_1_2 == "INSIDE":
                print("")
                print("You rush into the cabin and as you close the door, you are struck by something unknown and devoured by zombies…. THE END")
            elif desciption_1_2 == "INVESTIGATE":
                 print("")
                 print("As you approach stealthily through the trees, you encounter some zombies… when you turn around, you see that you are surrounded…" 
                 " and you are tragically bitten and turned into a zombie")

            else:
             print("")
             print("You hadn't even decided what to do and a zombie dog ate you... THE END")
             print("Try again using the correct options marked in capital letters (EXAMPLE).")

        else:
             print("")
             print("You hadn't even decided what to do and a zombie dog ate you... THE END")
             print("Try again using the correct options marked in capital letters (EXAMPLE).")
    else:
        pass

    if desciption_1 == "RUN" or desciption_1 == "RUN THROUGH THE FOREST":
        print("")
        print("You ran into the forest and got lost, after hours of wandering you were surrounded by zombies and bitten... THE END")

    # city scenario

    if desciption_1 == "CITY":
        print("")
        print("You walk calmly in that direction, and the path seems deserted…")
        desciption_1_2 = input("When you're near the bridge, you notice zombies nearby who haven't noticed you yet. You panic and must quickly choose between RUNNING or CALMING DOWN and continuing to walk. What will you do? : ").upper()
        if desciption_1_2 == "RUNNING" or desciption_1_2 == "RUN":
            print("")
            print("You start running and the zombies around you notice, they chase you, and halfway across the bridge you trip and a zombie quickly bites you. You manage to escape and at the end of the bridge," 
            " not far away, you see a person who doesn't appear to be a zombie.")
            desciption_1_3 = input("You have two options: TALK to the person or TURN AROUND and continue on your way through the city. What will you do? : ").upper()
            if desciption_1_3 == "TALK":
                print("")
                print("You approach and, upon speaking with the person, she tells you her name is Darling and that she's a survivor, that there are more like her. But she notices you've been bitten, quickly pulls out her weapon, and shoots you. You die staring at the morning sky… THE END")
            elif desciption_1_3 == "TURN AROUND" or desciption_1_3 == "TURN" or desciption_1_3 == "AROUND":
                print("")
                print("You wandered around all day feeling the pain of the bite, and by the end of the afternoon, you were just another zombie… THE END")
            else:
                print("")
                print("You hadn't even decided what to do and a zombie dog ate you... THE END")
                print("Try again using the correct options marked in capital letters (EXAMPLE).")
        elif desciption_1_2 == "CALMING DOWN" or desciption_1_2 == "CALM"or desciption_1_2 == "CALMING" or desciption_1_2 == "DOWN":
            print("")
            print("You kept walking and saw a path to the side that was a bit more discreet. You followed it and reached the end of the path where you found a girl named Darling who helped you and took you to a group of survivors… THE END")
            print("")
            print("Well done, you survived!!!")
        else:
                print("")
                print("You hadn't even decided what to do and a zombie dog ate you... THE END")
                print("Try again using the correct options marked in capital letters (EXAMPLE).")
    else:
        print("")
        print("You hadn't even decided what to do and a zombie dog ate you... THE END")
        print("Try again using the correct options marked in capital letters (EXAMPLE).")

    print("")
    print("I hope you has enjoy it, please try againg and see all the scenaris to see if you could stay human. :)")

A= True
Games = ["1. Guess my number puzzle", "2. Guees the world puzzle", "3. History Game"]


print("Hello thanks for be here, choose what game or list that would you like to play.")
while A:
    print()
    print("Please select one game by the number")
    for menu in Games:
        print(menu)
    choose = input("Please enter an action: ")
    if choose == "1":
        get_game_1(choose)
    elif choose == "2":
        get_game_2(choose)
    elif choose == "3":
        get_game_3(choose)
"""""
 Author = Luis Villegas
"""""

#My creativity add some spaces and a congratulation message more natural like using word "you got it" instead of just "correct" or "right".

def main():
    
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

if __name__ == "__main__":
    main()

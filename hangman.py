import random

def hangman():
    # Step 1: Predefined word list
    words = ["python", "codealpha", "football", "hangman", "program"]
    
    # Step 2: Randomly choose a word
    word = random.choice(words)
    
    # Step 3: Track game state
    guessed = ["_"] * len(word)  # display underscores
    attempts = 6                 # max wrong guesses
    guessed_letters = []         # store letters guessed

    print(" Welcome to Hangman!")
    print("Guess the word: ", " ".join(guessed))
    
    # Step 4: Game loop
    while attempts > 0 and "_" in guessed:
        guess = input("Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("✅You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        print("Word: ", " ".join(guessed))
        print("Guessed letters: ", ", ".join(guessed_letters))

    # Step 5: Game outcome
    if "_" not in guessed:
        print(f"🎉 Congratulations! You guessed the word '{word}'")
    else:
        print(f"🚫..Game Over! The word was..🚫'{word}'")

# Run the game
hangman()

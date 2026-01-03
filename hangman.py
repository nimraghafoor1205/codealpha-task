import random   # Importing random module to select a word randomly


def hangman_game():
    # Step 1: Creating a list of predefined words
    words_list = ["python", "internship", "coding", "alpha", "developer"]

    # Step 2: Randomly selecting one word from the list
    secret_word = random.choice(words_list)

    # Step 3: Initializing game variables
    max_attempts = 6              # Maximum number of incorrect guesses allowed
    guessed_letters = set()       # Set to store guessed letters (avoids duplicates)

    # Step 4: Displaying game title and instructions
    print("\n===== HANGMAN GAME =====")
    print(f"Word Length: {len(secret_word)} letters")
    print("You have 6 incorrect attempts.\n")

    # Step 5: Starting the game loop
    # The loop continues until the player runs out of attempts
    while max_attempts > 0:

        # Step 6: Displaying the current state of the word
        # Guessed letters are shown, unguessed letters are shown as underscores
        displayed_word = "".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )
        print("Word:", " ".join(displayed_word))

        # Step 7: Checking win condition
        # If there are no underscores left, the user has guessed the word
        if "_" not in displayed_word:
            print("\n🎉 Congratulations! You guessed the word correctly.")
            return

        # Step 8: Taking user input
        guess = input("\nEnter a letter: ").lower()

        # Step 9: Validating user input
        # Ensures input is a single alphabet character
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabet letter.")
            continue

        # Step 10: Checking if the letter was already guessed
        if guess in guessed_letters:
            print("You have already guessed this letter.")
            continue

        # Step 11: Adding the guessed letter to the set
        guessed_letters.add(guess)

        # Step 12: Checking if the guessed letter is in the secret word
        if guess not in secret_word:
            max_attempts -= 1
            print(f"Incorrect guess. Remaining attempts: {max_attempts}")
        else:
            print("Correct guess!")

    # Step 13: Game over condition
    # Executed when all attempts are used
    print("\n❌ Game Over!")
    print("The correct word was:", secret_word)


# Step 14: Program execution starts here
if __name__ == "__main__":
    hangman_game()

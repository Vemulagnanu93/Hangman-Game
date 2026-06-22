import random

def display_hangman(tries):
    # ASCII art for hangman stages to make the game visually engaging in the console
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]

def play_game():
    # Predefined list of 5 words as specified in the instructions
    words_list = ["python", "developer", "software", "computer", "program"]
    word = random.choice(words_list).lower()
    word_letters = set(word)  # Letters in the secret word
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()  # Letters the user has guessed

    tries = 6  # Limit incorrect guesses to 6

    print("=======================================")
    print("      WELCOME TO HANGMAN GAME!         ")
    print("=======================================")
    print("Try to guess the secret programming-related word.")
    print(f"You have {tries} incorrect guesses allowed.")
    print("Let's start!")

    # Game loop
    while len(word_letters) > 0 and tries > 0:
        # Display current hangman state
        print(display_hangman(tries))
        
        # Display current word state (e.g., "p _ t h _ _")
        word_display = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_display))
        print(f"Guessed letters: {', '.join(sorted(used_letters)) if used_letters else 'None'}")
        print(f"Remaining incorrect guesses: {tries}")
        
        # Get user input
        user_guess = input("Guess a letter: ").strip().lower()
        print("\n" + "-"*40 + "\n")

        # Validate input
        if len(user_guess) != 1 or user_guess not in alphabet:
            print("Invalid input! Please guess a single alphabetical letter.")
            continue

        if user_guess in used_letters:
            print(f"You have already guessed the letter '{user_guess}'. Try a different one.")
            continue

        # Add to used letters list
        used_letters.add(user_guess)

        # Check if the guess is correct
        if user_guess in word_letters:
            word_letters.remove(user_guess)
            print(f"Good job! '{user_guess}' is in the word.")
        else:
            tries -= 1
            print(f"Oops! '{user_guess}' is not in the word.")

    # Game over checks
    if tries == 0:
        print(display_hangman(0))
        print("GAME OVER! You ran out of guesses.")
        print(f"The secret word was: '{word}'")
    else:
        print(f"CONGRATULATIONS! You successfully guessed the word: '{word}'!")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again not in ["y", "yes"]:
            print("Thank you for playing Hangman! Goodbye!")
            break
        print("\n" + "="*40 + "\n")

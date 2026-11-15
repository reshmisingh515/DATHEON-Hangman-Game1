import random

# -------------------- WORD LIST --------------------
WORDS = [
    "PYTHON",
    "COMPUTER",
    "PROGRAMMING",
    "KEYBOARD",
    "INTERNET",
    "SOFTWARE",
    "HARDWARE",
    "DEVELOPER",
    "DATABASE",
    "ALGORITHM"
]

# -------------------- HANGMAN DRAWINGS --------------------
# One drawing for each number of incorrect guesses (0 to 6).
HANGMAN_PICTURES = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========
""",
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========
""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
"""
]


def display_game(secret_word, guessed_letters, wrong_guesses):
    """Display the gallows, masked word, guessed letters, and remaining chances."""
    print(HANGMAN_PICTURES[wrong_guesses])

    masked_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("Word:             ", masked_word)
    print("Guessed letters:  ", " ".join(sorted(guessed_letters)) or "None")
    print("Attempts left:    ", 6 - wrong_guesses)


def play_game():
    """Run one complete Hangman game."""
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\n========== HANGMAN WORD GUESSING GAME ==========")
    print("Guess the hidden word one letter at a time.")
    print("You have 6 incorrect attempts. Good luck!")

    while wrong_guesses < max_wrong_guesses:
        display_game(secret_word, guessed_letters, wrong_guesses)

        # Check whether all letters have been guessed.
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word:", secret_word)
            return

        guess = input("\nEnter a letter: ").strip().upper()

        # Validate the input.
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter exactly one alphabet letter.")
            continue

        # Do not penalize a repeated guess.
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Incorrect guess!")

    # Show the final drawing and reveal the word after six mistakes.
    display_game(secret_word, guessed_letters, wrong_guesses)
    print("\nGame over! You used all 6 attempts.")
    print("The correct word was:", secret_word)


def main():
    """Allow the user to play multiple rounds."""
    while True:
        play_game()
        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()

        if play_again not in ("y", "yes"):
            print("\nThank you for playing Hangman!")
            break


if __name__ == "__main__":
    main()

import random

# 5 predefined words
words = ["python", "developer", "computer", "coding", "keyboard"]

# Select a random word
word = random.choice(words)

# Create blanks for the word
display = ["_"] * len(word)

# Game settings
wrong_guesses = 0
max_wrong_guesses = 6
guessed_letters = []

# Hangman stages
hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("=" * 35)
print("        HANGMAN GAME")
print("=" * 35)
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")


# Main game loop
while wrong_guesses < max_wrong_guesses and "_" in display:

    print(hangman_stages[wrong_guesses])
    print("Word:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    guess = input("\nGuess a letter: ").lower()

    # Check whether input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check whether letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:

        print("Correct!")

        # Reveal the correct letter
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:

        print("Wrong guess!")
        wrong_guesses += 1


# Game result
if "_" not in display:

    print("\n" + "=" * 35)
    print("       YOU WON!")
    print("=" * 35)
    print("The word was:", word)

else:

    print(hangman_stages[6])

    print("\n" + "=" * 35)
    print("       GAME OVER!")
    print("=" * 35)
    print("The word was:", word)


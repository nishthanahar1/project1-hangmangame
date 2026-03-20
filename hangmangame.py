import random

# Hangman stages (animation)
stages = [
    """
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """
]

# Word list
words = ["apple", "tiger", "chair", "plant", "bread"]
word = random.choice(words)

# Game variables
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("Welcome to Hangman!")
print(" ".join(guessed_word))
print(stages[attempts])

# Game loop
while "_" in guessed_word and attempts > 0:
    guess = input("Guess a letter: ").lower()

    # Prevent repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

    print(stages[attempts])  # show hangman
    print(" ".join(guessed_word))

# Final result
if "_" not in guessed_word:
    print("🎉 You won! Word was:", word)
else:
    print(stages[0])
    print("😢 You lost! Word was:", word)

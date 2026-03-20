import random

# Step 1: word list
words = ["apple", "tiger", "chair", "plant", "bread"]

# Step 2: choose random word
word = random.choice(words)

# Step 3: create blank display
guessed_word = ["_"] * len(word)

print("Welcome to Hangman!")
print(" ".join(guessed_word))

# Step 4: game loop (basic)
while "_" in guessed_word:
    guess = input("Guess a letter: ").lower()

    if guess in word:
        print("Correct guess!")
        # reveal letters
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")

    print(" ".join(guessed_word))

print("You guessed the word:", word)

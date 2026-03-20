import random

words = ["apple", "tiger", "chair", "plant", "bread"]
word = random.choice(words)

guessed_word = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman!")
print(" ".join(guessed_word))

while "_" in guessed_word and attempts > 0:
    guess = input("Guess a letter: ").lower()

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

    print(" ".join(guessed_word))

# Final result
if "_" not in guessed_word:
    print("🎉 You won! Word was:", word)
else:
    print("😢 You lost! Word was:", word)

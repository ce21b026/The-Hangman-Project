import random

def hangman():
    words = ['apple', 'banana', 'orange', 'grape', 'strawberry'] # List of words for the game
    word = random.choice(words) # Select a random word from the list
    guessed_letters = []
    tries = 6

    while tries > 0:
        print("\n" + "-" * 20)
        print("Word:", " ".join([letter if letter in guessed_letters else "_" for letter in word]))

        if "" not in [letter if letter in guessed_letters else "" for letter in word]:
            print("Congratulations! You guessed the word correctly!")
            return

        print("Guessed letters:", ", ".join(guessed_letters))
        print("Tries left:", tries)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print("Wrong guess!")

    print("\n" + "-" * 20)
    print("Game over! You ran out of tries.")
    print(f"The word was: {word}")

hangman()
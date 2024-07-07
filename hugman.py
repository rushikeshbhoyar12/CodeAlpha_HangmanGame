import random


word_list = ["python", "hangman", "programming", "developer", "openai", "artificial", "intelligence"]



def get_random_word(word_list):
    return random.choice(word_list).upper()


def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_hangman():
    word = get_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while incorrect_guesses < max_incorrect_guesses and set(word) != guessed_letters:
        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! The word now looks like this: {display_word(word, guessed_letters)}")
        else:
            incorrect_guesses += 1
            guessed_letters.add(guess)
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} tries left.")

        print(display_word(word, guessed_letters))

    if set(word) == guessed_letters:
        print(f"Congratulations! You've guessed the word '{word}' correctly!")
    else:
        print(f"Game over! You've used all your guesses. The word was '{word}'.")



if __name__ == "__main__":
    play_hangman()

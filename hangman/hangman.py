# Get required packages
from random_word import RandomWords
hangman_pictures = {0: "", 1:'''
      +---+
      |   |
          |
          |
          |
          |
    =========''',2: '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',3: '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',4: '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',5: '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''',6: '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''',7: '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========='''}

# Generate a random word in the dictionary
def generate_random_word():
    word_class = RandomWords()
    guessable_word = word_class.get_random_word().replace("-", "").replace(" ", "")
    while len(guessable_word) < 7:
        guessable_word = word_class.get_random_word().replace("-", "").replace(" ", "")
    return guessable_word

# Play hang man
def hangman(guessable_word):
    letters_contained = list(guessable_word)
    # Get number of characters in underscore form
    word_in_underscores = ""
    for letter in letters_contained:
        word_in_underscores += "_"

    print("Ready to play hangman?")
    print("Your word is")
    print(word_in_underscores)
    print("You have 7 guesses. This word has {} characters.".format(len(word_in_underscores)))

    guess_a_letter(letters_contained, guessable_word, word_in_underscores)


def guess_a_letter(letters_contained, guessable_word, word_in_underscores):
    victory = False

    used_letters = set()
    mistakes = 0
    underscore_list = list(word_in_underscores)
    while victory is False:
        guessed_letter = input("Enter your guess:\n").lower()
        if not guessed_letter.islower():
            print("That is an invalid character.")
            continue

        if guessed_letter not in letters_contained:
            print("Uh oh. This word does not contain '{}'".format(guessed_letter))
            used_letters.add(guessed_letter)
            mistakes += 1
            if mistakes == 7:
                display_hang_man(mistakes)
                print("You're not only a murderer, but you lost!")
                exit()

        if guessed_letter in letters_contained:
            if guessed_letter in used_letters:
                print("You've already guessed that!")
                print("Used letters: " + str(used_letters).replace("{","").replace("}",""))
                continue

            print("Congratulations. That letter is in the word. Revealing location...")
            used_letters.add(guessed_letter)

            i = 0
            for letter in guessable_word:
                if guessed_letter == letter:
                    underscore_list[i] = guessed_letter
                i += 1
            word_in_underscores = ''.join(underscore_list)

            if "_" not in word_in_underscores:
                print("Congratulations. You won! The man is saved!")
                victory = True

        display_hang_man(mistakes)
        print("Used letters: " + str(used_letters).replace("{","").replace("}",""))
        print(word_in_underscores)

def display_hang_man(mistakes):
    print(hangman_pictures[mistakes])
def main():
    # Generate random word
    guessable_word = generate_random_word()
    hangman(guessable_word)

main()
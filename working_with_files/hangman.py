# Get required packages
from random_word import RandomWords

# Generate a random word in the dictionary
def generate_random_word():
    word_class = RandomWords()
    return word_class.get_random_word()

# Check word is at least 7 letters, with no spaces or dashes
def word_length_checker(guessable_word):
    if len(guessable_word) < 7:
        main()
    if "-" in guessable_word:
        main()
    if " " in guessable_word:
        main()
# Play hang man
def hangman(guessable_word):
    # Possible letters to guess list, and letters contained in the word list
    possible_guessable = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                          "t", "u", "v", "w", "x", "y", "z"}
    letters_contained = {}
    for letter in guessable_word:
        if letter not in letters_contained:
            letters_contained[letter] = 1
        else:
            letters_contained[letter] += 1
    # Get number of characters in underscore form
    word_in_underscores = ""
    while len(word_in_underscores) < len(guessable_word):
        word_in_underscores += "_"
    print("Ready to play hangman?")
    print("Your word is")
    print(word_in_underscores)
    print("You have 7 guesses. This word has {} characters.".format(len(word_in_underscores)))
    # Start guesses until the end
    # Mistake counter - maximum of 7
    mistakes = 0
    used_letters = {}
    guess_a_letter(possible_guessable, letters_contained, guessable_word, word_in_underscores, mistakes, used_letters)


def guess_a_letter(possible_guessable, letters_contained, guessable_word, word_in_underscores, mistakes, used_letters):
    hangman_pictures = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    print("Letter(s) used: " + str(list(used_letters.keys())).replace("[",  "").replace("]", ""))
    guessed_letter = input("Enter your guess:\n").lower()

    if guessed_letter not in possible_guessable:
        print("That isn't a valid guess. You have either entered it already, or it isn't a letter")
        guess_a_letter(possible_guessable, letters_contained, guessable_word, word_in_underscores, mistakes,
                       used_letters)
    if guessed_letter not in letters_contained:
        print("Uh oh. This word does not contain '{}'".format(guessed_letter))
        possible_guessable.remove(guessed_letter)
        used_letters[guessed_letter] = 1
        mistakes += 1
        if mistakes == 1:
            print(hangman_pictures[0])
            print(word_in_underscores)
        elif mistakes == 2:
            print(hangman_pictures[1])
            print(word_in_underscores)
        elif mistakes == 3:
            print(hangman_pictures[2])
            print(word_in_underscores)
        elif mistakes == 4:
            print(hangman_pictures[3])
            print(word_in_underscores)
        elif mistakes == 5:
            print(hangman_pictures[4])
            print(word_in_underscores)
        elif mistakes == 6:
            print(hangman_pictures[5])
            print(word_in_underscores)
        elif mistakes == 7:
            print(hangman_pictures[6])
            print("You are not only a murderer, but you lost.")
            print("The word was {}.".format(guessable_word))
            exit()
        guess_a_letter(possible_guessable, letters_contained, guessable_word, word_in_underscores, mistakes,
                       used_letters)
    if guessed_letter in letters_contained:
        print("Congratulations. That letter is in the word. Revealing location...")
        possible_guessable.remove(guessed_letter)
        letters_contained.pop(guessed_letter)
        used_letters[guessed_letter] = 1
        i = 0
        underscore_list = list(word_in_underscores)
        for letter in guessable_word:
            if guessed_letter == letter:
                underscore_list[i] = guessed_letter
            i += 1
        word_in_underscores = ''.join(underscore_list)
        print(word_in_underscores)
        if "_" not in word_in_underscores:
            print("Congratulations. You won! The man is saved!")
        else:
            guess_a_letter(possible_guessable, letters_contained, guessable_word, word_in_underscores, mistakes,
                           used_letters)

def main():
    guessable_word = generate_random_word()
    word_length_checker(guessable_word)
    hangman(guessable_word)

main()
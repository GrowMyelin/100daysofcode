import random
import nltk

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def main():
    word_list = nltk.corpus.words.words()
    chosen_word = random.choice(word_list)
    print(chosen_word)
    display = ["_"] * len(chosen_word)
    won = False
    lives = 6
    while not won:
        print(display)
        print(stages[lives])
        print(lives)
        correct = False
        guess = input("Guess a letter: ").lower()
        for n, letter in enumerate(chosen_word):
            if letter == guess:
                correct = True
                display[n] = guess
            else:
                pass
        if not correct:
            lives -= 1
        if "_" not in display:
            print('You won!')
            won = True
        else:
            won = False
            if lives == 0:
                print(stages[lives])
                print('You lost.')
                break


if __name__ == "__main__":
    main()
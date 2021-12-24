import random

hang = ["""
H A N G M A N
 +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N
 +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N
 +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]


def getRandomWord():
    word = random.choice(['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple',
                          'lemon', 'coconut', 'watermelon', 'cherry', 'berry', 'peach', 'frizzled',
                          'submarine', 'matrix', 'game', 'people', 'sword', 'zebra', 'grandma', 'unzip'])

    return word


def displayBoard(hang, missedLetters, correctLetters, secretWord):
    print(hang[len(missedLetters)])
    print("")

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # show secret word with spaces in between letters
        print(letter, end=' ')
    print("\n")


def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    return input("Do you want to play again?").lower().startswith('y')


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord()
gameIsDone = False

while True:
    displayBoard(hang, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("\nYes! The secret word is " + secretWord + "! You Won!")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(hang) - 1:
            displayBoard(hang, missedLetters, correctLetters, secretWord)
            print("You ran out of guesses! After " + str(len(missedLetters)) + " missed guesses and "
                  + str(len(correctLetters)) + " correct guesses, the word was '" + secretWord + "'")
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord()
        else:
            break

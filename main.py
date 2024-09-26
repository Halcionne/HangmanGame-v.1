# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:21:43 2024

@author: Lenovo
"""

import random
import string
import time
import webbrowser

hangmanASCII = ['''
  +---+
      |
      |
      |
      |
      |
=========''',
    '''
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

WORDLIST_FILENAME = "C:/Users/Lenovo/.spyder-py3/Python Scripts/Hangman game/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    matchingCase = True
    for letter in secretWord:
        if letter not in lettersGuessed:
            matchingCase = False
            return False
    if matchingCase:
        return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = []
    for letter in lettersGuessed:
        if letter not in secretWord:
            guessedWord += ""
        elif letter in secretWord:
            if secretWord.count(letter) > 1:
                for item in range(secretWord.count(letter)):
                    guessedWord.append(letter)
            else:
                guessedWord.append(letter)
    guessedLetters = guessedWord
    if guessedWord != secretWord:
        guessedWord = []
        for letter in secretWord:
            if letter in guessedLetters != letter in secretWord:
                guessedWord += letter
            else:
                guessedWord.append( "__")
    lettersGuessed = guessedWord    
    return " ".join(lettersGuessed)

alphabet = string.ascii_lowercase

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    global alphabet
    internalAlphabet = string.ascii_lowercase
    if manyLetters(lettersGuessed) == False:
        for letter in lettersGuessed:    
            if letter in internalAlphabet: 
                alphabet = alphabet.replace(letter, "") 
            elif letter not in alphabet:
                break
            else:
                print("Invalid letter detected. Please input a letter!")

    return alphabet

def startSequence(userChoice):
    '''
    userChoice: string, whether the game starts or not
    
    Returns:
    True or False or Something devious
    '''
    positiveSeq = ["start", "go", "yes", "yeah", "ye", "yep", "yup"]
    negativeSeq = ["stop", "nope", "nuhuh", "no", "nah"]
    kayoSeq = ["negative", "affirmative"]
    if userChoice in positiveSeq:
        return True
    elif userChoice in negativeSeq:
        return False
    elif userChoice == "meow":
        webbrowser.open("https://www.youtube.com/watch?v=0tOXxuLcaog")
        return None
    elif userChoice in kayoSeq:
        webbrowser.open("https://youtu.be/PneEoLXIEUI?t=12")
        return None
    else:
        print("Your invalid choice caused Hangman's mind to explode, please try again!")
        return print("Valid entries accepted are: " + str(" ".join(positiveSeq)) + " " + str(" ".join(negativeSeq)) + " " + str(" ".join(kayoSeq)) + " and meow...")

def manyLetters(lettersGuessed):
    letters = 0
    for letter in lettersGuessed: 
        letters += lettersGuessed.count(letter)
    if letters > 1:
        return True
    else:
        return False  
def illustrationHanging(deathCount):
    if deathCount == 0:
        print("")
        print("Hangman's gallow has been made.")
        print(f"{hangmanASCII[deathCount]}")
        time.sleep(1)
        print("Hangman still trusts you though. Don't let him down!")
        time.sleep(2)
    elif deathCount ==1:
        print("")
        print("Hangman's hanging is proceeding.")
        time.sleep(1)
        print(hangmanASCII[deathCount])
    elif deathCount ==2:
        print("")
        print("Hangman's hanging is proceeding.")
        time.sleep(1)
        print(hangmanASCII[deathCount])
    elif deathCount ==3:
        print("")
        print("Hangman's hanging is proceeding.")
        time.sleep(1)
        print("Hangman says he will be hung if you fail four more times.")
        time.sleep(1)
        print("Be careful what you guess next!")
        time.sleep(1.5)
        print(hangmanASCII[deathCount])
    elif deathCount ==4:
        print("")
        print("Hangman's hanging is proceeding.")
        time.sleep(1)
        print("Hangman says he will be hung if you fail three more times.")
        time.sleep(1)
        print("Be careful what you guess next!")
        time.sleep(1.5)
        print(hangmanASCII[deathCount])
    elif deathCount ==5:
        print("")
        print("Hangman's hanging is proceeding.")
        time.sleep(1)
        print("Hangman is now scared.")
        time.sleep(1)
        print("Hangman's trust in you wavers.")
        time.sleep(1.5)
        print(hangmanASCII[deathCount])
    elif deathCount ==6:
        print("")
        print("Hangman's life is hanging by a thread!")
        time.sleep(1)
        print("Hangman screams to bring another defendant.")
        time.sleep(1)
        print("Hangman no longer trusts you.")
        time.sleep(1)
        print("Hangman will be hung if you fail once more!")
        time.sleep(1.5)
        print(hangmanASCII[deathCount])
    elif deathCount ==7:
        print("")
        print("Hangman has been hung!")
        time.sleep(1.5)
        print(hangmanASCII[deathCount])
        time.sleep(1)
        print("Hangman curses at you from the afterlife.")
        time.sleep(1)
        print("Try again.")
        
def emptyChar(chars):
    
    for char in range(int(chars)):
        print("")

def hangman():
    '''
    secretWord: string, the secret word to guess
    Starts up an interactive game of Hangman
    * At the start of the game, let the user know how many 
      letters the secretWord contains
    * Ask the user to supply one guess (i.e. letter) per round
    * The user should receive feedback immediately after each guess 

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed
    Follows the other limitations detailed in the problem write-up
    '''
    score = 0
    hungCount = 0
    lettersGuessed = []
    alreadyGuessed = []
    time.sleep(1)
    print("Welcome to the game, Hangman!"); time.sleep(2)
    print("Guess the letters in a random word."); time.sleep(2)
    print("If your letter is actually a part of the word it is added to the spelling."); time.sleep(2)
    print('If not. Hangman is slowly led towards death.'); time.sleep(2)
    print("If you guess a wrong letter 8 times Hangman is hung"); time.sleep(2)
    print(f' {hangmanASCII[7]}'); time.sleep(1)
    userChoice = input("Are you ready to save Hangman?: ").lower()
    if startSequence(userChoice):
        gamesCount = int(input("How many games would you like to play?: "))
        for game in range(gamesCount):
            deathCount = 0
            userGuesses = 8
            isHung = False
            secretWord = chooseWord(wordlist)
            print("I am thinking of a word that is " + str(len(secretWord)) + " letters long."); time.sleep(3)
            while isWordGuessed(secretWord, lettersGuessed) == False and isHung == False:
                time.sleep(1)
                print("-------------")
                print("You have " + str(userGuesses) + " guesses remaining.")
                print("Available letters: " + str(getAvailableLetters(lettersGuessed)))
                guessedWord = getGuessedWord(secretWord, alreadyGuessed)
                if hungCount == gamesCount:
                    time.sleep(1)
                    emptyChar(1)
                    print("Your lost all your games! Better luck next time!")
                    emptyChar(1)
                if guessedWord.replace(" ", "") == secretWord:
                    score+=1
                    time.sleep(1)
                    emptyChar(1)
                    print("Congratulations, you won!")
                    emptyChar(1)
                    print("The word was: " + str(secretWord))
                    emptyChar(2)
                    break
                elif userGuesses == 0:
                    illustrationHanging(7)
                    isHung = True
                    hungCount += 1
                    time.sleep(1)
                    emptyChar(1)
                    print('Sorry, you ran out of guesses. The word was ' + secretWord +'.')
                    emptyChar(1)
                    break
                elif userGuesses > 0:
                    time.sleep(1)
                    lettersGuessed = input("Please guess a letter: ").lower()
                    emptyChar(1)
                    if manyLetters(lettersGuessed) == False:
                        if lettersGuessed in alreadyGuessed:
                            time.sleep(1)
                            emptyChar(1)
                            print("Oops! You've already guessed that letter!")
                            print(str(getGuessedWord(secretWord, alreadyGuessed)))
                            emptyChar(1)
                        elif lettersGuessed in secretWord:
                            alreadyGuessed += lettersGuessed
                            time.sleep(1)
                            emptyChar(1)
                            print("Well done! This fits right in!")
                            emptyChar(2)
                            print(str(getGuessedWord(secretWord, alreadyGuessed)))
                            emptyChar(2) 
                        elif lettersGuessed not in secretWord:
                            if lettersGuessed in alreadyGuessed: 
                                time.sleep(1)
                                emptyChar(1)
                                print("Oops! You've already guessed that letter!")
                                emptyChar(2) 
                                print(str(getGuessedWord(secretWord, alreadyGuessed)))
                                emptyChar(2)
                            else:
                                alreadyGuessed += lettersGuessed
                                time.sleep(1)
                                print("Oops! That letter is not in my word!")
                                emptyChar(2) 
                                print(str(getGuessedWord(secretWord, alreadyGuessed)))
                                emptyChar(2) 
                                userGuesses -= 1
                                illustrationHanging(deathCount)
                                deathCount += 1
                        else:
                            return print("There has been an error somewhere, please try again!")
                        # elif getGuessedWord(secretWord, lettersGuessed) == False:
                        #     print("meow")
                    elif manyLetters(lettersGuessed) == True:
                        print("Please type one letter at a time, or the full guess!")
    else: 
        time.sleep(3)
        print("That's unfortunate..."); time.sleep(3)
        print("Feel free to re-run the code whenever you want to start and enter 'start' on prompt!"); time.sleep(3)
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
hangman()
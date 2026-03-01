<<<<<<< HEAD
from colorama import init, Fore, Back, Style
import getpass
import random
#import pygame
import sys
import time

#pygame.mixer.init()
#init(autoreset=True)

frequency = [
        "e",
        "t",
        "a",
        "o",
        "i",
        "n",
        "s",
        "r",
        "h",
        "d",
        "l",
        "u",
        "c",
        "m",
        "f",
        "y",
        "w",
        "g",
        "p",
        "b",
        "v",
        "k",
        "x",
        "q",
        "j",
        "z"
        ]
    
def choose_word() -> str:
    #This will be opening a text file for a large list of words instead of being hardcoded
    words = []
    with open("words.txt",  "r") as file:
        lines = file.read().splitlines()
    
    return random.choice(lines)
class Hangman:
    def __init__(self):
        self.word = choose_word()
        self.word_completion = "_" * len(self.word)
        self.tries = 6
        self.guessed_letters = []
def computer_guess(freq: list[str], guessed: list[str]) -> str:
    # Here is where the "computer" will detemine it's guess.
    sub_letters = freq[0:6]
    even_more_subbed = freq[6:27]
    filterd1 = [letter for letter in sub_letters if letter not in guessed] 
    filterd2 = [letter for letter in even_more_subbed if letter not in guessed]
    if filterd1 != []:
        random_letter1 = random.choice(filterd1)
        return random_letter1
    else:  
        random_letter2 = random.choice(filterd2)
        return random_letter2



=======
import getpass
import random


def choose_word() -> str:
    words: list[str] = [
        "silever",
        "diamond",
        "emerald",
        "gold",
        "opal",

    ]
    return random.choice(words)
    
>>>>>>> 7dad4677a2fee80a347b6f675bf0b4cdcfbd2543
def display_hangman(tries: int) -> None:
    """ Displays the current stage oh hangman """
    stages: list[str] = [
            """
            ------------
            |          |    
            |          O
            |         \\|/ 
            |          |
            |         / \\
            |
           - --
            """,
            """
            ------------
            |          |    
            |          O
            |         \\|/ 
            |          |
            |         / 
            |
           - --
            """,
            """
            ------------
            |          |    
            |          O
            |         \\|/ 
            |          |
            |        
            |
           - --
            """,
            """
            ------------
            |          |    
            |          O
            |         \\| 
            |          |
            |       
            |
           - --
            """,
            """
            ------------
            |          |    
            |          O
            |          |
            |          |
            |        
            |
           - --
            """,
            """
            ------------
            |          |    
            |          O
            |              
            |           
            |             
            |
           - --
            """,
            """
            ------------
            |          |    
            |           
            |              
            |           
            |             
            |
           - --
            """,
    ]   
    print(stages[tries])
def display_game(tries: int, word_completion: str) -> None:
    display_hangman(tries)
    #Display the ______
    print(word_completion)
    print()
<<<<<<< HEAD
def play_hangman() -> None:
    game = Hangman()
    print()
    print("Welcome to Hangman!")
    print()
    print("Let's play!")
    display_game(game.tries, game.word_completion)

    while not guessed and game.tries > 0:
=======

def play_hangman() -> None:
    print()
    print("Welcome to Hangman!")
    print()

    #ask the user if they wna to input own word, or use a random one
    #from the list
    while True:
        user_picks_word = input("Would you like to enter your own word? (y|n): ").lower()

        if user_picks_word == "y" or user_picks_word == "n":
            break

        else:
            print("Please enter 'y' or 'n'")
    # IF the user is picking the word, get if from them now. Otherwise, pick
    #a random one from our list. 

    if user_picks_word =="y":
        word = getpass.getpass("Enter the word to guess: ")
    else:
        word = choose_word()
    # This will be the underscores showing the letters
    word_completion = "_" *len(word)
    
    #this will be set to True if the word get successfully guess which will end the game
    guessed = False

    #keeps track of the letters being guessed, preventing duplicates
    guessed_letters: list[str] = []

    #Number of tries. This is used to determine which stage of the hangman process we are in
    tries = 6

    print("Let's play!")
    display_game(tries, word_completion)

    while not guessed and tries > 0:
>>>>>>> 7dad4677a2fee80a347b6f675bf0b4cdcfbd2543
        guess = input("Please guess a letter: ").lower()

        # Make sure they give a valid letter
        if len(guess) == 1 and guess.isalpha():
<<<<<<< HEAD
            if guess in game.guessed_letters:
                print(f"You already guessed the letter{guess}")

            #wrong guess
            elif guess not in game.word:
                print(Fore.RED + f"{guess} is not in the word.")

                game.tries -= 1
                game.guessed_letters.append(guess)
                print(game.guessed_letters)

            else:
                print(Fore.GREEN + f"Good job, {guess} is in the word!")
 
                game.guessed_letters.append(guess)
                
                #make the _ _  _  _ thing
                word_as_list = list(game.word_completion)
                indices: list[int] = [i for i, letter in enumerate(game.word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                game.word_completion = "".join(word_as_list)

                #Check if they've won
                if "_" not in game.word_completion:
=======
            if guess in guessed_letters:
                print(f"You already guessed the letter{guess}")

            #wrong guess
            elif guess not in word:
                print(f"{guess} is not in the word.")

                tries -= 1
                guessed_letters.append(guess)

            else:
                print(f"Good job, {guess} is in the word!")

                guessed_letters.append(guess)
                
                #make the _ _  _  _ thing
                word_as_list: list[str] = list(word_completion)
                indices: list[int] = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

                #Check if they've won
                if "_" not in word_completion:
>>>>>>> 7dad4677a2fee80a347b6f675bf0b4cdcfbd2543
                    guessed = True

        else:
            print("Invalid input, please enter a single letter.")

<<<<<<< HEAD
        display_game(game.tries, game.word_completion)
=======
        display_game(tries, word_completion)
>>>>>>> 7dad4677a2fee80a347b6f675bf0b4cdcfbd2543

    if guessed:
        print("Congratulations, you guessed the word! You win!")

    else:
<<<<<<< HEAD
        print(f"Sorry, you ran out of tries. The word was {game.word} Maybe next time!.")

computer_guess(frequency, [])
=======
        print(f"Sorry, you ran out of tries. The word was {word} Maybe next time!.")


>>>>>>> 7dad4677a2fee80a347b6f675bf0b4cdcfbd2543
play_hangman()


from colorama import init, Fore, Back, Style
import getpass
import random
#import pygame
import os
import sys
import time

#pygame.mixer.init()
init(autoreset=True)

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
def wait_times():
    time.sleep(2)
def computer_guess(freq: list[str], guessed: list[str], complete_word: str, secret_word: str) -> str:
    #Computer automatically wins if only one letter left on it's turn

    if complete_word.count("_") == 1:
        for letter, blank in zip(complete_word, secret_word):
            if letter == "_":
                return blank
    # Here is where the "computer" will detemine it's guess.

    # I splice the freq list so it will choose the most popular letters first
    sub_letters = freq[0:6]
    # If will use all the sub_letters first then move on to even_more_subbed

    even_more_subbed = freq[6:27]
    filtered1 = [letter for letter in sub_letters if letter not in guessed] 
    filtered2 = [letter for letter in even_more_subbed if letter not in guessed]
    if filtered1 != []:
        random_letter1 = random.choice(filtered1)
        return random_letter1
    else:  
        random_letter2 = random.choice(filtered2)
        return random_letter2

def user_word_guess(correct_word: str, guess: str) -> bool:
    if guess == correct_word:
        print("Thats right! You win!")
        sys.exit(0)
        return True
    else:
        print("Sorry that is not right, you lose a life")
        return False

def clear_screen():
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

def user_vs_computer():
    game = Hangman()
    guessed = False
    user_tries = 6
    computer_tries = 6
    all_guessed = []
    current_player = "human"
    #user_guessed = []
    #computer_guessed = []
    print()
    print("Welcome to computer vs player Hangman!")
    print("You will alternate guessing letters with the computer, first to guess the word wins!")
    print()

    # Player will go first.
    while not guessed and user_tries > 0 and computer_tries > 0:
        valid_turn = True
        if valid_turn == True:
            print()
            print(Fore.MAGENTA + "Player")
            display_game(user_tries, game.word_completion)
            # Seeing if player knows the word
            choice1 = input("Do you think you know the word? y/n: ")
            if choice1 == "y":
                guess = input("Make your guess: ")
                result = user_word_guess(game.word, guess)
                #if player guessed right, game finished in user_guessed
                #if player get it wrong, return False and loses life
                #if player doesn't guess word, game moves on like normal
                if result is False:
                    user_tries -= 1
                    valid_turn = False
            if valid_turn == True:
                print(all_guessed)
                guess = input("Please guess a letter: ").lower()
                # Making sure it's the right guess
                if len(guess) == 1 and guess.isalpha():
                        if guess in all_guessed:
                            print(f"You already guessed the letter {guess}. Please try again.")
                        
                        # User wrong guess
                        elif guess not in game.word:
                            print(Fore.RED + f"{guess} is not in the word.")
                            user_tries -= 1
                            print(user_tries)
                            all_guessed.append(guess)
                            print(all_guessed)
                        # User right Guess
                        elif guess in game.word:
                            all_guessed.append(guess)
                            print(Fore.GREEN + f"{guess} is in the word!")
                            print(all_guessed)  

                            word_as_list = list(game.word_completion)
                            indices: list[int] = [i for i, letter in enumerate(game.word) if letter == guess]
                            for index in indices:
                                word_as_list[index] = guess
                            game.word_completion = "".join(word_as_list)

                            if "_" not in game.word_completion:
                                current_player = "human"
                                guessed = True
                                break
                            wait_times()

        #Computers turn

        current_player = "computer" 
        guessed_letter = computer_guess(frequency, all_guessed, game.word_completion, game.word)
        print()
        print(Fore.BLUE + "Computer")
        display_game(computer_tries, game.word_completion)
        wait_times()
        print(f"Computers guess was {guessed_letter}.")
        # Computer wrong guess
        if guessed_letter not in game.word:
            print(Fore.RED + f"{guessed_letter} is not in the word.")
            wait_times()
            all_guessed.append(guessed_letter)
            print(all_guessed)
            computer_tries -= 1
            print(computer_tries)
        # Computer right guess
        else:
            print(Fore.GREEN + f"{guessed_letter} is in the word!")
            all_guessed.append(guessed_letter)
            print(all_guessed)
            word_as_list = list(game.word_completion)
            indices: list[int] = [i for i, letter in enumerate(game.word) if letter == guessed_letter]
            for index in indices:
                word_as_list[index] = guessed_letter
            game.word_completion = "".join(word_as_list)
        
            if "_" not in game.word_completion:
                guessed = True
                break
        clear_screen() 

    if current_player == "human" and guessed == True:                
        print("You win!")    
        
    elif current_player == "computer" and guessed == True:
        print("Sorry, you lose.")

    elif user_tries == 0 and computer_tries > 0:
        print("Computer wins because you ran out of tries first.")

    elif computer_tries == 0 and user_tries > 0:
        print("You win because the computer ran out of tries!")



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
def play_hangman() -> None:
    game = Hangman()
    guessed = False
    print()
    print("Welcome to Hangman!")
    print()
    print("Let's play!")
    display_game(game.tries, game.word_completion)

    while not guessed and game.tries > 0:
        guess = input("Please guess a letter: ").lower()

        # Make sure they give a valid letter
        if len(guess) == 1 and guess.isalpha():
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
                    guessed = True

        else:
            print("Invalid input, please enter a single letter.")

        display_game(game.tries, game.word_completion)

    if guessed:
        print("Congratulations, you guessed the word! You win!")

    else:
        print(f"Sorry, you ran out of tries. The word was {game.word} Maybe next time!.")
user_vs_computer()
#computer_guess(frequency, [])
#play_hangman()






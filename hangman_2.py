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
        guess = input("Please guess a letter: ").lower()

        # Make sure they give a valid letter
        if len(guess) == 1 and guess.isalpha():
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
                    guessed = True

        else:
            print("Invalid input, please enter a single letter.")

        display_game(tries, word_completion)

    if guessed:
        print("Congratulations, you guessed the word! You win!")

    else:
        print(f"Sorry, you ran out of tries. The word was {word} Maybe next time!.")


play_hangman()

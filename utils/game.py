import random

class Hangman():
    def __init__(self, possible_words):
        # initiating the attributes turn count, error count (both 0 at start of game)
        # intiate lives (standard = 5)
        # initiate the possible words (can adjust or add words in this list if needed)
        self.turn_count = 0
        self.error_count = 0
        self.lives = 5
        self.possible_words = possible_words
        # the word to find is linked to the possible words, we choose one random word out of the possible words list
        self.word_to_find = []
        # pick a random word out of the list of possible words
        for i in random.choice(self.possible_words):
            #we append each letter of the random word to the word_to_find list 
            self.word_to_find.append(i.upper())
        # the guessed correctly variable is linked to the word to find variable (same length)
        # use list comprehension to create the correctly guessed letters var
        self.correctly_guessed_letters=["_" for x in range(len(self.word_to_find))]
        # set wrongly guessed letters to empty list (no guesses / wrong guesses at start of game)
        self.wrongly_guessed_letters = []

    # initialize the play method
    def play(self):
        # make While True loop (so the input will keep being asked as long as the input is not correct)
        while True:
            # start of the turn so we add 1 to the turn counter
            self.turn_count +=1
            player_input = input("Please input 1 letter you want to guess: ")
            # checking if the length of the player_input is more than 1 - if so > deny the input and return to the Input()
            if len(player_input) > 1:
                print("Please return only 1 input, please try again ...")
                print(self.correctly_guessed_letters)
                continue

            # filter out the special characters + filter out if its a number (return to Input if it is)
            special_characters = '"!@#$%^&*()-+?._=,<>/"'
            if player_input.isdigit() or player_input in special_characters:
                print("Please return a letter - not a number or special character, try again ...")
                # print the  _ _ _ _ _ (depending on length of letters - just to make it nice for the player visually)
                print(self.correctly_guessed_letters)
                continue
            else:
                # standardize the player input so it prints out uppercase letters + so we are not comparing lower and uppercases
                player_input = player_input.upper()
                # check if the letter that has been entered by the player is in the list of the letters of the word to find
                if player_input in self.word_to_find:
                    # if the player input is repeated more than once in the word to find we need to get both indices of the location of the letter
                    indices = []
                    # using enumerate to get the indices of the letters in the word to find
                    for i, letter in enumerate(self.word_to_find):
                        if player_input == letter:
                            indices.append(i)
                    # once we have the indices, we will replace the player input letters into the correctly guessed letters
                    for i in indices:
                        # so correctly guessed letter ar index i will be player input (and we iterate over all of the items in index (1 or more))
                        self.correctly_guessed_letters[i] = player_input
                    break
                # if the player_input is not already present in the wrongly guessed letters (because i dont want to repeat the wrong letters if the players guesses it wrong twice)
                else:
                    if player_input not in self.wrongly_guessed_letters: 
                        # add the player input in the wrongly guessed letter only once
                        self.wrongly_guessed_letters.append(player_input)
                    # increment de error count because player had it wrong
                    self.error_count += 1
                    # remove 1 life because player had it wrong
                    self.lives -= 1
                    break

    #initialize the game_over method                
    def game_over(self):
        # printing some visuals to help the player
        print("[!!!] Game Over - You have lost all your lives! [!!!]")
        print("#### YOUR END RESULT ####")
        # Summarizing the correctly guessed letters when game over so the players knows what he is missing
        print(self.correctly_guessed_letters)
        print("#### THE WORD WE WERE LOOKING FOR WAS ####")
        # Showing the actual word we were looking for
        print(self.word_to_find)
        # exiting the program as the game is over
        exit()
    
    # initialize the well_played method 
    def well_played(self):
        print("\n")
        print(f"[!*!] You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors! [!*!]")
        exit()

    # initialize the start_game method
    def start_game(self):
        # start game with welcome message + print a fancy ASCII art banner
        print("------------ Welcome to Hangman! ------------")
        print("""   _    _                   __  __             
 | |  | |                 |  \/  |            
 | |__| | __ _ _ __   __ _| \  / | __ _ _ __  
 |  __  |/ _` | '_ \ / _` | |\/| |/ _` | '_ \ 
 | |  | | (_| | | | | (_| | |  | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_|  |_|\__,_|_| |_|
                      __/ |                   
                     |___/                     """)
        print("---------------------------------------------")
        print("[?] What word are we looking for [?]")
        print("---------------------------------------------")
        # print the correctly guessed letters (which will be blank because we are just starting the game)
        print(self.correctly_guessed_letters)
        print("---------------------------------------------")
        # start while True loop to check if the player still has lives / and if the word is guessed already or not
        while True:
            # if no more lives then it's game over
            if self.lives == 0:
                Hangman.game_over(self)
            # if the correctly guessed letters are the same as the word we need to find then player won the game
            elif self.correctly_guessed_letters == self.word_to_find:
                Hangman.well_played(self)
            # if both conditions are not met we will play the game
            Hangman.play(self)
            # after each iteration of the play method we will print the current status
            print(f"Letters you have right: {self.correctly_guessed_letters}, Wrong: {self.wrongly_guessed_letters}, lives: {self.lives}, errors: {self.error_count}, turns: {self.turn_count}")
            


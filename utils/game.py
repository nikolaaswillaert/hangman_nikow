import random

class Hangman():
    def __init__(self):
        self.turn_count = 0
        self.error_count = 0
        self.lives = 5
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = []
        for i in random.choice(self.possible_words):
            self.word_to_find.append(i.upper())
        self.correctly_guessed_letters=["_" for x in range(len(self.word_to_find))]
        self.wrongly_guessed_letters = []

    def play(self):
        while True:
            self.turn_count +=1
            player_input = input("Please input 1 letter you want to guess: ")
            if len(player_input) > 1:
                print("Please return only 1 input, please retry")
                print(self.correctly_guessed_letters)
                continue
            
            special_characters = '"!@#$%^&*()-+?._=,<>/"'
            if player_input.isdigit() or player_input in special_characters:
                print("Please return a letter - not a number or special character")
                print(self.correctly_guessed_letters)
                continue
            else:
                player_input = player_input.upper()
                if player_input in self.word_to_find:
                    indices = []
                    for i, letter in enumerate(self.word_to_find):
                        if player_input == letter:
                            indices.append(i)
                    for i in indices:
                        self.correctly_guessed_letters[i] = player_input
                    break
                else:
                    if player_input not in self.wrongly_guessed_letters: 
                        self.wrongly_guessed_letters.append(player_input)
                    self.error_count += 1
                    self.lives -= 1
                    break

    def game_over(self):
        print("[!!!] Game Over - You have lost all your lives! [!!!]")
        print("#### YOUR END RESULT ####")
        print(self.correctly_guessed_letters)
        print("#### WORD WE WERE LOOKING FOR WAS ####")
        print(self.word_to_find)

        exit()
        
    def well_played(self):
        print("\n")
        print(f"[!*!] You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors! [!*!]")
        exit()

    def start_game(self):
        print("----------- Welcome to Hangman! -----------")
        print(self.correctly_guessed_letters)
        while True:
            if self.lives == 0:
                Hangman.game_over(self)
            elif self.correctly_guessed_letters == self.word_to_find:
                Hangman.well_played(self)

            Hangman.play(self)
            print(f"correct: {self.correctly_guessed_letters}, wrong: {self.wrongly_guessed_letters}, life: {self.lives}, error: {self.error_count}, turns: {self.turn_count}")
            


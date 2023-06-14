import random

class Hangman():
    def __init__(self, turn_count=0, error_count=0, lives=5):
        self.turn_count = 0
        self.error_count = 0
        self.lives = 5
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = []
        for i in random.choice(self.possible_words):
            self.word_to_find.append(i.upper())
        
        print(self.word_to_find)
        print(len(self.word_to_find))
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

            if player_input.isdigit():
                print("Please return a letter - not a number")
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
                    self.wrongly_guessed_letters.append(player_input)
                    self.error_count += 1
                    self.lives -= 1
                    break

    def game_over(self):
        print(self.correctly_guessed_letters)
        print(self.word_to_find)
        print("Game Over - You have lost all your lives! ")
        exit()
        
    def well_played(self):
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")
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
            


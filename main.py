from utils.game import Hangman

def main():
    possible_words = ['becode', 'learning', 'mathematics', 'sessions']
    game = Hangman(possible_words)
    game.start_game()

if __name__ == '__main__':
    main()
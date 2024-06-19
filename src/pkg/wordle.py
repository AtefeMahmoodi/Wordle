import random
from src.utils import  print_error, print_success, print_warning


random.seed(45)

class Wordle:
    def __init__(self, file_path: str, word_len: int = 5, limit: int = 10000):
        self.word_len = word_len

        self.words = self.generate_word_frequency(file_path, word_len, limit)

    def generate_word_frequency(self, file_path: str, word_len: int = 5, limit: int = 1000):
        #Read Data
        words = []
        with open(file_path) as f:
            for line in f:
                word, frequency = line.split(', ')
                words.append((word, int(frequency)))

        #Sort Data
        words = sorted(words, key=lambda w: w[1], reverse=True)

        #Limit Data
        words = words[:limit]

        #Drop Frequency Data
        words = [w[0] for w in words]

        #Filter 5 Letter Data
        words = list(filter(lambda w: len(w) == word_len, words))

        return words

    def run(self):
        #random Word
        word = random.choice(self.words)

        #start Game
        num_try = 6
        success = False

        while num_try:
            guess_word = input(f"Enter a {self.word_len} word or press q to exit:")
            if guess_word == 'q':
                break
    
            #Word Length
            if len(guess_word) != self.word_len:
                print(f'Word must have {self.word_len} letters. You entered {len(guess_word)}.')
                continue
    
            #Check Valid word
            if guess_word not in self.words:
                print_warning('Word is not valid!')
    
            #check Valid, invalid position, invalid character
            for w_letter, g_letter in zip(word, guess_word):
                if w_letter == g_letter:
                    print_success(f' {g_letter} ', end='')
                    print(' ', end='')
                elif g_letter in word:
                    print_warning(f' {g_letter} ', end='')
                    print(' ', end='')
                else:
                    print_error(f' {g_letter} ', end='')
                    print(' ', end='')
            print()

            #check success
            if guess_word == word:
                print('\n')
                print_success('Congratulations!', end='')
                success = True
                break
    
            num_try -= 1
        if not success:
            print_warning(f'Game over! The word was "{word}"')
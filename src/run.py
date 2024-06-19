from src.pkg.wordle import Wordle

file_path = './src/data/words_frequency.txt'
word_len = 5
limit = 10000
wordle = Wordle(file_path, word_len, limit)

wordle.run()

# What is Wordle
Wordle is a word game, which recently got very popular and was added to NYT Games website. It is developed by Josh Wardle. You can find the original game [here](https://www.nytimes.com/games/wordle/index.html). However, you can only play it once a day.

Luckily, in this version of Wordle that you are going to be programming, you will be able to play as many times as you want in a day. Moreover, you will be allowed to see which words could potentially be the right answer. What is more, you will be using a bigger data set than the actual Wordle, which basically involves all the 5 letter words in a Scrabble dictionary.

## Rules

- The player enters a random 5-letter word.
- If the random word is the word to be guessed, the game is over. The player receives a congratulations message.
- If the random word isn’t the word to be guessed, the player is informed about whether the right letter is at the right place and if some of the letters are in the word but wrongly placed.
- Based on this, the player has 6 tries to guess the word.
- At the end of the 6 attempts, if the player fails to guess the right word, the word is revealed.

## How to Run

- Clone the repository and `cd` into it.
- Install the requirements by running `pip install -r requirements.txt`.
- In your terminal, run `export PYTHONPATH=$PYTHONPATH:$(pwd)` to add the current directory to your `PYTHONPATH`.
- Run `python src/wordle.py` to start the game.

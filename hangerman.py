# # print("hi")


# """
# The following are the requirements of the submission -

# 1. The Hangman game should ask the Name of the User. :
# 2. The user should get 3 chances to guess the word. :heavy_check_mark:
# 3. There should be at least 5 words added to the game for the user to guess. :heavy_check_mark:
# 4. If the user guesses the correct character there should be a response. Otherwise, notify the user that they made a mistake. :heavy_check_mark:
# 5. If the user is able to guess all the characters of the word within the maximum number of attempts, they win the game. :heavy_check_mark:
# 6. If the user exhausts all their attempts before guessing the entire word, they lose. :heavy_check_mark:

import random
class HangmanGame:
    def __init__(self):
        self.words = ["banana", "watermelon", "apple", "orange", "grapes"]

    @property
    def random_word(self):
        self.word = random.choice(self.words)
        return self.word

    def start_game(self):
        self.name = input("\nEnter your name: ")
        print(f"Welcome, {self.name}!")

        while True:
            key = input("\nEnter 's' to START or 'q' to QUIT: ").lower()

            if key == 's':
                chances = 3
                word_to_guess = self.random_word
                dashes = "_" * len(word_to_guess)
                print(f"\nWord to guess: {dashes}")

                while chances > 0:
                    user_guess = input("\nEnter a character to guess the word: ")
                    if user_guess in word_to_guess:
                        dashes = ''.join([char if char in dashes or char == user_guess else '_' for char in word_to_guess])
                        print(f"\nCorrect guess! Word so far: {dashes}")
                        if user_guess in dashes:
                            print("\nBUT You already guessed that letter")
                        if '_' not in dashes and  dashes == word_to_guess:
                            print(f"Congratulations!\n{self.name}  You won!!\nThe word was:  {word_to_guess}")
                            break

                    else:
                        chances -= 1
                        print(f"\nWrong guess! Remaining chances: {chances}, Word so far: {dashes}")

                        if chances == 0:
                            print(f"\nSorry, You Lose! The word was {word_to_guess}. Try again.")
                            break

            elif key == 'q':
                print("Goodbye!")
                break

if __name__ == "__main__":
    game = HangmanGame()
    game.start_game()

#   python number guess game with alexs

#  choosing a random number between 1 and 100
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#  function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number turns remaining """
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


#  make a function to set difficulty

def set_difficulty():
    level = input("choose a difficulty. Type 'easy' or 'hard' :")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("welcome to the number guessing game: ")
    print("I'm thinking of a number between 1 and 100")

    answer = random.randint(1, 100)
    print(answer)

    turns = set_difficulty()

    #  repeat the guess functionality if they get it wrong.
    guess = 0
    while guess != answer:
        #  Track the number of turns and reduce by 1 if they get it wrong
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        #  let the user guess a number
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess Again")


game()


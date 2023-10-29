#   python number guess game with alexs

#  here insert a logo don't miss
import random

print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("choose a difficulty. Type 'easy' or 'hard': ")

random_integer = random.randint(1, 100)


def guess_Game():
    def hard():
        number_of_attempts = 10
        while range(1, number_of_attempts):
            print(f"You have {number_of_attempts} attempts remaining to guess the number")
            your_guess = int(input("Make a guess: "))
            if your_guess > random_integer:
                number_of_attempts -= 1
                print("Too High")
                print("Guess again.")
            if your_guess < random_integer:
                number_of_attempts -= 1
                print("Too Low")
                print("Guess again.")
            if your_guess == random_integer:
                print("You Win")

    def easy():
        number_of_attempts_easy = 5
        while range(1, number_of_attempts_easy):
            print(f"You have {number_of_attempts_easy} attempts remaining to guess the number")
            your_guess = int(input("Make a guess: "))
            if your_guess > random_integer:
                number_of_attempts_easy -= 1
                print("Too High")
                print("Guess again.")
            if your_guess < random_integer:
                number_of_attempts_easy -= 1
                print("Too Low")
                print("Guess again.")
            if your_guess == random_integer:
                print("You Win")

    if difficulty == "hard":
        hard()
    else:
        easy()


guess_Game()

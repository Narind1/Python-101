import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Take a guess: "))
        attempts += 1

        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
import random
def guess_number_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 10)

    # Initialize variables
    attempts = 0
    guessed_number = None

    print("Welcome to the Random Number Guessing Game!")

    while guessed_number != secret_number:
        try:
            # Get user input for a guess
            guessed_number = int(input("Enter your guess (between 1 and 10): "))

            # Increment the number of attempts
            attempts += 1

            # Check if the guessed number is correct
            if guessed_number == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            elif guessed_number < secret_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    guess_number_game()

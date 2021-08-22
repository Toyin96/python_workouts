import random


def guessing_game():
    """
    A function that generates a random number between 1 - 100
    and prompts the user to guess the number correctly.
    :return: None i.e. it prints the outcome
    """

    name = input("Welcome to guessing game 1.0 \nKindly enter your name to start: ")

    while name.isdigit():
        name = input("Welcome to guessing game 1.0 \nKindly enter your name to start: ")

    counter = 3
    while counter > 0:
        num = random.randint(1, 100)
        user_input = input("Can you guess the integer generated between 0 and 100? ")

        try:
            user_input = int(user_input)
        except ValueError:
            print("You did not enter a valid integer")
        else:
            if user_input == num:
                print(f"Correct! the answer is {user_input}")
                break
            elif user_input > num:
                print(f"Your guess of {user_input} is too high. You have {counter - 1} chance left")
            elif user_input < num:
                print(f"Your guess of {user_input} is too low. You have {counter - 1} chance left")

        counter -= 1


if __name__ == "__main__":
    guessing_game()

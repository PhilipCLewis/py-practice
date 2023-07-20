# generate code
import random

# caps means constant
COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


# generate code with function
def generate_code():
    # create list that containts all elements in code
    print(f"Welcome to Mastermind, you have {TRIES} tries to guess the code...")
    print("The valid colos are", *COLORS)
    # prints welcome messages
    while True:
        user_input = input("Would you like to play? (y/n)").lower()
        if user_input == "y":
            print("Great!  Here we go!")
        elif user_input == "n":
            print("Ok, maybe next time.  Have a great day!")
            break
        else:
            print("Please choose a valid option.")
            continue

    code = []

    for _ in range(CODE_LENGTH):
        # _ can be replaced with i/x or whatever, anonymous variable
        # code will run 4 times (code_length), randonmly select four colors and add to code
        color = random.choice(COLORS)
        code.append(color)

    return code


# guess the code with function
def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")
        # .split with " " turns into list with spaces.  example: "GGGG" > ["G","G","G","G"]

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            # f string in python 3.7 or above
            continue

        for color in guess:
            # looping through colors in users guess
            # if non are in the COLORS list, try again and break out of for loop, which continues with while loop
            if color not in COLORS:
                print(f"Invalid color: {color}.  Try again.")
                break
        else:
            break
        # need break as if all colors in if loop were correct, need this break to end the while loop

    return guess


# create function to check code
def check_code(guess, real_code):
    # check correct position
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        # looping through all colors in real code, if color is not key in dictionary need to add it
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
        # no matter what, increment count for that color in the dictionary

    for guess_color, real_color in zip(guess, real_code):
        # zip - takes two arguements, combine into a list containing tuples
        # example guess = ["G", "R"]  real = ["W", "Y"]  combination would be [("G", "W"), ("R", Y)]
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1
            # gets rid of color from count since it's in correct position

        # check colors in incorrect position
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


# link components togethert with game logic


def game():
    code = generate_code()
    # generate code and for the number of attempts we have, we are going to do the following
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(
            f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}"
        )

    else:
        print("You ran out of tries, the code was:", *code)
        # asterix on code takes individual element and passes to print, which means space separated


if __name__ == "__main__":
    game()

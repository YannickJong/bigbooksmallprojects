import random
# Constant values for length of digit and the amount of guesses
NUM_DIGITS = 3
MAX_GUESSES = 10


def getSecretNum():
    """Returns a string made up from NUM_DIGITS unique random digits"""
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_number = ''
    for i in range(NUM_DIGITS):
        secret_number += numbers[i]
    return secret_number


def guessAnswer(guess, secret_number):
    """Determines what to answer to a guess (e.g. Pico, Fermi, etc.)"""
    answer = []
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            answer.append("Fermi")
        elif guess[i] in secret_number:
            answer.append("Pico")
    if len(answer) == 0:
        answer.append("Bagels")
    return " ".join(answer)


while True:
    print('''
I am thinking of a {}-digit number with no repeated numbers. Try to guess what it is.
Here are some clues:
When I say:       That means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.
You have {} guesses'''.format(NUM_DIGITS, MAX_GUESSES))
    # Generate new secret number and set guesses to 0 every time a new game starts
    guesses = 0
    secret_num = getSecretNum()
    guessed = False
    # Main game loop
    while guesses < MAX_GUESSES:
        user_input = input(f"Guess #{guesses + 1}: ")
        ans = guessAnswer(user_input, secret_num)
        guesses += 1
        if user_input == secret_num:
            print("You guessed correctly!")
            guessed = True
            break
        else:
            print(ans)

    # If all guesses have been used and the secret number has not been guessed,
    # tell the gamer they've lost
    if guessed is False:
        print("You lost! The correct number was {}!".format(secret_num))

    # Ask gamer if they want to play again
    user_input = input("Do you want to play again? (y/n) ")
    if user_input.lower().startswith("y"):
        pass
    else:
        print("Have a nice day!")
        break

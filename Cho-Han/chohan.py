import sys
import random

# Import Japanese numbers
JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}


def roll_dice():
    """Simulates rolling 2 dice """
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return d1, d2


money = 5000
print(f"""
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
""")

# Main loop
while True:
    # Kick player out if they have no money
    if money <= 0:
        print("You don't have any money left!")
        sys.exit()
    print(f"You have {money} mon. How much do you bet? (or QUIT)")
    # Ask for a bet until they give a valid answer
    while True:
        bet = input("> ")
        if bet.lower().startswith("q"):
            print("Thanks for playing!")
            sys.exit()
        if bet.isnumeric() and 0 < int(bet) <= money:
            bet = int(bet)
            break

    dices = roll_dice()
    print(f"""
The dealer swirls the cup and you hear the rattle of dice.
The dealer slams the cup on the floor, still covering the
dice and asks for your bet.

    CHO (even) or HAN (odd)?
    """)
    # Ask player for bet EVEN or ODD
    while True:
        response = input("> ")
        if response.lower().startswith("c"):
            response = "cho"
            break
        elif response.lower().startswith("h"):
            response = "han"
            break

    print(f"""
The dealer lifts the cup to reveal:
    {JAPANESE_NUMBERS[dices[0]]} - {JAPANESE_NUMBERS[dices[1]]}
    {dices[0]} - {dices[1]}
    """)
    # If % 2 == 0 it must be an even number, so if the bet/response
    # was cho (even) they win the game
    if sum(dices) % 2 == 0 and response == "cho":
        print(f"You won! You take {int(2*bet)} mon.")
        print(f"The house takes a {int(bet*0.1)} mon fee.")
        money += 0.9*bet
        money = int(money)
    # If % 2 == 1 it must be an odd number, so if the bet/response
    # was han (odd) they win the game
    elif sum(dices) % 2 == 1 and response == "han":
        print(f"You won! You take {int(2 * bet)} mon.")
        print(f"The house takes a {int(bet * 0.1)} mon fee.")
        money += 0.9 * bet
        money = int(money)
    # If they don't win with either guess, they lose
    else:
        print(f"You lost! You give the house {bet} mon.")
        money -= bet
        money = int(money)

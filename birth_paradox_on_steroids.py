import datetime
import random
import matplotlib.pyplot as plt
from playsound import playsound


def generateDate(numberOfBirthdays):
    """Generates a random date for a set amount of dates"""
    birthdays = []
    startOfYear = datetime.date(2001, 1, 1)
    for i in range(numberOfBirthdays):
        birthdays.append(startOfYear + datetime.timedelta(random.randint(0, 364)))
    return birthdays


def getMatch(birthdays):
    """Checks if multiple birthdays are occurring in a set"""
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA


# Set the amount of simulations per group of people
AMOUNT_OF_SIMS = int(1e5)

print("""
The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept by plotting the probability of
having the same birthday occur in a group against the number of people
in this group.
""")

matches_list = []
for x in range(1, 101):
    matches = 0
    print(f"Calculating for group of {x} people...")
    # Calculate the amount of matches for each group of
    # people and store them
    for i in range(AMOUNT_OF_SIMS):
        birthdays = generateDate(x)
        match = getMatch(birthdays)
        if match is not None:
            matches += 1
    matches_list.append(matches)

# With a large sample size the calculation can take quite a while
# so a 'ding' is played when the program is done calculating
playsound('ding.wav')
# Plot the calculation
plt.plot(range(1, 101), [i*100/AMOUNT_OF_SIMS for i in matches_list], "b--")
plt.grid()
plt.xlabel(r"Amount of people in group $N$ [-]")
plt.ylabel(r"Probability of same birthday in group $P$ [%]")
plt.savefig("Birthday_paradox.pdf", bbox_inches='tight')
plt.show()

import datetime, random


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
# and set a list of months in order
AMOUNT_OF_SIMS = int(1e5)
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

print("""
The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
""")

# Ask user for amount of birthdays to generate
while True:
    print("How many birthdays shall I generate? (max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBdays = int(response)
        break

print(f"""
Here are {numBdays} birthdays: 
""")

# Print a set of birthdays
birthdays = generateDate(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ", end="")
    monthName = MONTHS[birthday.month - 1]
    datetext = f"{monthName} {birthday.day}"
    print(datetext, end="")

match = getMatch(birthdays)
if match is None:
    print("\nIn this simulation, no people had the same birthday.")
else:
    print(f"\nIn this simulation, multiple people have a birthday"
          f" on {MONTHS[match.month - 1]} {match.day}.")

print(f"""
Generating {numBdays} random birthdays {AMOUNT_OF_SIMS} times...
""")

# Run the same program a set amount of times to determine
# the percentage of times the same birthday occurs
matches = 0
for i in range(AMOUNT_OF_SIMS):
    if i % 10_000 == 0:
        print(f"{i} simulations run...")
    birthdays = generateDate(numBdays)
    match = getMatch(birthdays)
    if match is not None:
        matches += 1

print(f"""
Out of {AMOUNT_OF_SIMS} simulations of {numBdays} people, there was a
matching birthday in that group {matches} times. This means
that {numBdays} people have a {round(matches*100/AMOUNT_OF_SIMS, 2)}% chance of
having a matching birthday in their group.
""")

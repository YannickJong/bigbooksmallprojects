import random
import sys


# Import symbols for the cards
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

# Set a max bet size
BACKSIDE = "backside"
MAX_BET = 5000


def getBet(maxBet):
    """Ask the player how much they want to bet for this round"""
    while True:
        bet = input("> ")
        if bet.upper() == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    """Generates a shuffled deck of cards"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for face in ("2", "3", "4", "5", "6", "7", "8", "9", "10",
             "J", "Q", "K", "A"):
            deck.append([face, suit])
    random.shuffle(deck)
    return deck


def displayCards(cards):
    """Displays cards to the player"""
    rows = ["", "", "", ""]
    for i, card in enumerate(cards):
        rows[0] += " ___ "
        if card == BACKSIDE:
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "|_##| "
            rows[0] += " "
        else:
            rank, suit = card
            rows[1] += "|{} |".format(rank.ljust(2))
            rows[2] += "| {} |".format(suit)
            rows[3] += "|_{}|".format(rank.rjust(2, "_"))
    for row in rows:
        print(row)


def getHandValue(hand):
    """Calculate the value in a hand"""
    value = 0
    numberOfAces = 0

    # Calculate value for non-ace cards
    for card in hand:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1
        elif rank in ("J", "Q", "K"):
            value += 10
        else:
            value += int(rank)

    # Add the value for the aces
    value += numberOfAces
    for i in range(numberOfAces):
        # If another 10 can be added without busting, do so
        if value + 10 <= 21:
            value += 10
    return value


def showHands(playerHand, dealerHand, showDealerHand):
    """Show hands of the player and dealer. Hide dealers first card
    if showDealerHand is set to False"""
    if showDealerHand:
        print(f"Dealer: {getHandValue(dealerHand)}")
        displayCards(dealerHand)
    else:
        print("Dealer: ???")
        displayCards([BACKSIDE] + dealerHand[1:])

    print(f"Player: {getHandValue(playerHand)}")
    displayCards(playerHand)


def getMove(playerHand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for stand
     and 'D' for double down."""
    # Keep asking until a valid choice is made
    while True:
        # Determine what moves the player can do
        moves = ["(H)it", "(S)tand"]

        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")

        # Get the players move
        print("Would you like to: ")
        movePrompt = ', '.join(moves) + '? > '
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move
        if move == "D" and "(D)ouble down" in moves:
            return move


print("""
Rules:
    Try to get as close to 21 without going over.
    Kings, Queens and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.""")

# Set starting money
money = 5000

# Main loop
while True:
    # Don't let the player play if they have no money
    if money <= 0:
        print("You're broke! Good thing you weren't playing with real money...")
        break
    print(f"""
Money: ${money}
How much do you bet? ($1-${MAX_BET}, or QUIT)""")

    # Ask how much the player wants to bet and generate a deck
    bet = getBet(money)
    deck = getDeck()

    # Give the dealer and player both 2 cards
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]

    print(f"""
Bet: {bet}
    """)
    # Main game loop, asks for moves
    while True:
        showHands(playerHand, dealerHand, False)

        # Check if player has bust
        if getHandValue(playerHand) > 21:
            break

        # Get the players move, either H, S, or D
        move = getMove(playerHand, money-bet)

        # Handle the move
        if move == "D":
            print("How much do you want to bet extra?")
            additionalBet = getBet(min(bet, (money - bet)))
            bet += additionalBet
            print(f"Bet increased to ${bet}!")

        if move in ("D", "H"):
            newCard = deck.pop()
            rank, suit = newCard
            print(f"You drew the {rank} of {suit}!")
            playerHand.append(newCard)

            if getHandValue(playerHand) > 21:
                break

        # If the move is double down, 1 card should be drawn, which was done in the last few lines
        # so here the move loop stops for double down
        if move in ("S", "D"):
            break

    # If player hasn't busted, let the dealer draw cards
    if getHandValue(playerHand) <= 21:
        while getHandValue(dealerHand) < 17:
            # Dealer hits
            print("The dealer hits...")
            dealerHand.append(deck.pop())
            showHands(playerHand, dealerHand, False)

            # Dealer busts
            if getHandValue(dealerHand) > 21:
                break
            input("Press enter to continue...")
            print("\n\n")

    # Show the final hands
    showHands(playerHand, dealerHand, True)

    # Calculate player and dealer values
    playerValue = getHandValue(playerHand)
    dealerValue = getHandValue(dealerHand)

    if dealerValue > 21:
        print(f"Dealer bust! You won ${bet}!")
        money += bet
    elif playerValue > 21:
        print(f"You bust! You lost ${bet}!")
        money -= bet
    elif playerValue > dealerValue:
        print(f"You won! Here's ${bet}!")
        money += bet
    elif playerValue < dealerValue:
        print(f"You lost ${bet}!")
        money -= bet
    elif playerValue == dealerValue:
        print(f"You tied!")


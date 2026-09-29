import random

small_blind = 1
big_blind = 2

suits = ["S", "C", "D", "H"]

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, "A"]

deck = []

player_allowance = 30
joey_allowance = 30
karen_allowance = 30

player_hand = []
joey_hand = []
karen_hand = []


def initial_Round(user):
    player_allowance -= small_blind
    joey_allowance -= big_blind
    print(user + " posts the small blind.  Joey posts the big blind.  Karen deals two face-down cards each to Joey and " + user + ".")
    first_draw_joey = random.choice(deck)
    joey_hand.append(first_draw_joey)
    deck.remove(first_draw_joey)
    first_draw_player = random.choice(deck)
    player_hand.append(first_draw_player)
    deck.remove(first_draw_player)


def form_Deck():  ## assembles deck of 52 from list of suits and numbers above
    for i in suits:
        for j in numbers:
            deck.append([i, j])


def main():
    form_Deck()
    print("Welcome to Texas Hold'em.  What is your name?")
    name = input()
    print("To start, post the small blind (1 dollar).  You have 30 dollars.")
    initial_Round(name)

main()
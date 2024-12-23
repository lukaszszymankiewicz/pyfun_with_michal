import random

colors = ["♦", "♣", "♠︎", "♥"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
actions = ["hit", "stand"]

# TODO: move it
class ClassCard:

    value = None
    color = None
    point = 0

    def __init__(self, value_to_set: int, color_to_set: str):

        if value_to_set not in values:
            raise ValueError()
        self.value = value_to_set

        if color_to_set not in colors:
            raise ValueError()
        self.color = color_to_set

        if value_to_set == "A":
            self.point = 11
        elif value_to_set == "K":
            self.point = 4
        elif value_to_set == "Q":
            self.point = 3
        elif value_to_set == "J":
            self.point = 2
        else:
            self.point = value_to_set

    def __repr__(self):
        return f"{str(self.value)}{self.color}"

# TODO: move it
class Hand:
    def __init__(self):
        self.cards = list()

    def count_points(self):
        result = 0
        aces = 0

        # easy
        for c in self.cards:
            # '+=' is sum to the previous value
            result += c.point

            if c.value == "A":
                aces += 1

        # TODO: tip: maybe use 'range' somehow?
        for n in range(aces):
            # cos tu trzeba dopisac, tylko co?


        # hard
        if result > 21:
            result -= 10

        return result

    def append(self, card):
        self.cards.append(card)

# TODO: move it
class ClassDeck:
    def __init__(
        self,
        deck_count: int,
        croupiers_cards: int,
        player_cards: int
    ):

        if actions == "hit":
            self.newcard = 1
        if actions == "stand":
            self.newcard = 0

        if (
            deck_count < 1 or deck_count > 52
        ):  # Prawdopodobnie wystarczy ze nie moze byc mniejsze od 1
            raise ValueError
        self.deck = 52 - croupiers_cards - player_cards

        if croupiers_cards < 2:
            raise ValueError
        self.croupiers = 2 + self.newcard

        if player_cards < 2:
            raise ValueError
        self.player = 2 + self.newcard

# TODO: move it (but where?)
deck = []

for color in colors:
    for value in values:
        deck.append(ClassCard(value, color))

# tasowanie
random.shuffle(deck)

player_hand = Hand()
croupier_hand = Hand()

# TODO: move it (but where?)
# My propsition so we don't have to make x times pop with each card:
for _ in range(2):
    random_card = deck.pop()  # Losowanie karty z talii
    player_hand.cards.append(random_card)  # Dodanie karty do ręki gracza

for _ in range(2):
    random_card = deck.pop()
    croupier_hand.cards.append(random_card)

# Remember end and test yourself - ML

print("croupier: ", end="")
print(f"POINTS: {croupier_hand.count_points()}")
for card in croupier_hand.cards:
    print(card, end=" ")

print("\nplayer: ", end="")
print(f"POINTS: {player_hand.count_points()}")
for card in player_hand.cards:
    print(card, end=" ")


# this is the croupies logic
# point < 17 -> Hit
# points >=17 -> Pass

# madry komentarz tutaj
if croupier_hand.count_points() < 17:
    card_hit = deck.pop()
    croupier_hand.cards.append(card_hit)

# win or lose
if player_hand.count_points() > 21:
    print('player busted, you lose')

elif croupier_hand.count_points() > 21:
    print('croupier busted, you win')

# TODO:
# check if both players passed
# when game should be continued?

player_input = input("\nP[ass] or H[it]?")

if player_input != ("H[it]?"):
    player_input == ("\nP[ass]")


    print(player_input)


# comments are for humans **NOT** computers
while True:
    pass
    # ONLY AT THE BEGINNING:
    # give 2 cards

    # MAIN LOOP:
    # print
    # input (Hit or Stand)
    # croupier
    # win or lose (break loop if lose)


"""
RESOURCES:
a) https://stackoverflow.com/questions/14017341/how-to-calculate-the-score-for-blackjack-game-where-am-i-going-wrong
b) https://stackoverflow.com/questions/2402483/calculating-hand-values-in-blackjack
"""

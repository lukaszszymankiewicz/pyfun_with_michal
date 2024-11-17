import random


colors = ["pik", "trefl", "kier", "karo"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jopek", "krolowa", "krol", "as"]
actions = ['hit', 'stand']

"""IRRELAVANT"""
# deck = [str(color) + "_" + value for color in colors for value in values]
# print(deck)

# deck[0]

# how to check the value of the card
card = "pik_jopek"
value = card.split("_")[1]
type = card.split("_")[0]

#Action which player and croupiers can take



"""CLASS IMPLEMENTATION"""


class ClassCard:
    def __init__(self, value_to_set: int, color_to_set: str):

        if value_to_set not in values:
            raise ValueError()
        self.value = value_to_set

        if color_to_set not in colors:
            raise ValueError()
        self.color = color_to_set

        if value_to_set == "as":
            """
            TODO (ASSIGNEMENT 1):
                - how to properly set points to ace card? It can be 1 or 11
                  depending on the overall hand point. ML: Player input
                - maybe it is bad place for storing point? ML: I would create new class for storing points
                - think: sum of points is a characteristic of a single card or full hand?
            """
            self.point = 1
        elif value_to_set == "krol":
            self.point = 4
        elif value_to_set == "krolowa":
            self.point = 3
        elif value_to_set == "jopek":
            self.point = 2
        else:
            self.point = value_to_set

    def __repr__(self):

        return f"ClassCard(value_to_set='{self.value}', color_to_set='{self.color}, point_to_set='{self.point})"

classCard = ClassCard
print(repr(classCard))


# Inicjalizacja obiektu

# card_pik_2 = ClassCard(2, "pik")
# print(card_pik_2.value)
# print(card_pik_2.color)

"""TODO (ASSIGNEMENT 3):
    - we need **something** to keep track of the:
        - deck
        - croupiers cards
        - player/s cards
    - think if there is a suitable way to handle all this cases in reusable and
      readable way
    - hint: maybe some **class** will have use here? After all, each of the
      case is just a collection of cards.
"""

class Hand:
    def __init__(self):
        self.cards = list()

    def count_points(self):
        pass

    def append(self, card):
        # TODO: is it right? Chyba nie bo nie mamy rozkminonego card? Jest wyżej zmienna ale nie mamy żadnego systemu który łaczy elementy z listy i określa co mamy w zmiennej card
        self.cards.append(card)


# 1) add cards to player
# 2) what we can do with the cards?
# 3) player input
# 4) show cards


# to na razie zostawiamy jak jest
class ClassDeck:
    def __init__(self, deck_count: int, croupiers_cards: int, player_cards: int):

        if actions == 'hit':
            self.newcard = 1
        if actions == 'stand':
            self.newcard = 0

        if deck_count < 1 or deck_count > 52:  # Prawdopodobnie wystarczy ze nie moze byc mniejsze od 1
            raise ValueError
        self.deck = 52 - croupiers_cards - player_cards

        if croupiers_cards < 2:
            raise ValueError
        self.croupiers = 2 + self.newcard

        if player_cards < 2:
            raise ValueError
        self.player = 2 + self.newcard



deck = []

for color in colors:
    for value in values:
        deck.append(ClassCard(value, color))

# tasowanie
random.shuffle(deck)

losowa_karta = deck[0]
losowa_karta = deck[-1]

# pop -> deck[-1] + usuwa element + zwraca go


# TODO: find-and-replace in PyCharm
player_hand = Hand()
croupier_hand = Hand()

#CTRL F CTRL R z shiftem dla all ale wbudowane w pycharm i wystarczy kliknac
#ciekawostka regex:
# For more advanced searches, you can utilize regular expressions (regex):
#
#     Enable regex by clicking the corresponding checkbox in the search dialog.
#     Regular expressions allow you to search for patterns rather than fixed strings. For example, searching for \b[A-Z]+\b will find all uppercase words.

testdupa = 'sraka_okrutna_gownem'
# Done

# logic of adding a card
# TODO: why this does not work as intended?
random_card = deck.pop()
player_hand.cards.append(random_card)
player_hand.cards.append(random_card)
print(player_hand)

random_card = deck.pop()
croupier_hand.cards.append(random_card)
croupier_hand.cards.append(random_card)
print(croupier_hand)

# My propsition so we don't have to make x times pop with each card:
for _ in range(2):
    random_card = deck.pop()  # Losowanie karty z talii
    player_hand.cards.append(random_card)  # Dodanie karty do ręki gracza

print(player_hand)

for _ in range(2):
    random_card = deck.pop()
    croupier_hand.cards.append(random_card)

print(croupier_hand)
# If I'm not as stupid as I look, we should be able to extend this loop in the future to initialize card drawing depending on the player's actions.
# Additionally, this allows for changing values and using this code  in other games where we need to draw more cards


# GAME STARTS!
# GRAPHICS!

# deck -> player_hand

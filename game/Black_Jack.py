import random


colors = ["pik", "trefl", "kier", "karo"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jopek", "krolowa", "krol", "as"]

"""IRRELAVANT"""
# deck = [str(color) + "_" + value for color in colors for value in values]
# print(deck)

# deck[0]

# how to check the value of the card
card = "pik_jopek"
value = card.split("_")[1]
type = card.split("_")[0]

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
                  depending on the overall hand point.
                - maybe it is bad place for storing point?
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
        """
        TODO (ASSIGNEMENT 2):
            - check what `__repr__` method does
            - write proper function here to make readability better
        """
        return None


# Inicjalizacja obiektu

# card_pik_2 = ClassCard(2, "pik")
# print(card_pik_2.value)
# print(card_pik_2.color)

# Tworzy talie

deck = []

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

for color in colors:
    for value in values:
        deck.append(ClassCard(value, color))

print(deck)

# tasowanie
random.shuffle(deck)

print(deck)

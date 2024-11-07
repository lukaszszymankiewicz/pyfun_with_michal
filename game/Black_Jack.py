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
    def __init__(self, value_to_set: int, color_to_set:str):

        if value_to_set not in values:
            raise ValueError()
        self.value = value_to_set

        if color_to_set not in colors:
            raise ValueError()
        self.color = color_to_set


        if value_to_set == "as":
            self.point = 1  # TODO: or 11
        elif value_to_set == "krol":
            self.point = 4
        elif value_to_set == "krolowa":
            self.point = 3
        elif value_to_set == "jopek":
            self.point = 2
        else:
            self.point = value_to_set

    # APPOINTMENT 2 (TODO)
    def __repr__(self):
        return None  # what is done here?


#Inicjalizacja obiektu

# card_pik_2 = ClassCard(2, "pik")
# print(card_pik_2.value)
# print(card_pik_2.color)

#Tworzy talie

deck = []

for color in colors:
    for value in values:
        deck.append(ClassCard(value, color))

print(deck)

# tasowanie
random.shuffle(deck)

print(deck)
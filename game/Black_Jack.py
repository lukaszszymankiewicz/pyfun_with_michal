import random

colors = ["♦", "♣", "♠︎", "♥"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
actions = ['hit', 'stand']


class ClassCard:
    def __init__(self, value_to_set: int, color_to_set: str):

        if value_to_set not in values:
            raise ValueError()
        self.value = value_to_set

        if color_to_set not in colors:
            raise ValueError()
        self.color = color_to_set

        if value_to_set == "A":
            self.point = 1
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


class Hand:
    def __init__(self):
        self.cards = list()

    def count_points(self):
        pass

    def append(self, card):
        # TODO: is it right? Chyba nie bo nie mamy rozkminonego card? Jest wyżej zmienna ale nie mamy żadnego systemu który łaczy elementy z listy i określa co mamy w zmiennej card
        self.cards.append(card)


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

player_hand = Hand()
croupier_hand = Hand()

# My propsition so we don't have to make x times pop with each card:
for _ in range(2):
    random_card = deck.pop()  # Losowanie karty z talii
    player_hand.cards.append(random_card)  # Dodanie karty do ręki gracza


for _ in range(2):
    random_card = deck.pop()
    croupier_hand.cards.append(random_card)

# If I'm not as stupid as I look, we should be able to extend this loop in the future to initialize card drawing depending on the player's actions.
# Additionally, this allows for changing values and using this code  in other games where we need to draw more cards

# GAME STARTS!
# GRAPHICS!

# a) what to draw:
# players hand + points
# croupiers hand + points
# print(player_hand)
# print(croupier_hand)

#  Remember end and test yourself - ML

print('croupier: ', end="")
for card in croupier_hand.cards:
    print(card, end=" ")

print('\nplayer: ', end="")
for card in player_hand.cards:
    print(card, end=" ")

# TODO: print points:
# 0) ALGORITHM!
# a) where points should be calculated?
# b) what about aces?
# c) where to print it?



# 1) add cards to player
# 2) what we can do with the cards?
# 3) player input
# 4) show cards

# deck -> player_hand

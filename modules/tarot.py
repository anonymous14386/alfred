import logging
import random


CARD_SUIT = [
    "Ace of",
    "Two of",
    "Three of",
    "Four of",
    "Five of",
    "Six of",
    "Seven of",
    "Eight of",
    "Nine of",
    "Ten of",
    "Page of",
    "Knight of",
    "Queen of",
    "King of",
]

CARD_SPECIAL = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strenght",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World",
]


def pickTarotCards(amount: int):

    for index in range(amount):
        suit = random.randint(1, 5)
        if suit != 1:
            card = random.randint(1, 14)
            pre = CARD_SUIT[card]
        else:
            card = random.randint(1, 21)
            name = CARD_SPECIAL[card]

        if suit == 2:
            suit = "swords"
        elif suit == 3:
            suit = "cups"
        elif suit == 4:
            suit = "coins"
        elif suit == 5:
            suit = "wands"
        else:
            suit = "other"

        pos = random.randint(1, 2)
        if pos == 1:
            position = "regular"
        else:
            position = "reversed"

        print("Suit: ", suit, " Card: ", card, " Position: ", position)

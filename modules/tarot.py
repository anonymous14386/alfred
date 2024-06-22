import logging
import random
import json

from discord import Embed
from pathlib import Path


def pickTarotCards(amount: int) -> [Embed]:
    """
    Picks one through n tarot cards and generates a discord embed for them
    TODO: refactor this code so that it can be used by both disccord and the xmpp bot
    """
    cardJson = Path("data/cards.json")
    if not cardJson.exists():
        logging.error("Failed to open cards.json!!!")

    imagesJson = Path("data/images.json")
    if not imagesJson.exists():
        logging.error("Failed to open images.json!!!")

    with open(cardJson) as f:
        cardData = json.load(f)

    with open(imagesJson) as f:
        imageData = json.load(f)

    cardArray = []

    for i in range(amount):
        num = random.randint(0, 77)
        card = cardData[str(num)]
        pos = random.randint(0, 1)
        cardParts = card.split("|")
        name = cardParts[1]
        poseDescs = cardParts[2].split(";")

        if pos == 0:
            description = poseDescs[0]
            fileName = cardParts[0] + ".jpg"
        else:
            description = poseDescs[1]
            name = name + " Reversed"
            fileName = cardParts[0] + "r.jpg"

        logging.debug("Title: " + name)
        logging.debug("Desc: " + description)
        logging.debug("File: " + fileName)

        image = imageData[str(num)]

        cardEmbed = Embed(title=name, description=description, colour=0xC000FF)
        cardEmbed.set_image(url=image)

        cardArray.append(cardEmbed)

    return cardArray

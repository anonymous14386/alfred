import logging
import random

from PIL import Image
import numpy as np

import data.db

COLORS_FOR_POKE_TYPES = {
    "Grass": 0x007400,
    "Poison": 0xC000FF,
    "Fire": 0xFF0000,
    "Flying": 0x73A7D6,
    "Water": 0x0071D8,
    "Bug": 0x579857,
    "Normal": 0x767676,
    "Electric": 0xFFFF00,
    "Ground": 0x675418,
    "Fairy": 0xFFC0CB,
    "Fighting": 0x983838,
    "Psychic": 0xFF3A9C,
    "Rock": 0xA17950,
    "Steel": 0xCCCCCC,
    "Ice": 0x00FFFF,
    "Ghost": 0x3D47C6,
    "Dragon": 0x8087E1,
    "Dark": 0x3E1F00,
}

IMAGE_API_URL = "https://www.serebii.net/pokemon/art"


def getAverageColor(imagePath: str) -> int:
    image = Image.Open(imagePath)
    imageArray = np.array(image)
    averageCol = np.mean(imageArray, axis=(0, 1)).astype(int)

    return averageCol


def getEmbedColor(pokemonType: str) -> int:
    """
    Get the embed color for the specified pokemon type
    """
    # FIXME: download the image and then
    # calculate the averate color automatically instead of looking it up in the dict
    return COLORS_FOR_POKE_TYPES[pokemonType]


def getImageUrl(numberData: str) -> str:
    """
    Returns the url for the image of a pokemon specified
    by the number data
    """
    return "%(url)s/%(imgNum)s.png" % {"url": IMAGE_API_URL, "imgNum": numberData}


def loadData(dataFolder: str) -> bool:
    """
    Load all the text files
    """
    pokeLowerListFile = open("%s/nameLower.txt" % dataFolder, "r")
    pokeLowerList = pokeLowerListFile.read().split(",")


def getRandomPokemon() -> (str, int):
    """
    Get a random pokemon from the pokedex
    """
    logging.debug("Getting random pokemon")

    randNum = random.randint(1, 1023)
    pokeNumberData = str(randNum).zfill(3)
    query = int(pokeNumberData) - 1

    imgUrl = getImageUrl(pokeNumberData)
    embedColor = getEmbedColor("Grass")

    logging.debug("imgurl %s and embed color %x" % imgUrl, embedColor)

    return (imgUrl, embedColor)

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


def getEmbedColor(pokemonType: str) -> int:
    """
    Get the embed color for the specified pokemon type
    """
    return COLORS_FOR_POKE_TYPES[pokemonType]


def getImageUrl(numberData: str) -> str:
    """
    Returns the url for the image of a pokemon specified
    by the number data
    """
    return "%(url)s/%(imgNum)s.png" % IMAGE_API_URL, numberData

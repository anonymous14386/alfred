import discord
import logging
import random
import json

from discord.ext import commands

import modules.pokemon as pk
import modules.tarot as tr

CHANNEL_ID = "test"


@commands.command()
async def info(ctx):
    help = discord.Embed(title="Help:")

    help.add_field(
        name="Command prefix: ~",
        value="Please put this before the request",
        inline=False,
    )

    help.add_field(
        name="Pokedex commands:",
        value="poke rand: Returns a random pokemon\npoke (num or name): Returns a specific pokemon",
        inline=False,
    )

    help.add_field(
        name="Tarot commands:",
        value="tarot(x): Returns x amount of Tarot cards",
        inline=False,
    )

    await ctx.send(embed=help)


@commands.command()
async def poke(ctx, arg):

    pokeLowerList = open("data/nameLower.txt", "r")
    pokeLowerListDatat = pokeLowerList.read()
    pokeLowerListData = pokeLowerListDatat.split(",")

    pokeList = open("data/name.txt", "r")
    pokeListDatat = pokeList.read()
    pokeListData = pokeListDatat.split(",")

    pokeTypeList = open("data/type.txt", "r")
    pokeTypeDatat = pokeTypeList.read()
    pokeTypeData = pokeTypeDatat.split(",")

    uInput = arg

    if uInput.isnumeric():
        pokeNumberData = str(uInput).zfill(3)

        query = int(pokeNumberData) - 1

        pokeTypeSplit = pokeTypeData[query].split(" | ")
        firstType = pokeTypeSplit[0].split()

        typeColor = pk.getEmbedColor(firstType)
        image = pk.getImageUrl(pokeNumberData)
        embed = discord.Embed(colour=typeColor)
        embed.add_field(
            name=pokeListData[query],
            value="Type: " + pokeTypeData[query] + "\nNumber: " + pokeNumberData,
        )

        # debug
        logging.debug(query)
        logging.debug("Name: " + pokeListData[query])
        logging.debug("Number: " + pokeNumberData)
        logging.debug("Type: " + pokeTypeData[query])
        logging.debug("You entered: " + pokeNumberData + " and it was numeric")
        # /debug

    elif uInput.lower() == "rand":

        randNum = random.randint(1, 1025)

        pokeNumberData = str(randNum).zfill(3)

        query = int(pokeNumberData) - 1

        # embed color by type

        pokeTypeSplit = pokeTypeData[query].split(" | ")
        firstType = pokeTypeSplit[0].strip()

        typeColor = pk.getEmbedColor(firstType)
        image = pk.getImageUrl(pokeNumberData)

        embed = discord.Embed(colour=typeColor)
        embed.add_field(
            name=pokeListData[query],
            value="Type: " + pokeTypeData[query] + "\nNumber: " + pokeNumberData,
        )

        # debug
        logging.debug(query)
        logging.debug("Name: " + pokeListData[query])
        logging.debug("Number: " + pokeNumberData)
        logging.debug("Type: " + pokeTypeData[query])
        logging.debug("You entered: " + pokeNumberData + " and it was numeric")
        # /debug

    else:
        inLower = uInput.lower()
        pokeNum = pokeLowerListData.index(inLower) + 1
        pokeNumberData = str(pokeNum).zfill(3)

        query = int(pokeNumberData) - 1

        # embed color by type

        pokeTypeSplit = pokeTypeData[query].split(" | ")
        firstType = pokeTypeSplit[0].strip()

        typeColor = pk.getEmbedColor(firstType)
        image = pk.getImageUrl(pokeNumberData)

        embed = discord.Embed(colour=typeColor)
        embed.add_field(
            name=pokeListData[query],
            value="Type: " + pokeTypeData[query] + "\nNumber: " + pokeNumberData,
        )

        # debug
        logging.debug("Number: " + str(pokeNum))
        logging.debug("Name: " + pokeListData[pokeNum - 1])
        logging.debug("Type: " + pokeTypeData[pokeNum - 1])
        # /debug

    embed.set_image(url=image)
    await ctx.send(embed=embed)


@commands.command()
async def tarot(ctx, amount: int):
    for card in tr.pickTarotCards(amount):
        await ctx.send(embed=card)


class AlfredBotDiscord(discord.ext.commands.Bot):

    def setup(self):
        self.remove_command("help")
        self.add_command(info)
        self.add_command(poke)
        self.add_command(tarot)

    async def on_ready(self):
        logging.info("Alfred online on discord!")
        channel = self.get_channel(CHANNEL_ID)

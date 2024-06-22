# Setup stuff
import asyncio
import json
import discord
from discord.ext import commands
import random
from urllib.request import urlopen

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Pull from config
with open("config.json") as f:
    data = json.load(f)

# Pull from cards.json
with open("data/cards.json") as f:
    cardData = json.load(f)

# Pull image links
with open("data/images.json") as f:
    imageData = json.load(f)


BOT_TOKEN = data["bot-token"]
CHANNEL_ID = data["channel-id"]
PREFIX = data["command-prefix"]

# Who knows why the fuck this is necessary
bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Alfred online")
    channel = bot.get_channel(CHANNEL_ID)


@bot.command()
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


@bot.command()
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
        firstType = pokeTypeSplit[0]

        if firstType.strip() == "Grass":
            typeColor = 0x007400

        elif firstType.strip() == "Poison":
            typeColor = 0xC000FF

        elif firstType.strip() == "Fire":
            typeColor = 0xFF0000

        elif firstType.strip() == "Flying":
            typeColor = 0x73A7D6

        elif firstType.strip() == "Water":
            typeColor = 0x0071D8

        elif firstType.strip() == "Bug":
            typeColor = 0x579857

        elif firstType.strip() == "Normal":
            typeColor = 0x767676

        elif firstType.strip() == "Electric":
            typeColor = 0xFFFF00

        elif firstType.strip() == "Ground":
            typeColor = 0x675418

        elif firstType.strip() == "Fairy":
            typeColor = 0xFFC0CB

        elif firstType.strip() == "Fighting":
            typeColor = 0x983838

        elif firstType.strip() == "Psychic":
            typeColor = 0xFF3A9C

        elif firstType.strip() == "Rock":
            typeColor = 0xA17950

        elif firstType.strip() == "Steel":
            typeColor = 0xCCCCCC

        elif firstType.strip() == "Ice":
            typeColor = 0x00FFFF

        elif firstType.strip() == "Ghost":
            typeColor = 0x3D47C6

        elif firstType.strip() == "Dragon":
            typeColor = 0x8087E1

        elif firstType.strip() == "Dark":
            typeColor = 0x3E1F00

        image = "https://www.serebii.net/pokemon/art/" + pokeNumberData + ".png"
        embed = discord.Embed(colour=typeColor)
        embed.add_field(
            name=pokeListData[query],
            value="Type: " + pokeTypeData[query] + "\nNumber: " + pokeNumberData,
        )

        # debug
        print(query)
        print("Name: " + pokeListData[query])
        print("Number: " + pokeNumberData)
        print("Type: " + pokeTypeData[query])
        print("You entered: " + pokeNumberData + " and it was numeric")
    # /debug

    elif uInput.lower() == "rand":

        randNum = random.randint(1, 1025)

        pokeNumberData = str(randNum).zfill(3)

        query = int(pokeNumberData) - 1

        # embed color by type

        pokeTypeSplit = pokeTypeData[query].split(" | ")
        firstType = pokeTypeSplit[0]

        if firstType.strip() == "Grass":
            typeColor = 0x007400

        elif firstType.strip() == "Poison":
            typeColor = 0xC000FF

        elif firstType.strip() == "Fire":
            typeColor = 0xFF0000

        elif firstType.strip() == "Flying":
            typeColor = 0x73A7D6

        elif firstType.strip() == "Water":
            typeColor = 0x0071D8

        elif firstType.strip() == "Bug":
            typeColor = 0x579857

        elif firstType.strip() == "Normal":
            typeColor = 0x767676

        elif firstType.strip() == "Electric":
            typeColor = 0xFFFF00

        elif firstType.strip() == "Ground":
            typeColor = 0x675418

        elif firstType.strip() == "Fairy":
            typeColor = 0xFFC0CB

        elif firstType.strip() == "Fighting":
            typeColor = 0x983838

        elif firstType.strip() == "Psychic":
            typeColor = 0xFF3A9C

        elif firstType.strip() == "Rock":
            typeColor = 0xA17950

        elif firstType.strip() == "Steel":
            typeColor = 0xCCCCCC

        elif firstType.strip() == "Ice":
            typeColor = 0x00FFFF

        elif firstType.strip() == "Ghost":
            typeColor = 0x3D47C6

        elif firstType.strip() == "Dragon":
            typeColor = 0x8087E1

        elif firstType.strip() == "Dark":
            typeColor = 0x3E1F00

        image = "https://www.serebii.net/pokemon/art/" + pokeNumberData + ".png"
        embed = discord.Embed(colour=typeColor)
        embed.add_field(
            name=pokeListData[query],
            value="Type: " + pokeTypeData[query] + "\nNumber: " + pokeNumberData,
        )

        # debug
        print(query)
        print("Name: " + pokeListData[query])
        print("Number: " + pokeNumberData)
        print("Type: " + pokeTypeData[query])
        print("You entered: " + pokeNumberData + " and it was numeric")
    # /debug

    else:
        inLower = uInput.lower()
        pokeNum = pokeLowerListData.index(inLower) + 1
        pokeNumberData = str(pokeNum).zfill(3)

        query = int(pokeNumberData) - 1

        # embed color by type

        pokeTypeSplit = pokeTypeData[query].split(" | ")
        firstType = pokeTypeSplit[0]

        if firstType.strip() == "Grass":
            typeColor = 0x007400

        elif firstType.strip() == "Poison":
            typeColor = 0xC000FF

        elif firstType.strip() == "Fire":
            typeColor = 0xFF0000

        elif firstType.strip() == "Flying":
            typeColor = 0x73A7D6

        elif firstType.strip() == "Water":
            typeColor = 0x0071D8

        elif firstType.strip() == "Bug":
            typeColor = 0x579857

        elif firstType.strip() == "Normal":
            typeColor = 0x767676

        elif firstType.strip() == "Electric":
            typeColor = 0xFFFF00

        elif firstType.strip() == "Ground":
            typeColor = 0x675418

        elif firstType.strip() == "Fairy":
            typeColor = 0xFFC0CB

        elif firstType.strip() == "Fighting":
            typeColor = 0x983838

        elif firstType.strip() == "Psychic":
            typeColor = 0xFF3A9C

        elif firstType.strip() == "Rock":
            typeColor = 0xA17950

        elif firstType.strip() == "Steel":
            typeColor = 0xCCCCCC

        elif firstType.strip() == "Ice":
            typeColor = 0x00FFFF

        elif firstType.strip() == "Ghost":
            typeColor = 0x3D47C6

        elif firstType.strip() == "Dragon":
            typeColor = 0x8087E1

        elif firstType.strip() == "Dark":
            typeColor = 0x3E1F00

        image = "https://www.serebii.net/pokemon/art/" + str(pokeNumberData) + ".png"
        embed = discord.Embed(colour=typeColor)
        embed.add_field(
            name=pokeListData[query],
            value="Type: " + pokeTypeData[query] + "\nNumber: " + pokeNumberData,
        )

        # debug
        print("Number: " + str(pokeNum))
        print("Name: " + pokeListData[pokeNum - 1])
        print("Type: " + pokeTypeData[pokeNum - 1])
    # /debug

    embed.set_image(url=image)
    await ctx.send(embed=embed)


@bot.command()
async def T(ctx, amount: int):

    for i in range(amount):

        # 0-77
        num = random.randint(0, 77)

        card = cardData[str(num)]

        pos = random.randint(0, 1)
        # print ()
        # print (pos)
        # print(num)
        # print(card)
        cardParts = card.split("|")

        # print("File: " + fileName)

        name = cardParts[1]
        # print("Name:" + name)

        poseDescs = cardParts[2].split(";")

        if pos == 0:
            description = poseDescs[0]
            fileName = cardParts[0] + ".jpg"
        else:
            description = poseDescs[1]
            name = name + " Reversed"
            fileName = cardParts[0] + "r.jpg"

        print("Title: " + name)
        print("Desc: " + description)
        print("File: " + fileName)

        image = imageData[str(num)]

        cardEmbed = discord.Embed(title=name, description=description, colour=0xC000FF)

        cardEmbed.set_image(url=image)

        await ctx.send(embed=cardEmbed)

        # out = discord.Embed(title=cardName, description=position + cardDesc ,colour=0xC000FF)
        # await ctx.send( embed=out)

        # out = discord.Embed(title=cardName, description=position + cardDesc ,colour=0xC000FF)
        # await ctx.send( embed=out)


bot.run(BOT_TOKEN)

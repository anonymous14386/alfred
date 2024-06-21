import discord
import logging


class AlfredBotDiscord(discord.Bot):
    async def on_ready():
        logging.info("Alfred online on discord!")
        channel = bot.get_channel(CHANNEL_ID)

    @command()
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

    @command()
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

            typeColor = pk.getEmbedColor(firstType.strip())
            image = pk.getImageUrl(pokeNumberData)
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

            typeColor = pk.getEmbedColor(firstType.strip())
            image = pk.getImageUrl(pokeNumberData)
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

            typeColor = pk.getEmbedColor(firstType.strip())
            image = pk.getImageUrl(pokeNumberData)
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

    @command()
    async def tarot(ctx, amount: int):

        tarot = open("data/tarotDesc.txt", "r")
        tarotDB = tarot.read()

        for i in range(amount):
            name = "Tarot card name here"
            description = "Description"
            # 156 cards
            suit = random.randint(1, 5)
            if suit != 1:
                card = random.randint(1, 14)
                if card == 1:
                    pre = "Ace of"
                elif card == 2:
                    pre = "Two of"
                elif card == 3:
                    pre = "Three of"
                elif card == 4:
                    pre = "Four of"
                elif card == 5:
                    pre = "Five of"
                elif card == 6:
                    pre = "Six of"
                elif card == 7:
                    pre = "Seven of"
                elif card == 8:
                    pre = "Eight of"
                elif card == 9:
                    pre = "Nine of"
                elif card == 10:
                    pre = "Ten of"
                elif card == 11:
                    pre = "Page of"
                elif card == 12:
                    pre = "Knight of"
                elif card == 13:
                    pre = "Queen of"
                elif card == 14:
                    pre = "King of"

            else:
                card = random.randint(1, 21)
                if card == 1:
                    name = "The Fool"
                elif card == 2:
                    name = "The Magician"
                elif card == 3:
                    name = "The High Priestess"
                elif card == 4:
                    name = "The Empress"
                elif card == 5:
                    name = "The Emperor"
                elif card == 6:
                    name = "The Hierophant"
                elif card == 7:
                    name = "The Lovers"
                elif card == 8:
                    name = "The Chariot"
                elif card == 9:
                    name = "Strength"
                elif card == 10:
                    name = "The Hermit"
                elif card == 11:
                    name = "Wheel of Fortune"
                elif card == 12:
                    name = "Justice"
                elif card == 13:
                    name = "The Hanged Man"
                elif card == 14:
                    name = "Death"
                elif card == 15:
                    name = "Temperance"
                elif card == 16:
                    name = "The Devil"
                elif card == 17:
                    name = "The Tower"
                elif card == 18:
                    name = "The Star"
                elif card == 19:
                    name = "The Moon"
                elif card == 20:
                    name = "The Sun"
                elif card == 21:
                    name = "Judgement"
                elif card == 22:
                    name = "The World"

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

            # 1-22 misc
            # 24-37 swords
            # 39-52 cups
            # 55-68 coins
            # 70-83 wands

# Setup stuff
import asyncio
import json
import discord
import slixmpp
import logging
import random

#testr= git

from discord.ext import commands
from urllib.request import urlopen
from argparse import ArgumentParser
from pathlib import Path
from getpass import getpass

import modules.pokemon as pk
import backends.xmpp as xmpp
import backends.discord as dc


if __name__ == "__main__":

    PREFIX = "~"

    parser = ArgumentParser(description="Test")
    parser.add_argument(
        "-x",
        "--xmpp",
        action="store_const",
        dest="usexmpp",
        const=True,
        default=False,
        help="Use xmpp instead of discord",
    )
    parser.add_argument(
        "-c",
        "--config",
        dest="configPath",
        default="config.json",
        help="Path to the config file",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_const",
        dest="interactive",
        const=True,
        default=False,
        help="Run in interactive mode. This will ask for a username and password",
    )

    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG, format="%(levelname)-8s %(message)s")
    logging.info("Starting alfred bot ...")
    logging.debug(args)

    if not args.interactive:
        # check if config file exists
        configfile = Path(args.configPath)
        logging.debug("Trying to load %s" % configfile)

        if not configfile.exists():
            logging.error("Failed to find config file")
            exit(1)

    # Pull from config
    with open(configfile) as f:
        data = json.load(f)

    if not args.usexmpp:
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True

        if args.interactive:
            BOT_TOKEN = getpass("bot-token (not shown): ")
            CHANNEL_ID = input("channel-id: ")
            PREFIX = input("command-prefix: ")
        else:
            BOT_TOKEN = data["bot-token"]
            CHANNEL_ID = data["channel-id"]
            PREFIX = data["command-prefix"]

        bot = dc.AlfredBotDiscord(command_prefix=PREFIX, intents=discord.Intents.all())
        # bot.remove_command("help")
        bot.setup()
        bot.run(BOT_TOKEN)

    else:
        logging.info("Running in xmpp mode!")

        with open(configfile) as f:
            data = json.load(f)

        # either let the user enter the details
        # or read them from the config file
        if args.interactive:
            logging.info("Running in interactive mode...")
            XMPP_SERVER = input("xmpp-server address: ")
            XMPP_USER = input("username: ")
            XMPP_PASS = getpass("Password: ")
        else:
            XMPP_SERVER = data["xmpp-server"]
            XMPP_USER = data["xmpp-username"]
            XMPP_PASS = data["xmpp-password"]

        jid = "%(name)s@%(server)s" % {"name": XMPP_USER, "server": XMPP_SERVER}
        logging.debug("Jid is %s" % jid)
        logging.debug("Password is %s" % XMPP_PASS)

        xmppBot = xmpp.AlfredBotXMPP(jid, XMPP_PASS)
        xmppBot.register_plugin("xep_0030")  # Service discovery
        xmppBot.register_plugin("xep_0004")  # Data Forms
        xmppBot.register_plugin("xep_0060")  # PubSub
        xmppBot.register_plugin("xep_0199")  # Ping

        # Connect to the xmpp server and run the bot
        xmppBot.connect()
        xmppBot.process()

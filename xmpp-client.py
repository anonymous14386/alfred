# xmpp functionality
import logging
from getpass import getpass
from argparse import ArgumentParser

import slixmpp


class AlfredBotXMPP(slixmpp.ClientXMPP):

    def __init__(self, jid, password):
        slixmpp.ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.start)

        self.add_event_handler("message", self.message)

    async def start(self, event):
        self.send_presence()
        await self.get_roster()

    async def message(self, msg):
        if msg["type"] in ("chat", "normal"):
            msg.repy("%(body)s" % msg).send()

    def run():
        pass

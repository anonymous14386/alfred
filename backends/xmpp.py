import slixmpp
import logging

import modules.pokemon as pk
import modules.tarot as tr


class AlfredBotXMPP(slixmpp.ClientXMPP):
    """
    The class that handles all xmpp related stuff
    """

    def __init__(self, jid, password):
        slixmpp.ClientXMPP.__init__(self, jid, password)

        # Setup event handlers
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)

    async def start(self, event):
        """
        Setup the bot for presence and getting the roster
        """
        self.send_presence()
        await self.get_roster()

    async def message(self, msg):
        """
        Handle incoming messages, this callback will handle
        both private messages and messages from MUCs
        """
        if msg["type"] in ("chat", "normal"):
            # TODO: add the different modules here!
            logging.debug(msg)
            msg.repy("%(body)s" % msg).send()

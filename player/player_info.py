from session_wrapper import SesstionWrapper
from player.events import Events
from player.planets import Planets
from player.planet.galaxy_explorer.galaxy_explorer import GalaxyExplorer
from player.messages.message_manager import MessageManager

class PlayerInfo():

    def __init__(self, comm, server_info):
        assert isinstance(comm, SesstionWrapper)
        self._comm = comm

        self._planets = Planets(comm)
        self._events = Events(comm)

        self._message_manager = MessageManager(comm)

    @property
    def events(self):
        self._events.update_events()
        return self._events

    @property
    def planets(self):
        return self._planets

    @property
    def message_manager(self):
        return self._message_manager
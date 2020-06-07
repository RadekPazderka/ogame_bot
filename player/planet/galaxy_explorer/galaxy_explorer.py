from player.planet.fleet.coord import Coord
from session_wrapper import SesstionWrapper
from player.ogame_client import OgameClient

class EnemyPlanetType():


    def __init__(self, type):
        self._type = type


class GalaxyExplorer(object):

    def __init__(self, comm: SesstionWrapper, planet_id):
        self._planet_id = planet_id
        self._comm = comm

    def galaxy_inactive_players(self, coord: Coord):
        inactive_players = OgameClient.get_galaxy(self._comm, self._planet_id, coord).getInactivePlanets()
        return inactive_players
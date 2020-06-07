from player.planet.galaxy_explorer.galaxy_explorer import GalaxyExplorer
from player.planet.fleet.coord import Location, Coord
from player.ogame_client import OgameClient

class GalaxyExplorerManager(object):
    def __init__(self, comm, planet_id, planet_location:Location):
        self._planet_id = planet_id
        self._planet_location = planet_location
        self._comm = comm
        self._galaxy_explorer = GalaxyExplorer(comm, planet_id)

    def explore_near_planet(self, radius):
        galaxy = self._planet_location.coord.galaxy
        system = self._planet_location.coord.system
        res = []
        for i in range(-radius, radius + 1):
            res += self._galaxy_explorer.galaxy_inactive_players(Coord(galaxy, system + i, 0))
        return res

    def get_galaxy_debris(self):
        return OgameClient.get_galaxy(self._comm, self._planet_id, self._planet_location.coord).get_expedition_debris()
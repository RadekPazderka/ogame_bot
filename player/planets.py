from player.planet.planet_info import PlanetInfo
from player.ogame_client import OgameClient

class Planets:

    def __init__(self, comm):
        planets_id = OgameClient.get_overview(comm).getPlanetsId()
        self._planets = [PlanetInfo(comm, planets_id) for planets_id in planets_id]

    def get_by_name(self, planet_name):
        return list(filter(lambda planet: planet.name == planet_name, self._planets))[0]

    def get_by_id(self, planet_id):
        return list(filter(lambda planet: planet.id == planet_id, self._planets))[0]

    def get_all(self):
        return self._planets


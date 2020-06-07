from bs4 import BeautifulSoup

from player.planet.fleet.coord import Location, Coord, DestinationType


class PlanetDetailPage():

    def __init__(self, content):
        el = BeautifulSoup(content, "lxml")
        self._head = el.find("head")

    def getPlanetName(self) -> str:
        return self._head.find("meta", attrs={"name": "ogame-planet-name"}).attrs["content"]

    def getLocation(self) -> Location:
        position = self._head.find("meta", attrs={"name": "ogame-planet-coordinates"}).attrs["content"].split(":")
        planet_type = self._head.find("meta", attrs={"name": "ogame-planet-type"}).attrs["content"]

        return Location(Coord(*position), DestinationType(planet_type))


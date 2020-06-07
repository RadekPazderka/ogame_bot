from bs4 import BeautifulSoup
from player.planet.fleet.coord import Coord, DestinationType, Location

class OverviewPage():

    def __init__(self, content):
        self._el = BeautifulSoup(content, "lxml")

    def getPlanetsId(self) -> map:
        planets = self._el.find_all("div", attrs={"class": "smallplanet"})

        return map(self._parse_planet_id, planets)

    def _parse_planet_id(self, planet):
        return int(planet.attrs["id"].replace("planet-", ""))

    def get_planet_name(self):
        head = self._el.find("head")
        return head.find("meta", attrs={"name": "ogame-planet-name"}).attrs["content"]


    def get_location(self):
        head = self._el.find("head")
        position = head.find("meta", attrs={"name": "ogame-planet-coordinates"}).attrs["content"].split(":")
        planet_type = head.find("meta", attrs={"name": "ogame-planet-type"}).attrs["content"]
        return Location(Coord(*position), DestinationType(planet_type))

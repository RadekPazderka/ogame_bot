import re
from player.planet.fleet.coord import Coord, DestinationType, Location

class HangarPage():

    def __init__(self, content):
        regex = "var upgradeEndpoint\s*=\s*\"(.*)\";"
        self._base_url = re.search(regex, content).group(1)

    def get_production_url(self, ship_id, amount):
        return self._base_url.replace("\\", "/").replace("TECHNOLOGY_ID", str(ship_id)).replace("AMOUNT", str(amount)).replace("//", "/")


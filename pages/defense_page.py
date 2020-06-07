import re
from player.planet.fleet.coord import Coord, DestinationType, Location

class DefensePage():
    #var upgradeEndpoint = "https:\/\/s146-cz.ogame.gameforge.com\/game\/index.php?page=ingame&component=defenses&modus=1&token=cc38cdcb9355d07a091d7f156d9a0d9d&type=TECHNOLOGY_ID&menge=AMOUNT";
    def __init__(self, content):
        regex = "var upgradeEndpoint\s*=\s*\"(.*)\";"
        self._base_url = re.search(regex, content).group(1)

    def get_production_url(self, defense_id, amount):
        return self._base_url.replace("\\", "/").replace("TECHNOLOGY_ID", str(defense_id)).replace("AMOUNT", str(amount)).replace("//", "/")


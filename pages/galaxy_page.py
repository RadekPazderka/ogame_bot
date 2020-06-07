from bs4 import BeautifulSoup
from player.planet.fleet.coord import Coord
import json
import re

class GalaxyPage():

    def __init__(self, content):
        json_data = json.loads(content)
        self._debug_content = json_data["galaxy"]
        self._parser = BeautifulSoup(json_data["galaxy"], "lxml")

    def getInactivePlanets(self):

        inactive_players = []
        galaxy_table = self._parser.find("table", attrs={"id": "galaxytable"})
        galaxy = int(galaxy_table.attrs["data-galaxy"])
        system = int(galaxy_table.attrs["data-system"])

        inactives = galaxy_table.find_all("tr", attrs={"class": "row inactive_filter"})
        for inactive in inactives:
            check_status = inactive.find("td", attrs={"class": ["playername", "inactive"]})
            if check_status is None:
                continue

            position = int(inactive.find("td", attrs={"class": "position"}).text)
            player_id = int(inactive.find("a", attrs={"class": "sendMail"}).attrs["data-playerid"])

            inactive_players.append({
                "coord": Coord(galaxy, system, position),
                "player_id": player_id
            })
        return inactive_players

    def get_expedition_debris(self):
        expedition_devris_element = self._parser.find("div", attrs={"class": "expeditionDebrisSlotBox"})
        if expedition_devris_element is None:
            return {"metal": 0, "crystal": 0, "explorers": 0}

        resources = expedition_devris_element.find_all("li", attrs={"class" :"debris-content"})
        explorers_element = expedition_devris_element.find("li", attrs={"class" :"debris-recyclers"})
        metal_string = resources[0].text
        crystal_string = resources[1].text
        explorer_needed_string = explorers_element.text

        metal = int(re.search("\w+:\s*([0-9\.]*)", metal_string).group(1).replace(".", ""))
        crystal = int(re.search("\w+:\s*([0-9\.]*)", crystal_string).group(1).replace(".", ""))
        exploreres = int(re.search(".*:\s*([0-9\.]*)", explorer_needed_string).group(1).replace(".", ""))

        return {"metal": metal, "crystal": crystal, "explorers": exploreres}
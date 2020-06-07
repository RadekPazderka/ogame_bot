from bs4 import BeautifulSoup
import re

from player.planet.fleet.coord import Location, Coord, DestinationTypeBuilder
from player.planet.fleet.fleet_army import FleetBuilder, FleetArmy
from player.planet.defense.defense_towers import DefenseTowersBuilder, DefenseArmy
from player.planet.resources.resources_status import ResourcesStatus


class SpyMessageDetailPage(object):
    def __init__(self, content):
        self._parser = BeautifulSoup(content, "lxml")


    def get_location(self):
        header = self._parser.find("div", attrs={"class": "detail_msg_head"})
        link = header.find("a", attrs={"class": "txt_link"})
        res = re.search(".*\[(\d+):(\d+):(\d+)\]", link.text)
        galaxy = res.group(1)
        system = res.group(2)
        position = res.group(3)

        return Location(Coord(galaxy, system, position),DestinationTypeBuilder.planet())


    def get_resources(self) -> ResourcesStatus:
        resources_ul = self._parser.find("ul", attrs={"data-type": "resources"})

        resources = resources_ul.find_all("span", attrs={"class": "res_value"})
        res = []
        for resource in resources:
            txt_resource = resource.text
            if txt_resource.find("M") != -1:
                txt_resource = txt_resource.replace("M", "").replace(",", ".")
                int_resource = int(float(txt_resource) * 1000*1000)
            else:
                int_resource = int(txt_resource.replace(".", ""))
            res.append(int_resource)
        metal, cry, deu, energy = res
        return ResourcesStatus(metal, cry, deu, energy)


    def get_fleet(self) -> FleetArmy:
        fleet_builder = FleetBuilder()
        fleet_ul = self._parser.find("ul", attrs={"data-type": "ships"})
        fleets = fleet_ul.find_all("li")

        for fleet in fleets:
            fleet_type = fleet.find("img", attrs={"class": re.compile("tech\d+")}).attrs["class"][0]
            fleet_id = int(fleet_type.replace("tech", ""))
            fleet_count = int((fleet.find("span", attrs={"class": "fright"}).text).replace(".", ""))
            fleet_builder.add_fleet_by_id(fleet_id, fleet_count)
        return fleet_builder.build()


    def get_defense(self) -> DefenseArmy:
        def_tower_builder = DefenseTowersBuilder()
        defense_ul = self._parser.find("ul", attrs={"data-type": "defense"})

        defense = defense_ul.find_all("li")
        for defense_tower in defense:
            defense_type = defense_tower.find("img", attrs={"class": re.compile("defense\d+")}).attrs["class"][0]
            defense_tower_id = int(defense_type.replace("defense", ""))
            defense_tower_count = int((defense_tower.find("span", attrs={"class": "fright"}).text).replace(".", ""))
            def_tower_builder.add_defense_by_id(defense_tower_id, defense_tower_count)
        return def_tower_builder.build()

    def get_buildings(self):
        return None #TODO

    def get_research(self):
        return None #TODO
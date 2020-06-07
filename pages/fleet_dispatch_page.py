import re
from player.planet.fleet.fleet_army import FleetArmy, FleetBuilder
from bs4 import BeautifulSoup

from player.planet.fleet.fleet_status import FleetStatus


class FleetDispatchPage():

    def __init__(self, content):
        self._content = content

    def _get_token(self):
        return re.search("var\s+fleetSendingToken\s*=\s*\"(.*)\"", self._content).group(1)  # TODO: check

    def _get_fleet_army(self) -> FleetArmy:
        fleet_builder = FleetBuilder()
        parsed = BeautifulSoup(self._content, "lxml")
        fleet_blogs = parsed.find_all("ul", attrs={"id": re.compile("(military|civil)")})
        for fleet_blog in fleet_blogs:
            fleets = fleet_blog.find_all("li", attrs={"class": "technology"})

            for fleet in fleets:
                count = fleet.find("span", attrs={"class": "amount"}).attrs["data-value"]
                fleet_id = int(fleet.attrs["data-technology"])
                fleet_builder.add_fleet_by_id(fleet_id, count)
        return fleet_builder.build()

    def get_fleet_status(self) -> FleetStatus:
        res_fleet = re.search("<span>\s*letek:\s*<\/span>\s*(\d+)\/(\d+)\s*<\/span>", self._content)
        res_expedition = re.search("<span>\s*expedice:\s*<\/span>\s*(\d+)\/(\d+)\s*<\/span>", self._content)

        fleet_used_slots =  int(res_fleet.group(1))
        fleet_max_slots = int(res_fleet.group(2))
        expeditions_used_slots = int(res_expedition.group(1))
        expedition_max_slots = int(res_expedition.group(2))

        return FleetStatus(fleet_army=self._get_fleet_army(), fleet_used_slots=fleet_used_slots, fleet_max_slots=fleet_max_slots,
                    expeditions_used_slots=expeditions_used_slots, expedition_max_slots=expedition_max_slots)

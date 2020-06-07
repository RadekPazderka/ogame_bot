from player.ogame_client import OgameClient

class BuildingsInfo(object):

    def __init__(self, comm, planet_id):
        self._comm = comm
        self._planet_id = planet_id

    def get_producers(self):
        supplies_page = OgameClient.get_supplies(self._comm, self._planet_id).get_producers_list()

        producers_list = ["metalMine", "crystalMine", "deuteriumSynthesizer",
                          "solarPlant", "fusionPlant", "metalStorage",
                          "crystalStorage", "deuteriumStorage"]

        return {producer_name: supplies_page.get_item(producer_name) for producer_name in producers_list}
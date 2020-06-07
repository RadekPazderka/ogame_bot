from player.planet.building.building_info import BuildingsInfo
from player.planet.building.building_strategy import SuppliesUpgradeStrategy, SuppliesStorageUpgradeStrategy

class BuildingManager(object):

    def __init__(self, comm, planet_id, planet_name:str):
        self._comm = comm
        self._planet_id = planet_id
        self._buildings = BuildingsInfo(comm, planet_id)

        self._planet_name = planet_name

    def build_buildings(self): #TODO reformat strategy...
        producers = self._buildings.get_producers()

        build_strategy = SuppliesUpgradeStrategy()
        selected_producer = build_strategy.select_upgrade(producers)
        if selected_producer is not None:
            print("[{} (planet)] Build: {}".format(self._planet_name, selected_producer["name"]))
            self._comm.get(selected_producer["upgrade_url"])

    def build_storages(self):
        producers = self._buildings.get_producers()

        build_strategy = SuppliesStorageUpgradeStrategy()
        selected_producer = build_strategy.select_upgrade(producers)
        if selected_producer is not None:
            print("[{} (planet)] Build: {}".format(self._planet_name, selected_producer["name"]))
            self._comm.get(selected_producer["upgrade_url"])
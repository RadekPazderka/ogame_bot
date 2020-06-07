from player.planet.facility.facility_info import FacilityInfo
from player.planet.facility.facility_strategy import FacilitiesUpgradeStrategy


class FacilityManager(object):

    def __init__(self, comm, planet_id, planet_name:str):
        self._comm = comm
        self._planet_id = planet_id
        self._facilities = FacilityInfo(comm, planet_id)
        self._planet_name = planet_name

    def build_facilities(self): #TODO reformat strategy...

        facilities = self._facilities.get_facilities()


        facility_strategy = FacilitiesUpgradeStrategy()
        selected_facility = facility_strategy.select_upgrade(facilities)
        if selected_facility is not None:
            print("[{} (planet)] Build facility: {}".format(self._planet_name, selected_facility["name"]))
            self._comm.get(selected_facility["upgrade_url"])

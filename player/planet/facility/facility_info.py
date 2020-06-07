from player.ogame_client import OgameClient

class FacilityInfo(object):

    def __init__(self, comm, planet_id):
        self._comm = comm
        self._planet_id = planet_id

    def get_facilities(self):
        facilities_page = OgameClient.get_facilities(self._comm, self._planet_id).get_producers_list()

        facilities_list = ["roboticsFactory", "shipyard", "researchLaboratory",
                          "allianceDepot", "missileSilo", "naniteFactory",
                          "terraformer", "repairDock"]

        return {facility_name: facilities_page.get_item(facility_name) for facility_name in facilities_list}
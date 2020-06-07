from player.ogame_client import OgameClient
from player.planet.fleet.fleet_army import FleetArmy
class HangarManager(object):

    def __init__(self, comm, planet_id, planet_name:str):
        self._comm = comm
        self._planet_id = planet_id
        self._planet_name = planet_name

    def make_fleet(self, fleet):
        assert isinstance(fleet, FleetArmy)

        fleet_to_build = fleet.get_data()

        for fl in fleet_to_build:
            hangar_page = OgameClient.get_hangar(self._comm, self._planet_id)
            url = hangar_page.get_production_url(fl[0], fl[1]) #TODO: refactor!
            self._comm.get(url)
            print("[{} (planet)] Hangar production: {}x {}".format(self._planet_name, fl[1], fl[2]))
        pass

        #hangar_page.get_production_url()




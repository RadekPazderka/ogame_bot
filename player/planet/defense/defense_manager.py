from player.ogame_client import OgameClient
from player.planet.defense.defense_towers import DefenseArmy

class DefenseManager(object):

    def __init__(self, comm, planet_id, planet_name:str):
        self._comm = comm
        self._planet_id = planet_id
        self._planet_name = planet_name

    def make_defense(self, defense):
        assert isinstance(defense, DefenseArmy)

        defense_to_build = defense.get_data()

        for fl in defense_to_build:
            defense_page = OgameClient.get_defense(self._comm, self._planet_id)
            url = defense_page.get_production_url(fl[0], fl[1]) #TODO: refactor!
            self._comm.get(url)
            print("[{} (planet)] Defense production: {}x {}".format(self._planet_name, fl[1], fl[2]))
        pass

        #hangar_page.get_production_url()

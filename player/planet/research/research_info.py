from player.ogame_client import OgameClient

class ResearchInfo(object):

    def __init__(self, comm, planet_id):
        self._comm = comm
        self._planet_id = planet_id

    def get_reseach(self):
        research_page = OgameClient.get_reseach(self._comm, self._planet_id).get_research_list()

        research_list = ['energyTechnology', 'laserTechnology', 'ionTechnology', 'hyperspaceTechnology',
                         'plasmaTechnology','combustionDriveTechnology', 'impulseDriveTechnology', 'hyperspaceDriveTechnology',
                         'espionageTechnology', 'computerTechnology', 'astrophysicsTechnology', 'researchNetworkTechnology',
                         'gravitonTechnology', 'weaponsTechnology', 'shieldingTechnology', 'armorTechnology']

        return {reseach_name: research_page.get_item(reseach_name) for reseach_name in research_list}
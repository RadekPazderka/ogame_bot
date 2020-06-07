from player.planet.research.research_info import ResearchInfo
from player.planet.research.research_strategy import ExamineResearchStrategy

class ResearchManager(object):

    def __init__(self, comm, planet_id, planet_name:str):
        self._comm = comm
        self._planet_id = planet_id
        self._researches = ResearchInfo(comm, planet_id)

        self._planet_name = planet_name

    def make_reseach(self): #TODO reformat strategy...
        producers = self._researches.get_reseach()

        research_strategy = ExamineResearchStrategy()
        selected_producer = research_strategy.select_upgrade(producers)
        if selected_producer is not None:
            print("[{} (planet)] - Reseach: {} has begun".format(self._planet_name, selected_producer["name"]))
            self._comm.get(selected_producer["upgrade_url"])


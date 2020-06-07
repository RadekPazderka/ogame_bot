from player.planet.fleet.coord import Location

class FarmPlanetInfo():
    def __init__(self, location:Location, metal, cry, deu,
                 fleet, defense,
                 metalMine, crystalMine, deuteriumSynthesizer,
                 metalStorage, crystalStorage, deuteriumStorage):
        self._location = location
        self._metal = metal
        self._cry = cry
        self._deu = deu
        self._fleet = fleet
        self._defense = defense
        self._metalMine = metalMine
        self._crystalMine = crystalMine
        self._deuteriumSynthesizer = deuteriumSynthesizer
        self._metalStorage = metalStorage
        self._crystalStorage = crystalStorage
        self._deuteriumStorage = deuteriumStorage

    def __str__(self):
        return "{}"
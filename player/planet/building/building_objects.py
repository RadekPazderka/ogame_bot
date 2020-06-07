class BuildingBase(object):
    NAME = ""
    ID = 0

    def __init__(self, level):
        self._level = level

    @property
    def level(self):
        return self._level


class MetalMine(BuildingBase):
    NAME = "metalMine"
    ID = 1

class CrystalMine(BuildingBase):
    NAME = "crystalMine"
    ID = 2

class DeuteriumSynthesizer(BuildingBase):
    NAME = "deuteriumSynthesizer"
    ID = 3

class SolarPlant(BuildingBase):
    NAME = "solarPlant"
    ID = 4

class FusionPlant(BuildingBase):
    NAME = "fusionPlant"
    ID = 12

class MetalStorage(BuildingBase):
    NAME = "metalStorage"
    ID = 22

class CrystalStorage(BuildingBase):
    NAME = "crystalStorage"
    ID = 23

class DeuteriumStorage(BuildingBase):
    NAME = "deuteriumStorage"
    ID = 24

class Buildings(object):
    def __init__(self, buildings: [BuildingBase]):
        self._buildings = buildings


class BuildingBuilder():
    MAPPING = {
        1 : MetalMine,
        2 : CrystalMine,
        3 : DeuteriumSynthesizer,
        4 : SolarPlant,
        12 : FusionPlant,
        22 : MetalStorage,
        23 : CrystalStorage,
        24 : DeuteriumStorage
    }

    def __init__(self):
        self._buildings = []

    def add_by_id(self, building_id, level):
        self._buildings.append(self.MAPPING[building_id](level))

    def with_metalMine(self, level):
        self._buildings.append(MetalMine(level))
        return self

    def with_crystalMine(self, level):
        self._buildings.append(CrystalMine(level))
        return self

    def with_deuteriumSynthesizer(self, level):
        self._buildings.append(DeuteriumSynthesizer(level))
        return self

    def with_solarPlant(self, level):
        self._buildings.append(SolarPlant(level))
        return self

    def with_fusionPlant(self, level):
        self._buildings.append(FusionPlant(level))
        return self

    def with_metalStorage(self, level):
        self._buildings.append(MetalStorage(level))
        return self

    def with_crystalStorage(self, level):
        self._buildings.append(CrystalStorage(level))
        return self

    def with_deuteriumStorage(self, level):
        self._buildings.append(DeuteriumStorage(level))
        return self

    def build(self) -> Buildings:
        return Buildings(self._buildings)




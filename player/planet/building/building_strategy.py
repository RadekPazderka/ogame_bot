from abc import ABC, abstractmethod

class SuppliesUpgradeBase(ABC):

    @abstractmethod
    def select_upgrade(self, producers):
        pass

class SuppliesUpgradeStrategy(SuppliesUpgradeBase):

    def __init__(self):
        pass

    producers_list = {
                "metalMine":            lambda x: x,
                "crystalMine":          lambda x: x,
                "deuteriumSynthesizer": lambda x: x,
                "solarPlant":           lambda x: x+5,
                "fusionPlant":          lambda x: x+200, #no need
                "metalStorage":         lambda x: x*3,
                "crystalStorage":       lambda x: (x+2)*3,
                "deuteriumStorage":     lambda x: (x+4)*3
                }

    buildings_max_level = {
        "metalMine": 100,
        "crystalMine": 100,
        "deuteriumSynthesizer": 100,
        "solarPlant": 30,
        "fusionPlant": 0,
        "metalStorage": 15,
        "crystalStorage": 14,
        "deuteriumStorage": 13
        }

    def select_upgrade(self, producers):
        result = None
        new_dict = {building_name: {**{"score": self.producers_list[building_name](producer["level"])}, **producer} for building_name, producer in producers.items()}
        new_dict = dict(filter(lambda x: x[1]["status"] == "on", new_dict.items()))
        new_dict = dict(filter(lambda x: x[1]["level"] < self.buildings_max_level[x[0]], new_dict.items()))

        if new_dict:
            result = min(new_dict.values(), key=lambda x:x["score"])
        return result


class SuppliesStorageUpgradeStrategy(SuppliesUpgradeBase):
    producers_list = {
                "metalMine":            lambda x: x,
                "crystalMine":          lambda x: x+2,
                "deuteriumSynthesizer": lambda x: x+8,
                "solarPlant":           lambda x: x+1,
                "fusionPlant":          lambda x: x+200, #no need
                "metalStorage":         lambda x: x,
                "crystalStorage":       lambda x: x+1,
                "deuteriumStorage":     lambda x: x+2
                }
    filter_list = [
        "metalMine",
        "crystalMine",
        "deuteriumSynthesizer",
        "solarPlant",
        "fusionPlant"
    ]

    def select_upgrade(self, producers):
        result = None
        new_dict = {building_name: {**{"score": self.producers_list[building_name](producer["level"])}, **producer} for building_name, producer in producers.items()}
        new_dict = dict(filter(lambda x: x[1]["status"] == "on", new_dict.items()))
        new_dict = dict(filter(lambda x: x[1]["name"] not in self.filter_list, new_dict.items()))

        if new_dict:
            result = min(new_dict.values(), key=lambda x:x["score"])
        return result



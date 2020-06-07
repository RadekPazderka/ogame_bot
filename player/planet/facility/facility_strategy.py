
class FacilitiesUpgradeStrategy():

    def __init__(self):
        pass

    facilities_max_level = {
        "roboticsFactory": 10,
        "shipyard": 10,
        "researchLaboratory": 100,
        "allianceDepot": 2,
        "missileSilo": 3,
        "naniteFactory": 3,
        "terraformer": 4,
        "repairDock": 7
        }
    filter_list = [

    ]

    def select_upgrade(self, facilities):
        result = None

        new_dict = dict(filter(lambda x: x[1]["status"] == "on", facilities.items()))
        new_dict = dict(filter(lambda x: x[1]["level"] < self.facilities_max_level[x[0]], new_dict.items()))
        new_dict = dict(filter(lambda x: x[1]["name"] not in self.filter_list, new_dict.items()))

        if new_dict:
            result = min(new_dict.values(), key=lambda x:x["level"])
        return result

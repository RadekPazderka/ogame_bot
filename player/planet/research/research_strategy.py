import random

class ExamineResearchStrategy():
    RESEARCHES_MAX_LEVELS = {
        'energyTechnology': 8,
        'laserTechnology': 12,
        'ionTechnology': 6,
        'hyperspaceTechnology': 100,
        'plasmaTechnology': 100,
        'combustionDriveTechnology': 20,
        'impulseDriveTechnology': 100,
        'hyperspaceDriveTechnology': 100,
        'espionageTechnology': 100,
        'computerTechnology': 100,
        'astrophysicsTechnology': 100,
        'researchNetworkTechnology': 100,
        'gravitonTechnology': 1,
        'weaponsTechnology': 100,
        'shieldingTechnology': 100,
        'armorTechnology': 100
        }


    def select_upgrade(self, researches):
        result = None
        for name, research_data in researches.items():
            if research_data["level"] < self.RESEARCHES_MAX_LEVELS[name]:
                researches[name]["available"] = True
            else:
                researches[name]["available"] = False

        researches = dict(filter(lambda x: x[1]["available"] and x[1]["status"] == "on", researches.items()))
        if researches:
            result = random.choice(list(researches.values()))

        return result
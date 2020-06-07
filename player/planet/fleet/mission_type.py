class MissionType(object):
    MAPPING = {'Attack': 1,
               'GroupedAttack': 2,
               'Transport': 3,
               'Park': 4,
               'ParkInThatAlly': 5,
               'Spy': 6,
               'Colonize': 7,
               'RecycleDebrisField': 8,
               'Destroy': 9,
               'Expedition': 15}

    def __init__(self, mission_type_name, holding_time):
        self._mission_type_name = mission_type_name
        self._mission_id = self.MAPPING[mission_type_name]
        self._holding_time = holding_time

    def __str__(self):
        return str(self._mission_type_name)

    def to_payload(self):
        return {
            "holdingtime": self._holding_time,
            "mission": self._mission_id
        }

class MissionTypeBuilder(object):

    @staticmethod
    def Attack():
        return MissionType(mission_type_name="Attack", holding_time=0)

    @staticmethod
    def GroupedAttack():
        return MissionType(mission_type_name="GroupedAttack", holding_time=0)

    @staticmethod
    def Transport():
        return MissionType(mission_type_name="Transport", holding_time=0)

    @staticmethod
    def Park():
        return MissionType(mission_type_name="Park", holding_time=0)

    @staticmethod
    def ParkInThatAlly():
        return MissionType(mission_type_name="ParkInThatAlly", holding_time=0)

    @staticmethod
    def Spy():
        return MissionType(mission_type_name="Spy", holding_time=0)

    @staticmethod
    def Colonize():
        return MissionType(mission_type_name="Colonize", holding_time=0)

    @staticmethod
    def RecycleDebrisField():
        return MissionType(mission_type_name="RecycleDebrisField", holding_time=0)

    @staticmethod
    def Destroy():
        return MissionType(mission_type_name="Destroy", holding_time=0)

    @staticmethod
    def Expedition(holding_time=1):
        return MissionType(mission_type_name="Expedition", holding_time=holding_time)





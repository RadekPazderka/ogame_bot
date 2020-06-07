
class FleetBase(object):
    INTEGRITY = 0
    ID = 0
    NAME = ""
    TYPE = ""

    def __init__(self, count):
        self._count = int(count)

    def get_integrity(self):
        return self.INTEGRITY * self._count

    @property
    def count(self):
        return self._count

    def __repr__(self):
        return "{}: {}".format(self.NAME, self._count)

class TransporterSmall(FleetBase):
    NAME = "transporterSmall"
    ID = 202
    INTEGRITY = 4000
    TYPE = "civil"

class TransporterLarge(FleetBase):
    NAME = "transporterLarge"
    ID = 203
    INTEGRITY = 12000
    TYPE = "civil"

class ColonyShip(FleetBase):
    NAME = "colonyShip"
    ID = 208
    INTEGRITY = 30000
    TYPE = "civil"

class Recycler(FleetBase):
    NAME = "recycler"
    ID = 209
    INTEGRITY = 16000
    TYPE = "civil"

class EspionageProbe(FleetBase):
    NAME = "espionageProbe"
    ID = 210
    INTEGRITY = 1000
    TYPE = "civil"

class FighterLight(FleetBase):
    NAME = "fighterLight"
    ID = 204
    INTEGRITY = 4000
    TYPE = "military"

class FighterHeavy(FleetBase):
    NAME = "fighterHeavy"
    ID = 205
    INTEGRITY = 10000
    TYPE = "military"

class Cruiser(FleetBase):
    NAME = "cruiser"
    ID = 206
    INTEGRITY = 27000
    TYPE = "military"

class Battleship(FleetBase):
    NAME = "battleship"
    ID = 207
    INTEGRITY = 60000
    TYPE = "military"

class Interceptor(FleetBase):
    NAME = "interceptor"
    ID = 215
    INTEGRITY = 70000
    TYPE = "military"

class Bomber(FleetBase):
    NAME = "bomber"
    ID = 211
    INTEGRITY = 75000
    TYPE = "military"

class Destroyer(FleetBase):
    NAME = "destroyer"
    ID = 213
    INTEGRITY = 110000
    TYPE = "military"

class Deathstar(FleetBase):
    NAME = "deathstar"
    ID = 214
    INTEGRITY = 9000000
    TYPE = "military"

class Reaper(FleetBase):
    NAME = "reaper"
    ID = 218
    INTEGRITY = 140000
    TYPE = "military"

class Explorer(FleetBase):
    NAME = "explorer"
    ID = 219
    INTEGRITY = 23000
    TYPE = "military"

class SolarSatellite(FleetBase):
    NAME = "solarSatellite"
    ID = 212
    INTEGRITY = 1000
    TYPE = "civil"

class Resbuggy(FleetBase):
    NAME = "resbuggy"
    ID = 217
    INTEGRITY = 0
    TYPE = "civil"


class FleetBuilder(object):
    MAPPING = {
        202 : TransporterSmall,
        203 : TransporterLarge,
        208 : ColonyShip,
        209 : Recycler,
        210 : EspionageProbe,
        204 : FighterLight,
        205 : FighterHeavy,
        206 : Cruiser,
        207 : Battleship,
        215 : Interceptor,
        211 : Bomber,
        213 : Destroyer,
        214 : Deathstar,
        218 : Reaper,
        219 : Explorer,
        212 : SolarSatellite,
        217 : Resbuggy
    }

    def __init__(self):
        self._fleet = []

    def add_fleet_by_id(self, fleet_id: int, count:int):
        self._fleet.append(self.MAPPING[int(fleet_id)](count))

    def with_transporterSmall(self, count: int):
        self._fleet.append(TransporterSmall(count))
        return self

    def with_transporterLarge(self, count):
        self._fleet.append(TransporterLarge(count))
        return self

    def with_colonyShip(self, count):
        self._fleet.append(ColonyShip(count))
        return self

    def with_recycler(self, count):
        self._fleet.append(Recycler(count))
        return self

    def with_espionageProbe(self, count):
        self._fleet.append(EspionageProbe(count))
        return self

    def with_fighterLight(self, count):
        self._fleet.append(FighterLight(count))
        return self

    def with_fighterHeavy(self, count):
        self._fleet.append(FighterHeavy(count))
        return self

    def with_cruiser(self, count):
        self._fleet.append(Cruiser(count))
        return self

    def with_battleship(self, count):
        self._fleet.append(Battleship(count))
        return self

    def with_interceptor(self, count):
        self._fleet.append(Interceptor(count))
        return self

    def with_bomber(self, count):
        self._fleet.append(Bomber(count))
        return self

    def with_destroyer(self, count):
        self._fleet.append(Destroyer(count))
        return self

    def with_deathstar(self, count):
        self._fleet.append(Deathstar(count))
        return self

    def with_reaper(self, count):
        self._fleet.append(Reaper(count))
        return self

    def with_explorer(self, count):
        self._fleet.append(Explorer(count))
        return self

    def with_resbuggy(self, count):
        self._fleet.append(Resbuggy(count))
        return self

    def build(self):
        return FleetArmy(self._fleet)




class FleetArmy():

    def __init__(self, fleet: [FleetBase]):
        self._fleet = fleet
        self._payload_data = self._get_payload_data(self._fleet)


    def get_explorers(self):
        result = Explorer(0)
        for fleet in self._fleet:
            if fleet.NAME == "explorer":
                result = fleet
                break
        return result

    def get_bombers(self):
        result = Bomber(0)
        for fleet in self._fleet:
            if fleet.NAME == "bomber":
                result = fleet
                break
        return result




    def get_whole_integrity(self):
        return sum(fl.get_integrity() for fl in self._fleet)

    def split_fleet_into(self, parts: int):
        fleet_builder = FleetBuilder()
        for fleet in self._fleet:
            fleet_builder.add_fleet_by_id(fleet.ID, fleet.count//parts)
        return fleet_builder.build()

    def get_data(self):
        return [(fleet.ID, fleet.count, fleet.NAME)for fleet in self._fleet]

    def get_fleet_data(self):
        return self._fleet

    def to_payload(self):
        return self._payload_data

    def _get_payload_data(self, fleets: [FleetBase]):
        return {"am{}".format(fleet.ID): fleet.count for fleet in fleets}

    def __repr__(self):
        return str(self._fleet)

if __name__ == '__main__':
    fleet = FleetBuilder().with_transporterSmall(40).with_transporterLarge(10).build()
    pass
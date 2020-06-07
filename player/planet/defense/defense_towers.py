class DefenseTower(object):
    INTEGRITY = 0
    ID = 0
    NAME = ""

    def __init__(self, count):
        self._count = count

    @property
    def count(self):
        return self._count

    def get_integrity(self):
        return self.INTEGRITY * self._count

    def __repr__(self):
        return "{}: {}".format(self.NAME, self._count)

class RocketLauncher(DefenseTower):
    INTEGRITY = 2000
    ID = 401
    NAME = "rocketLauncher"

class LaserCannonLight(DefenseTower):
    INTEGRITY = 2000
    ID = 402
    NAME = "laserCannonLight"

class LaserCannonHeavy(DefenseTower):
    INTEGRITY = 8000
    ID = 403
    NAME = "laserCannonHeavy"

class GaussCannon(DefenseTower):
    INTEGRITY = 35000
    ID = 404
    NAME = "gaussCannon"

class IonCannon(DefenseTower):
    INTEGRITY = 8000
    ID = 405
    NAME = "ionCannon"

class PlasmaCannon(DefenseTower):
    INTEGRITY = 100000
    ID = 406
    NAME = "plasmaCannon"

class ShieldDomeSmall(DefenseTower):
    INTEGRITY = 20000
    ID = 407
    NAME = "shieldDomeSmall"

class ShieldDomeLarge(DefenseTower):
    INTEGRITY = 100000
    ID = 408
    NAME = "shieldDomeLarge"

class MissileInterceptor(DefenseTower):
    INTEGRITY = 0
    ID = 502
    NAME = "missileInterceptor"

class MissileInterplanetary(DefenseTower):
    INTEGRITY = 0
    ID = 503
    NAME = "missileInterplanetary"



class DefenseTowersBuilder(object):
    MAPPING = {
        401 : RocketLauncher,
        402 : LaserCannonLight,
        403 : LaserCannonHeavy,
        404 : GaussCannon,
        405 : IonCannon,
        406 : PlasmaCannon,
        407 : ShieldDomeSmall,
        408 : ShieldDomeLarge,
        502 : MissileInterceptor,
        503 : MissileInterplanetary
    }

    def __init__(self):
        self._defense_towers = []

    def add_defense_by_id(self, defense_id: int, count:int):
        self._defense_towers.append(DefenseTowersBuilder.MAPPING[int(defense_id)](count))

    def with_rocketLauncher(self, count: int):
        self._defense_towers.append(RocketLauncher(count))
        return self

    def with_laserCannonLight(self, count: int):
        self._defense_towers.append(LaserCannonLight(count))
        return self

    def with_laserCannonHeavy(self, count: int):
        self._defense_towers.append(LaserCannonHeavy(count))
        return self

    def with_gaussCannon(self, count: int):
        self._defense_towers.append(GaussCannon(count))
        return self

    def with_ionCannon(self, count: int):
        self._defense_towers.append(IonCannon(count))
        return self

    def with_plasmaCannon(self, count: int):
        self._defense_towers.append(PlasmaCannon(count))
        return self

    def with_shieldDomeSmall(self, count: int):
        self._defense_towers.append(ShieldDomeSmall(count))
        return self

    def with_shieldDomeLarge(self, count: int):
        self._defense_towers.append(ShieldDomeLarge(count))
        return self

    def with_missileInterceptor(self, count: int):
        self._defense_towers.append(MissileInterceptor(count))
        return self

    def with_missileInterplanetary(self, count: int):
        self._defense_towers.append(MissileInterplanetary(count))
        return self

    def build(self):
        return DefenseArmy(self._defense_towers)

class DefenseArmy():

    def __init__(self, defense_towers: [DefenseTower]):
        self._defense_towers = defense_towers

    def get_whole_integrity(self):
        return sum(tower.get_integrity() for tower in self._defense_towers)

    def count(self):
        return len(self._defense_towers)

    def get_data(self):
        return [(defense_tower.ID, defense_tower.count, defense_tower.NAME)for defense_tower in self._defense_towers]

    def __repr__(self):
        return str(self._defense_towers)

if __name__ == '__main__':
    "{}".format(DefenseArmy())
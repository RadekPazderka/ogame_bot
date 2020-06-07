from player.planet.fleet.fleet_army import FleetArmy
from player.planet.defense.defense_towers import DefenseArmy
from player.planet.fleet.coord import Location
from player.planet.resources.resources_status import ResourcesStatus

class SpyMessageDetail():
    def __init__(self,
                 location: Location,
                 resources: ResourcesStatus,
                 fleet: FleetArmy,
                 defense: DefenseArmy,
                 buildings=None,
                 research=None):
        self._location = location
        self._resources = resources
        self._fleet = fleet
        self._defense = defense
        self._buildings = buildings
        self._research = research

    @property
    def location(self):
        return self._location

    @property
    def resources(self):
        return self._resources

    @property
    def fleet(self):
        return self._fleet

    @property
    def defense(self):
        return self._defense

    @property
    def buildings(self):
        return self._buildings

    @property
    def research(self):
        return self._research

    def __repr__(self):
        return "{} {} {} {} {} {}\n".format(self._location, self._resources, self._fleet, self._defense, self._buildings, self._research)

    def __str__(self):
        return "{} {} {} {} {} {}\n".format(self._location, self._resources, self._fleet, self._defense, self._buildings, self._research)
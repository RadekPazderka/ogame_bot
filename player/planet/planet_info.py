from player.planet.building.building_manager import BuildingManager
from player.planet.research.reseach_manager import ResearchManager
from player.planet.hangar.hangar_manager import HangarManager
from player.planet.defense.defense_manager import DefenseManager
from player.planet.fleet.coord import Coord, Location, DestinationType
from player.planet.fleet.fleet_manager import FleetManager
from player.planet.facility.facility_manager import FacilityManager
from player.ogame_client import OgameClient
from player.planet.galaxy_explorer.galaxy_explorer_manager import GalaxyExplorerManager

class PlanetInfo():

    def __init__(self, comm, planet_id):
        self._comm = comm
        self._planet_id =  planet_id
        overview_page = OgameClient.get_overview(self._comm, self._planet_id)
        self._planet_name = overview_page.get_planet_name()
        self._location = overview_page.get_location()
        self._galaxy_explorer_manager = GalaxyExplorerManager(comm, planet_id, self._location)
        self._fleet_manager = None
        self._reseach_manager = None
        self._buildings = None
        self._facility_manager = None
        self._hangar_manager = None

        self._defense_manager = None

    @property
    def name(self):
        return self._planet_name

    @property
    def id(self):
        return self._planet_id

    @property
    def location(self):
        return self._location

    @property
    def fleet_manager(self):
        if self._fleet_manager is None:
            self._fleet_manager = FleetManager(self._comm, self._planet_id, self._location, self._planet_name)
        return self._fleet_manager

    @property
    def building_manager(self):
        if self._buildings is None:
            self._buildings = BuildingManager(self._comm, self._planet_id, self._planet_name)
        return self._buildings

    @property
    def facility_manager(self):
        if self._facility_manager is None:
            self._facility_manager = FacilityManager(self._comm, self._planet_id, self._planet_name)
        return self._facility_manager

    @property
    def reseach_manager(self):
        if self._reseach_manager is None:
            self._reseach_manager = ResearchManager(self._comm, self._planet_id, self._planet_name)
        return self._reseach_manager

    @property
    def hangar_manager(self):
        if self._hangar_manager is None:
            self._hangar_manager = HangarManager(self._comm, self._planet_id, self._planet_name)
        return self._hangar_manager

    @property
    def defense_manager(self):
        if self._defense_manager is None:
            self._defense_manager = DefenseManager(self._comm, self._planet_id, self._planet_name)
        return self._defense_manager


    @property
    def galaxy_explorer_manager(self):
        return self._galaxy_explorer_manager

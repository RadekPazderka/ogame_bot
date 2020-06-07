from session_wrapper import SesstionWrapper
from player.planet.fleet.coord import Location
from player.planet.fleet.fleet_army import FleetArmy
from player.planet.fleet.mission_type import MissionType
from player.ogame_client import OgameClient

class FleetDispatcher(object):

    def __init__(self, comm, planet_id):
        assert isinstance(comm, SesstionWrapper)
        self._comm = comm
        self._planet_id = planet_id


    def send_fleet(self, location: Location, mission_type: MissionType, fleet: FleetArmy):
        assert isinstance(location, Location)
        assert isinstance(mission_type, MissionType)
        assert isinstance(fleet, FleetArmy)

        print("Sending {} to {}".format(mission_type, location))
        fleetdispatch_page = OgameClient.get_fleet_dispatch(self._comm, self._planet_id)
        token = fleetdispatch_page._get_token()

        """****** stage 1 ******"""
        stage1_payload = FleetDispatcher._build_stage1_payload(location, fleet)
        stage1_params = FleetDispatcher._build_stage1_params()
        res_stage_1 = OgameClient.post_action(self._comm, params=stage1_params, data=stage1_payload)

        """****** stage 2 ******"""
        stage2_payload = FleetDispatcher._build_stage2_payload(stage1_payload, mission_type, token)
        stage2_params = FleetDispatcher._build_stage2_params()
        res_stage_2 = OgameClient.post_action(self._comm, params=stage2_params, data=stage2_payload)


    @staticmethod
    def _build_stage1_payload(location: Location, fleet: FleetArmy):
        constants = {
            "union": str("0")
        }
        return {**location.to_payload(), **fleet.to_payload(), **constants}

    @staticmethod
    def _build_stage1_params():
        return {
            "page": "ingame",
            "component": "fleetdispatch",
            "action": "checkTarget",
            "ajax": "1",
            "asJson": "1"
        }

    @staticmethod
    def _build_stage2_payload(stage1_payload, mission_type: MissionType, token, speed=10):
        constants = {
            "metal": 0,
            "crystal": 0,
            "deuterium": 0,
            "prioCrystal": 2,
            "prioDeuterium": 3,
            "prioMetal": 1,
            "retreatAfterDefenderRetreat": 0,
            "speed": speed,
            "token": token  # TODO: is it correct?
        }
        return {**stage1_payload, **mission_type.to_payload(), **constants}

    @staticmethod
    def _build_stage2_params():
        return {
            "page": "ingame",
            "component": "fleetdispatch",
            "action": "sendFleet",
            "ajax": "1",
            "asJson": "1"
        }



import copy
import random
from typing import List

from player.planet.fleet.fleet_army import FleetBuilder
from player.planet.fleet.fleet_info import FleetDispatcher
from player.planet.fleet.fleet_status import FleetStatus
from player.planet.fleet.mission_type import MissionTypeBuilder
from player.planet.fleet.coord import Coord, Location, DestinationTypeBuilder
from player.ogame_client import OgameClient
from player.messages.spy_message_detail import SpyMessageDetail
from player.planet.fleet.fleet_targets_wrapper import FLEET_TARGET_CONFIG

import time

from spy_reports.spy_logger import SpyLogger


class FleetManager(object):

    def __init__(self, comm, planet_id, planet_location: Location, planet_name: str):
        self._comm = comm
        self._planet_id = planet_id
        self._fleet_dispatcher = FleetDispatcher(comm, planet_id)
        self._planet_location = planet_location
        self._planet_name = planet_name

    def send_expeditions(self):
        fleet_status = self._update_fleet_status()

        send_expedition = fleet_status.get_free_expedition_slots()

        for _ in range(send_expedition):
            fleet = fleet_status.fleet_army.split_fleet_into(send_expedition)
            exp_coord = Location(Coord(self._planet_location.coord.galaxy,self._planet_location.coord.system, 16),
                                 DestinationTypeBuilder.planet())
            time.sleep(random.randint(5,10))
            print("Sleep before sending expeditions")
            self._fleet_dispatcher.send_fleet(exp_coord, MissionTypeBuilder().Expedition(), fleet)

    def send_farm_attacks(self):
        fleet_status = self._update_fleet_status()

        free_fleet_slots = fleet_status.get_free_fleet_slots()
        for _ in range(free_fleet_slots):
            target = FLEET_TARGET_CONFIG.get_next_target()

            location = Location(Coord(target["galaxy"], target["system"], target["position"]), DestinationTypeBuilder.planet())
            self._fleet_dispatcher.send_fleet(location, MissionTypeBuilder.Attack(), FleetBuilder().with_transporterSmall(42).build())

    def send_farm_attacks_by_spy(self, spy_messages: List[SpyMessageDetail]):
        fleet_status = self._update_fleet_status()
        free_fleet_slots = fleet_status.get_free_fleet_slots()
        spy_messages = list(sorted(spy_messages, key=lambda x: x.resources.get_sum(), reverse=True))
        SpyLogger.save_into_file(spy_messages, self._planet_name)
        print(spy_messages)


        #spy_messages = list(filter(lambda x: (x.fleet.get_whole_integrity() + x.defense.get_whole_integrity()) == 0, spy_messages))

        for i in range(len(spy_messages)):
            fleet_builder = FleetBuilder()
            location = spy_messages[i].location
            farm_resources = spy_messages[i].resources.get_sum()
            planet_integrity = spy_messages[i].defense.get_whole_integrity() + spy_messages[i].fleet.get_whole_integrity()
            if planet_integrity == 0:
                bombers_needed = 0
            else:
                bombers_needed = (planet_integrity // 5000) + 2
            bombers_count = fleet_status.fleet_army.get_bombers().count
            if bombers_needed <= bombers_count:
                fleet_builder.with_bomber(bombers_needed)
            else:
                print("Need more bombers ({0}/{1})".format(bombers_count, bombers_needed))
                continue
            transporterSmall_count = int(farm_resources*0.75 / 8500.0)+2
            fleet_builder.with_transporterSmall(transporterSmall_count)

            time.sleep(random.randint(5,10))
            fleet_army = fleet_builder.build()
            print("sleep before sending attack ({})".format(fleet_army))

            self._fleet_dispatcher.send_fleet(location, MissionTypeBuilder.Attack(), fleet_army)
            free_fleet_slots -= 1
            if not free_fleet_slots:
                break
            fleet_status = self._update_fleet_status()


    def send_spy(self, location:Location, count:int):
        fleet_status = self._update_fleet_status()
        free_fleet_slots = fleet_status.get_free_fleet_slots()
        if free_fleet_slots:
            self._fleet_dispatcher.send_fleet(location, MissionTypeBuilder.Spy(), FleetBuilder().with_espionageProbe(count).build())
            return True
        return False

    def send_spy_to_inactive_players(self, inactive_players):
        for inactiove_player in inactive_players:
            location = Location(inactiove_player["coord"], DestinationTypeBuilder.planet())
            res = self.send_spy(location, 20)
            while not res:
                res = self.send_spy(location, 20)
                print("Waiting for fleet slots... (10 sec..)")
                time.sleep(10)
        print("sleep after spy... 20s")
        time.sleep(20)

    def send_explorers_to_debris(self, max_explorers):
        if max_explorers == 0:
            return

        fleet_status = self._update_fleet_status()
        free_fleet_slots = fleet_status.get_free_fleet_slots()
        explorers_count = min(max_explorers, fleet_status.fleet_army.get_explorers().count)
        if free_fleet_slots == 0:
            return
        if explorers_count == 0:
            print("We haven't explorers to harvest debris.")
            return

        debris_location = Location(Coord(self._planet_location.coord.galaxy, self._planet_location.coord.system, 16), DestinationTypeBuilder.debris())
        explorer_army = FleetBuilder().with_explorer(explorers_count).build()
        self._fleet_dispatcher.send_fleet(debris_location, MissionTypeBuilder.RecycleDebrisField(), explorer_army)

    def _update_fleet_status(self) -> FleetStatus:
        fleet_dispatch = OgameClient.get_fleet_dispatch(self._comm, self._planet_id)
        return fleet_dispatch.get_fleet_status()
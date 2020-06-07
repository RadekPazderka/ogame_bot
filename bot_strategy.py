from account_logger import AccountLogger
from player.planet.fleet.fleet_army import FleetBuilder
from player.planet.defense.defense_towers import DefenseTowersBuilder
from player.planet.fleet.coord import Coord, Location, DestinationTypeBuilder
import time
import random

class BotStrategy(object):

    @staticmethod
    def farm_strategy(username, password, player_name):

        while True:
            try:
                acc_logger = AccountLogger()
                player_info = acc_logger.login(username, password, player_name)
                #player_info.planets.get_by_name("Mazlik").fleet_manager.send_expeditions(1)
                player_info.planets.get_by_name("Kulisek").fleet_manager.send_expeditions()
                player_info.planets.get_by_name("DarkWolf").fleet_manager.send_farm_attacks()

                #player_info.planets.get_by_name("Kulisek").reseach_manager.make_reseach()

                # fleet = FleetBuilder().with_transporterLarge(10).with_fighterHeavy(20).build()
                # player_info.planets.get_by_name("DarkWolf").hangar_manager.make_fleet(fleet)

               # player_info.planets.get_by_name("Kulisek").building_manager.build_storages()
                for planet in player_info.planets.get_all():
                    planet.facility_manager.build_facilities()
                    planet.building_manager.build_buildings()

            except:
                print("GLOBAL ERROR")

            sleep_time = random.randint(300, 500)
            print("Sleep: {} seconds".format(sleep_time))
            time.sleep(sleep_time)

    @staticmethod
    def develop_strategy(username, password, player_name):
        EVERY_N_CYCLES_SPY = 1
        curr_cyrcle = 0
        attack_planet_index = 6
        while True:
            try:
                acc_logger = AccountLogger()
                player_info = acc_logger.login(username, password, player_name)

                #player_info.planets.get_by_name("DarkWolf").facility_manager.build_facilities()
                # player_info.planets.get_by_name("DarkWolf").reseach_manager.make_reseach()
                # fleet = FleetBuilder().with_transporterLarge(10).with_fighterHeavy(20).build()
                # player_info.planets.get_by_name("DarkWolf").hangar_manager.make_fleet(fleet)

                debris = player_info.planets.get_by_name("Kulisek").galaxy_explorer_manager.get_galaxy_debris()
                player_info.planets.get_by_name("Kulisek").fleet_manager.send_explorers_to_debris(debris["explorers"])
                player_info.planets.get_by_name("Kulisek").fleet_manager.send_expeditions()
                player_info.planets.get_by_name("Kulisek").reseach_manager.make_reseach()

                for planet in player_info.planets.get_all():
                    planet.facility_manager.build_facilities()
                    planet.building_manager.build_buildings()
                    #planet.defense_manager.make_defense(DefenseTowersBuilder().with_plasmaCannon(2).with_rocketLauncher(30).build())

                ######################################################################################################

                if curr_cyrcle % EVERY_N_CYCLES_SPY == 0:
                    while True:
                        attacker_planet = player_info.planets.get_all()[attack_planet_index]
                        attack_planet_index += 1
                        attack_planet_index %= len(player_info.planets.get_all())
                        if attacker_planet.name not in ["Kulisek", "DarkWolf"]:
                            break

                    all_near_inactive_players = attacker_planet.galaxy_explorer_manager.explore_near_planet(50)
                    player_info.message_manager.clear_messages()
                    attacker_planet.fleet_manager.send_spy_to_inactive_players(all_near_inactive_players)

                    spy_messages = player_info.message_manager.get_spy_messages()
                    attacker_planet.fleet_manager.send_farm_attacks_by_spy(spy_messages)

            except:
                print("GLOBAL ERROR")
            curr_cyrcle += 1
            sleep_time = random.randint(1000, 1300)
            print("Sleep: {} seconds".format(sleep_time))
            time.sleep(sleep_time)

from pages.defense_page import DefensePage
from pages.fleet_dispatch_page import FleetDispatchPage
from pages.overview_page import OverviewPage
from pages.planet_detail_page import PlanetDetailPage
from pages.resource_page import ResourcePage
from pages.spy_message_detail_page import SpyMessageDetailPage
from pages.supplies_page import SuppliesPage
from pages.galaxy_page import GalaxyPage
from pages.research_page import ResearchPage
from pages.hangar_page import HangarPage
from pages.facilities_page import FacilitiesPage
from pages.spy_messages_page import SpyMessagesPage, SpyReport
from session_wrapper import SesstionWrapper

from player.planet.fleet.coord import Coord

class OgameClient():

    BASE_URL = "https://s146-cz.ogame.gameforge.com/"

    OVERVIEW_ENDPOINT = "game/index.php?page=ingame&component=overview"
    SUPPLIES_ENDPOINT = "game/index.php?page=ingame&component=supplies"
    FACILITIES_ENDPOINT = "game/index.php?page=ingame&component=facilities"
    RESEACH_ENDPOINT = "game/index.php?page=ingame&component=research"
    SHIPYARD_ENDPOINT = "game/index.php?page=ingame&component=shipyard"
    DEFENSE_ENDPOINT = "game/index.php?page=ingame&component=defenses"
    FLEET_DISPATCH_ENDPOINT = "game/index.php?page=ingame&component=fleetdispatch"
    GALAXY_ENDPOINT = "game/index.php?page=ingame&component=galaxyContent&ajax=1"
    MESSAGES_ENDPOINT = "game/index.php?page=messages"
    SPY_MESSAGES_ENDPOINT = "game/index.php?page=messages&tab=20&ajax=1"
    ACTION_ENDPOINT = "game/index.php"

    @staticmethod
    def get_planet_detail(context: SesstionWrapper, planet_id: str) -> PlanetDetailPage:
        url = OgameClient.BASE_URL + OgameClient.OVERVIEW_ENDPOINT

        response = context.get(url, params={"cp": planet_id})

        return PlanetDetailPage(response)

    @staticmethod
    def get_overview(context: SesstionWrapper, planet_id:str=None) -> OverviewPage:
        url = OgameClient.BASE_URL + OgameClient.OVERVIEW_ENDPOINT

        response = context.get(url, params={"cp": planet_id})

        return OverviewPage(response)

    @staticmethod
    def get_supplies(context: SesstionWrapper, planet_id: str) -> SuppliesPage:
        url = OgameClient.BASE_URL + OgameClient.SUPPLIES_ENDPOINT

        response = context.get(url, params={"cp": planet_id})

        return SuppliesPage(response)

    @staticmethod
    def get_facilities(context: SesstionWrapper, planet_id: str) -> FacilitiesPage:
        url = OgameClient.BASE_URL + OgameClient.FACILITIES_ENDPOINT

        response = context.get(url, params={"cp": planet_id})

        return FacilitiesPage(response)


    @staticmethod
    def get_reseach(context: SesstionWrapper, planet_id: str) -> ResearchPage:
        url = OgameClient.BASE_URL + OgameClient.RESEACH_ENDPOINT

        response = context.get(url, params={"cp": planet_id})

        return ResearchPage(response)


    @staticmethod
    def get_hangar(context: SesstionWrapper, planet_id: str) -> HangarPage:
        url = OgameClient.BASE_URL + OgameClient.SHIPYARD_ENDPOINT

        response = context.get(url, params={"cp": planet_id})

        return HangarPage(response)

    @staticmethod
    def get_defense(context: SesstionWrapper, planet_id: str) -> DefensePage:
        url = OgameClient.BASE_URL + OgameClient.DEFENSE_ENDPOINT

        response = context.get(url, params={"cp": planet_id})

        return DefensePage(response)


    @staticmethod
    def get_fleet_dispatch(context: SesstionWrapper, planet_id: str) -> FleetDispatchPage:
        url = OgameClient.BASE_URL + OgameClient.FLEET_DISPATCH_ENDPOINT

        response = context.get(url, params={"cp": planet_id})

        return FleetDispatchPage(response)

    def get_resources(self, context: SesstionWrapper, planet_id: str) -> ResourcePage:
        url = OgameClient.BASE_URL + OgameClient.OVERVIEW_ENDPOINT

        response = context.get(url, params={"cp": planet_id})
        return ResourcePage(response)

    @staticmethod
    def post_action(context: SesstionWrapper, params, data):
        url = OgameClient.BASE_URL + OgameClient.SUPPLIES_ENDPOINT

        return context.post(url, params=params, data=data)

    @staticmethod
    def get_galaxy(context: SesstionWrapper, planet_id, coord: Coord):
        url = OgameClient.BASE_URL + OgameClient.GALAXY_ENDPOINT

        payload = {
            "galaxy": coord.galaxy,
            "system": coord.system
        }
        response = context.post(url, data=payload,params={"cp": planet_id})
        return GalaxyPage(response)

    @staticmethod
    def get_spy_messages(context: SesstionWrapper):
        url = OgameClient.BASE_URL + OgameClient.SPY_MESSAGES_ENDPOINT
        response = context.get(url)
        return SpyMessagesPage(response)

    @staticmethod
    def get_spy_message_detail(context: SesstionWrapper, msg_detail: SpyReport):
        url = OgameClient.BASE_URL + OgameClient.SPY_MESSAGES_ENDPOINT
        params = {
            "messageId": msg_detail.msg_id,
            "tabid": 20,
            "ajax": 1
        }

        response = context.get(url,params=params)
        return SpyMessageDetailPage(response)

    @staticmethod
    def remove_message(context: SesstionWrapper, msg_detail: SpyReport):
        url = OgameClient.BASE_URL + OgameClient.MESSAGES_ENDPOINT

        payload = {
            "messageId": msg_detail.msg_id,
            "action": 103,
            "ajax": 1
        }
        context.post(url, data=payload)
        return True

    @staticmethod
    def clear_messages(context: SesstionWrapper, messages_type):
        url = OgameClient.BASE_URL + OgameClient.MESSAGES_ENDPOINT

        payload = {
            "tabid": 20, #TODO: messages_type (20 = spy messages..)
            "messageId": -1,
            "action": 103,
            "ajax": 1
        }
        context.post(url, data=payload)
        return True


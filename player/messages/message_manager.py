from session_wrapper import SesstionWrapper
from player.ogame_client import OgameClient
from player.messages.spy_message_detail import SpyMessageDetail


class MessageManager():

    def __init__(self, comm: SesstionWrapper):
        self._comm = comm

    def clear_messages(self):
        OgameClient.clear_messages(self._comm, 20)

    def get_spy_messages(self) -> [SpyMessageDetail]:
        spy_msg_reports = True
        spy_message_details = []
        while spy_msg_reports:
            spy_msg_reports = OgameClient.get_spy_messages(self._comm).get_spy_messages()

            for report in spy_msg_reports:
                msg_detail_page = OgameClient.get_spy_message_detail(self._comm, report)
                location = msg_detail_page.get_location()
                resources = msg_detail_page.get_resources()
                fleet = msg_detail_page.get_fleet()
                defense = msg_detail_page.get_defense()
                buildings = msg_detail_page.get_buildings()
                research = msg_detail_page.get_research()
                spy_message_details.append(SpyMessageDetail(location, resources, fleet, defense, buildings, research))
                OgameClient.remove_message(self._comm, report)
        return spy_message_details
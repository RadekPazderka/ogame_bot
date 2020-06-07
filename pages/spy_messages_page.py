from bs4 import BeautifulSoup
from player.messages.message_info import SpyReport


class SpyMessagesPage():

    def __init__(self, content):
        self._parser = BeautifulSoup(content, "lxml")

    def get_spy_messages(self):
        msgs = self._parser.find("div", attrs={"id": "fleetsgenericpage"})
        messages_data = msgs.find_all("li", attrs={"class": "msg"})

        return [SpyReport(int(msg_id.attrs["data-msg-id"])) for msg_id in messages_data]
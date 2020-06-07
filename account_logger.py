import json

from session_wrapper import SesstionWrapper
from player.player_info import PlayerInfo
import re

class AccountLogger:

    def login(self, username, password, account_name):
        comm = SesstionWrapper()

        self._login_user(comm, username, password)
        server_info = self._select_account(comm, account_name)

        return PlayerInfo(comm, server_info)

    def _login_user(self, comm, username, password):
        js_config_script = comm.get("https://lobby.ogame.gameforge.com/config/configuration.js")
        res = re.search("\"gameEnvironmentId\":\"([a-z0-9\-]+)\".*\"platformGameId\":\"([a-z0-9\-]+)\".*\"", js_config_script)
        gameEnvironmentId = res.group(1)
        platformGameId = res.group(2)

        payload = {
            "identity": username,
            "password": password,
            "locale": "cs_CZ",
            "gfLang": "cz",
            "platformGameId": platformGameId,
            "gameEnvironmentId": gameEnvironmentId,
            "autoGameAccountCreation": False
        }

        token = json.loads(comm.post('https://gameforge.com/api/v1/auth/thin/sessions', json=payload))["token"]
        comm.update_cookie("gf-token-production", token, ".gameforge.com")
        #authorization: Bearer cdb91a9d-4b1d-45c5-b50b-9be35d61e49a
        comm.update_header("authorization", "{} {}".format("Bearer", token))


    def _select_account(self, comm, account_name):

        accounts = json.loads(comm.get("https://lobby.ogame.gameforge.com/api/users/me/accounts"))
        acc = list(filter(lambda x: x["name"] == account_name, accounts))[0]
        PARAMS = {
            "id": acc["id"],
            "server[language]": acc["server"]["language"],
            "server[number]": acc["server"]["number"],
            "clickedButton": "account_list"
        }
        r = comm.get('https://lobby.ogame.gameforge.com/api/users/me/loginLink', params=PARAMS)
        comm.get(json.loads(r)["url"])

        return acc["server"]

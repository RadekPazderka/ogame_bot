# username: "odfbqorffhgijgdhxc@ttirv.org"
# password: "test123"

# POST
# https://lobby.ogame.gameforge.com/api/users
# data: {"credentials":{"email":"odfbqorffhgijgdhxc@ttirv.org","password":"test123"},"language":"cz","kid":"","autoLogin":false}

# GET
# https://lobby.ogame.gameforge.com/api/users/me/accounts
# resp: [{"server":{"language":"cz","number":147},"id":101705,"gameAccountId":101705,"name":"Lord Vela","lastPlayed":"2020-05-03T11:12:41+0000","lastLogin":"2020-05-03T11:12:41+0000","blocked":false,"bannedUntil":null,"bannedReason":null,"details":[{"type":"literal","title":"myAccounts.rank","value":"908"},{"type":"localized","title":"myAccounts.status","value":"playerStatus.active"}],"sitting":{"shared":false,"endTime":null,"cooldownTime":null},"trading":{"trading":false,"cooldownTime":null}}]

# GET
# https://lobby.ogame.gameforge.com/api/users/me/loginLink?id=101705&server[language]=cz&server[number]=147&clickedButton=account_list
# resp: {"url":"https:\/\/s147-cz.ogame.gameforge.com\/game\/lobbylogin.php?id=101705&token=e2a99cb0-58bf-40e1-b4b9-f3b90000b8c4"}

import requests
import json

from bs4 import BeautifulSoup


def login(username, password, account_name):
    session = requests.Session()
    payload = {"credentials":{"email":username,"password":password},
               "language":"cz","kid":"","autoLogin":False}

    session.post("https://lobby.ogame.gameforge.com/api/users", json=payload)


    json_resp = session.get("https://lobby.ogame.gameforge.com/api/users/me/accounts").content
    accounts = json.loads(json_resp)
    acc = list(filter(lambda x: x["name"] == account_name, accounts))[0]

    params = {
        "id": acc["id"],
        "server[language]": acc["server"]["language"],
        "server[number]": acc["server"]["number"],
        "clickedButton": "account_list"
    }
    resp_url = session.get("https://lobby.ogame.gameforge.com/api/users/me/loginLink", params=params).content
    login_url = json.loads(resp_url)["url"]
    session.get(login_url).content.decode("utf8")

    return session

def get_resources(sess: requests.Session):
    result = {}
    params = {
        "page": "ingame",
        "component": "overview"
    }
    #https://s147-cz.ogame.gameforge.com/game/index.php?page=ingame&component=overview
    page = sess.get("https://s147-cz.ogame.gameforge.com/game/index.php", params=params).content.decode("utf8")
    parsed_page = BeautifulSoup(page, "lxml")

    resources = parsed_page.find("div", attrs={"id": "resourcesbarcomponent"})

    resources_names = ["metal", "crystal", "deuterium", "energy"]
    for resource_name in resources_names:
        resource_raw = resources.find("span", attrs={"id": "resources_"+resource_name}).attrs["data-raw"]
        resource_count = int(float(resource_raw))
        result[resource_name] = resource_count

    return result


if __name__ == '__main__':
    sess = login("odfbqorffhgijgdhxc@ttirv.org", "test123", "Lord Vela")
    print(get_resources(sess))










































#POST
#https://lobby.ogame.gameforge.com/api/users
#data: {"credentials":{"email":"odfbqorffhgijgdhxc@ttirv.org","password":"test123"},"language":"cz","kid":"","autoLogin":false}


#GET
#https://lobby.ogame.gameforge.com/api/users/me/accounts


#GET
#https://lobby.ogame.gameforge.com/api/users/me/loginLink?id=101705&server[language]=cz&server[number]=147&clickedButton=account_list


# import requests
# import json
# from bs4 import BeautifulSoup
#
# def login(username, password, account_name):
#     session = requests.Session()
#
#     payload = {"credentials": {"email": "odfbqorffhgijgdhxc@ttirv.org", "password": "test123"}, "language": "cz",
#                "kid": "", "autoLogin": False}
#
#     session.post("https://lobby.ogame.gameforge.com/api/users", json=payload)
#
#     json_res = session.get("https://lobby.ogame.gameforge.com/api/users/me/accounts").content
#     accounts = json.loads(json_res)
#
#     acc = list(filter(lambda x: x["name"] == account_name, accounts))[0]
#
#     params = {
#         "id": acc["id"],
#         "server[language]":  acc["server"]["language"],
#         "server[number]" : acc["server"]["number"],
#         "clickedButton": "account_list"
#     }
#
#     # https://lobby.ogame.gameforge.com/api/users/me/loginLink?id=101705&server[language]=cz&server[number]=147&clickedButton=account_list
#     resp_url = session.get("https://lobby.ogame.gameforge.com/api/users/me/loginLink", params=params).content
#     session.get(json.loads(resp_url)["url"]).content.decode("utf8")
#     return session
#

#
# if __name__ == '__main__':
#     sess = login( "odfbqorffhgijgdhxc@ttirv.org", "test123", "Lord Vela")
#     print(get_resources(sess))





from bs4 import BeautifulSoup

class FacilityList():

    def __init__(self, el):
        self._el = el

    def get_item(self, producer_name: str):
        producer_data = self._el.find("li", attrs={"class": producer_name})
        building_level = int(producer_data.find("span", attrs={"class": "level"}).attrs["data-value"])
        status = producer_data.attrs["data-status"]

        upgrade_url = None
        if status == "on":
            upgrade_url = producer_data.find("button", attrs={"class": "upgrade"}).attrs["data-target"]

        return {
            "status": status,
            "upgrade_url": upgrade_url,
            "level": building_level,
            "name": producer_name
        }

class FacilitiesPage():

    def __init__(self, content):
        self._parsed = BeautifulSoup(content, "lxml")

    def get_producers_list(self) -> FacilityList:
        return FacilityList(self._parsed.find("div", attrs={"id": "facilities"}))

from bs4 import BeautifulSoup
from player.planet.resources.resources_status import ResourcesStatus

class ResourcePage():

    def __init__(self, content):
        self._parsed = BeautifulSoup(content, "lxml")

    def get_resources(self) -> ResourcesStatus:
        resources = self._parsed.find("div", attrs={"id": "resourcesbarcomponent"})

        resource_data = {}
        resources_names = ["metal", "crystal", "deuterium", "energy"]
        for resource_name in resources_names:
            resource_raw = resources.find("span", attrs={"id": "resources_" + resource_name}).attrs["data-raw"]
            resource_count = int(float(resource_raw))
            resource_data[resource_name] = resource_count

        return ResourcesStatus(metal=resource_data["metal"], crystal=resource_data["crystal"], deuterium=resource_data["deuterium"], energy=resource_data["energy"])






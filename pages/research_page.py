from bs4 import BeautifulSoup

class ResearchList():

    def __init__(self, el):
        self._el = el

    def get_item(self, research_name):

        research_data = self._el.find("li", attrs={"class": research_name})
        research_level = int(research_data.find("span", attrs={"class": "level"}).attrs["data-value"])

        status = research_data.attrs["data-status"]
        upgrade_url = None
        if status == "on":
            upgrade_url = research_data.find("button", attrs={"class": "upgrade"}).attrs["data-target"]

        return {"name": research_name,
                "level": research_level,
                "status": status,
                "upgrade_url": upgrade_url
                }

class ResearchPage():

    def __init__(self, content):
        self._parsed = BeautifulSoup(content, "lxml")

    def get_research_list(self) -> ResearchList:
        return ResearchList(self._parsed.find("div", attrs={"id": "technologies"}))






import json


class OlxBaseParser:
    def __init__(self, soup):
        self.soup = soup
        self.initial_data = self._get_ad_data()

    def _get_ad_data(self):
        return self.get_initial_data().get("ad", {})

    def get_initial_data(self):
        tag = "script"
        options = {"id": "initial-data"}
        key = "data-json"
        return json.loads(self.soup.find(tag, options)[key])

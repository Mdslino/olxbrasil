import json


class OlxBaseParser:
    def __init__(self, soup):
        self.soup = soup
        self._initial_data = self.__get_ad_data()

    def __get_ad_data(self):
        return json.loads(
            self.soup.find("script", {"id": "initial-data"})["data-json"]
        )["ad"]

    @property
    def title(self) -> str:
        return self._initial_data["subject"].strip()

    @property
    def price(self) -> float:
        price_value = self._initial_data["priceValue"]
        price_value = price_value.replace("R$ ", "")
        return float(price_value)

    @property
    def seller(self) -> str:
        return self._initial_data["user"]["name"].strip()

    @property
    def description(self) -> str:
        return self._initial_data["description"].replace("<br>", "\n").strip()

    @property
    def phone(self) -> str:
        return self._initial_data["phone"]["phone"].strip()

    @property
    def location(self) -> dict:
        return self._initial_data["location"]

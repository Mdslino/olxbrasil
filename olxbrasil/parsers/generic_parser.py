from olxbrasil.parsers.base import OlxBaseParser
from olxbrasil.utils import format_price


class GenericItemParser(OlxBaseParser):
    @property
    def title(self) -> str:
        return self.initial_data["subject"].strip()

    @property
    def price(self) -> float:
        return format_price(self.initial_data["price"])

    @property
    def seller(self) -> str:
        return self.initial_data["user"]["name"].strip()

    @property
    def description(self) -> str:
        return self.initial_data["description"].replace("<br>", "\n").strip()

    @property
    def phone(self) -> str:
        return self.initial_data["phone"]["phone"].strip()

    @property
    def location(self) -> dict:
        return self.initial_data["location"]

from olxbrasil.parsers.base import OlxBaseParser


class GenericItemParser(OlxBaseParser):
    @property
    def title(self) -> str:
        return self.initial_data["subject"].strip()

    @property
    def price(self) -> float:
        if price_value := self.initial_data["price"]:
            price_value = price_value.replace("R$ ", "").replace('.', '').replace(',', '.')
        else:
            price_value = "0"
        return float(price_value)

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

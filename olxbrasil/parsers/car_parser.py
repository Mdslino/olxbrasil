from olxbrasil.parsers.base import OlxBaseParser


class CarParser(OlxBaseParser):
    @property
    def properties(self) -> dict:
        car_properties = {}
        for item in self._initial_data["properties"]:
            car_properties[item["name"]] = item["value"]
        return car_properties

    def is_flex(self) -> bool:
        return self.properties["fuel"].lower().strip() == "flex"

    def is_exchangeable(self) -> str:
        return self.properties["exchange"].lower().strip() == "sim"

    def is_sole_owner(self):
        return self.properties["owner"].lower().strip() == "sim"

    def is_tax_paid(self):
        return self.properties["financial"].lower().strip() == "ipva pago"

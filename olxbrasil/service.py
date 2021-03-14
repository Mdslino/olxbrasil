from typing import Optional, Any, Dict

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from httpx import Client, HTTPStatusError

from olxbrasil.constants import CATEGORIES, STATES
from olxbrasil.exceptions import OlxRequestError
from olxbrasil.parsers import ListParser, ItemParser


class Olx:
    def __init__(
        self,
        category: str,
        subcategory: Optional[str] = None,
        state: Optional[str] = "www",
    ):
        self.__subdomain = STATES.get(state, "www")
        self.__user_agent = UserAgent()
        self.__category = None
        self.__subcategory = None
        self._client = Client(
            base_url=f"https://{self.__subdomain}.olx.com.br",
            headers={"User-Agent": self.__user_agent.random},
        )

        valid_category = category in CATEGORIES.keys()

        if valid_category:
            valid_subcategory = (
                subcategory in CATEGORIES[category]["subcategories"].keys()
            )
            self.__category = CATEGORIES[category]["category"]

            if subcategory and valid_subcategory:
                sub = CATEGORIES[category]["subcategories"][subcategory]
                self.__subcategory = sub

            if subcategory and not valid_subcategory:
                raise ValueError(
                    f"{subcategory} is not a valid subcategory, please provide a valid subcategory: "
                    f"{' '.join(CATEGORIES[category].keys())}"
                )
        else:
            raise ValueError(
                f"{category} is not a valid category, please provide a valid category: "
                f"{' '.join(CATEGORIES.keys())}"
            )

    def get_all(self, page=0) -> Dict[str, Any]:
        url = f"/{self.__category}"

        if self.__subcategory:
            url += f"/{self.__subcategory}"

        if page <= 100:
            url += f"?o={page}"
        else:
            url += "?o=100"
        try:
            response = self._client.get(url)

            response.raise_for_status()
        except HTTPStatusError:
            raise OlxRequestError("Was not possible to reach OLX server")

        soup = BeautifulSoup(response.text, "html.parser")

        parser = ListParser(soup)

        return parser.items

    def get_item(self, url: str) -> ItemParser:
        response = self._client.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        parser = ItemParser(soup)
        return parser

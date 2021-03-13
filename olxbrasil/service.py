from typing import Optional, Any, Dict, List

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from httpx import Client

from olxbrasil.constants import CATEGORIES, STATES
from olxbrasil.parsers import ListParser


class Olx:
    def __init__(
        self,
        category: str,
        subcategory: Optional[str] = None,
        state: Optional[str] = "www",
    ):
        self.__subdomain = STATES.get(state, 'www')
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

    def get_all(self, page=0) -> List[Dict[str, Any]]:
        url = ""
        if self.__category:
            url += f"/{self.__category}"

            if self.__subcategory:
                url += f"/{self.__subcategory}"

        url += f"?o={page}"

        response = self._client.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        parser = ListParser(soup)

        return parser.items

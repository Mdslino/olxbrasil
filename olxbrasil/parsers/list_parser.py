import contextlib
from typing import Any, Dict, List

from olxbrasil.parsers.base import OlxBaseParser
from olxbrasil.utils import format_price


class ListParser(OlxBaseParser):
    def _get_ad_data(self):
        return self.get_initial_data()["listingProps"]["adList"]

    @property
    def items(self) -> List[Dict[str, Any]]:
        ads = []
        for item in self.initial_data:
            with contextlib.suppress(KeyError):
                title = item.get("subject", "").strip()
                price = format_price(item.get("price"))
                url = item["url"]

                ads.append(
                    {
                        "title": title,
                        "price": float(price),
                        "url": url,
                        "is_professional": item['professionalAd']
                    }
                )

        return ads

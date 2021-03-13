import contextlib
from typing import Any, Dict, List

from olxbrasil.parsers.base import OlxBaseParser


class ListParser(OlxBaseParser):
    def _get_ad_data(self):
        return self.get_initial_data()["listingProps"]["adList"]

    @property
    def items(self) -> List[Dict[str, Any]]:
        ads = []
        for item in self.initial_data:
            with contextlib.suppress(KeyError):
                title = item.get("subject", "").strip()

                if price := item.get("price"):
                    price = (
                        price.replace("R$ ", "")
                        .replace(".", "")
                        .replace(",", ".")
                    )
                else:
                    price = "0"

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

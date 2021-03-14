from typing import Optional


def format_price(price: Optional[str] = None) -> float:
    try:
        price_value = (
            price.replace("R$ ", "").replace(".", "").replace(",", ".")
        )
        return float(price_value)
    except (ValueError, AttributeError):
        return 0

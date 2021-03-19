from typing import Optional, Iterable, Any
from olxbrasil.constants import ALLOWED_BOOLEAN_FILTERS


def format_price(price: Optional[str] = None) -> float:
    try:
        price_value = (
            price.replace("R$ ", "").replace(".", "").replace(",", ".")
        )
        return float(price_value)
    except (ValueError, AttributeError):
        return 0


def build_parameters(*olx_filters: str) -> dict:
    params = {}
    for olx_filter in olx_filters:
        if olx_filter not in ALLOWED_BOOLEAN_FILTERS:
            continue

        for key, value in ALLOWED_BOOLEAN_FILTERS[olx_filter].items():
            append_parameter(params, key, value)

    return params


def append_parameter(parameters: dict, parameter: str, value: Any):
    if parameter in parameters and not isinstance(parameters[parameter], list):
        parameters[parameter] = sorted([parameters[parameter], value])
    elif parameter not in parameters:
        parameters[parameter] = value
    else:
        parameters[parameter].append(value)

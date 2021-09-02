import pytest

from olxbrasil.filters import ItemFilter, LocationFilter


@pytest.fixture(scope="session")
def item_filter() -> ItemFilter:
    return ItemFilter(
        manufacturer="ford",
        model="ecosport",
        boolean_filters=("automatic", "gasoline"),
        search_filters={"min_year": 2011, "max_year": 2022},
    )


@pytest.fixture(scope="session")
def location_filter() -> LocationFilter:
    return LocationFilter("sp", 11)

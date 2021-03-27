from olxbrasil.filters import ItemFilter


def test_item_filter_with_just_manufacturer():
    item_filter = ItemFilter(manufacturer="ford")
    assert item_filter.get_endpoint() == "/ford"
    assert item_filter.get_filters() == {}


def test_item_filter_with_manufacturer_and_model():
    item_filter = ItemFilter(manufacturer="ford", model="escort")
    assert item_filter.get_endpoint() == "/ford/escort"
    assert item_filter.get_filters() == {}


def test_item_filter_with_filters():
    item_filter = ItemFilter(
        manufacturer="ford",
        model="escort",
        boolean_filters=("automatic", "gasoline", "unknown"),
        search_filters={"min_year": 2011, "max_year": 2022, "unknown": 123},
    )
    assert item_filter.get_endpoint() == "/ford/escort"
    assert item_filter.get_filters() == {"fu": 1, "gb": 2, "re": 40, "rs": 29}

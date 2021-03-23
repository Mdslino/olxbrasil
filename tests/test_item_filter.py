from olxbrasil.filters import ItemFilter


def test_car_filter_with_just_manufacturer():
    car_filter = ItemFilter(manufacturer="ford")
    assert car_filter.get_endpoint() == "/ford"
    assert car_filter.get_filters() == {}


def test_car_filter_with_manufacturer_and_model():
    car_filter = ItemFilter(manufacturer="ford", model="escort")
    assert car_filter.get_endpoint() == "/ford/escort"
    assert car_filter.get_filters() == {}


def test_car_filter_with_filters():
    car_filter = ItemFilter(
        manufacturer="ford",
        model="escort",
        boolean_filters=("automatic", "gasoline", "unknown"),
        search_filters={"min_year": 2011, "max_year": 2022, "unknown": 123},
    )
    assert car_filter.get_endpoint() == "/ford/escort"
    assert car_filter.get_filters() == {"fu": 1, "gb": 2, "re": 40, "rs": 29}

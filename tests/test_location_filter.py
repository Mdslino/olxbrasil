import pytest

from olxbrasil.exceptions import FilterNotFoundError
from olxbrasil.filters import LocationFilter


def test_location_filter_with_wrong_state():
    with pytest.raises(FilterNotFoundError):
        LocationFilter("tt")


def test_location_filter_with_wrong_ddd():
    with pytest.raises(FilterNotFoundError):
        LocationFilter("sp", 66)


def test_location_filter_with_ddd():
    location_filter = LocationFilter("sp", 11)
    assert location_filter.state == "SP"
    assert location_filter.get_endpoint() == "sao-paulo-e-regiao"
    assert isinstance(location_filter, LocationFilter)


def test_location_filter_without_ddd():
    location_filter = LocationFilter("sp")
    assert location_filter.state == "SP"
    assert not location_filter.get_endpoint()
    assert isinstance(location_filter, LocationFilter)

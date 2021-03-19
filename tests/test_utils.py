import pytest

from olxbrasil.utils import format_price, append_parameter, build_parameters


@pytest.mark.parametrize(
    "value,expected",
    (
        ("R$ 3.800,00", 3800.00),
        ("R$ 900.000.000,65", 900000000.65),
        ("some random string", 0),
        (None, 0),
        ("123.456.789,12", 123456789.12),
    ),
)
def test_format_price(value, expected):
    assert format_price(value) == expected


@pytest.mark.parametrize(
    "params,value,expected",
    (
        ({}, ("fu", 1), {"fu": 1}),
        ({"fu": 1}, ("fu", 2), {"fu": [1, 2]}),
        ({"fu": [1, 2]}, ("fu", 3), {"fu": [1, 2, 3]}),
    ),
)
def test_append_parameter(params, value, expected):
    append_parameter(params, *value)
    assert params == expected


@pytest.mark.parametrize(
    "parameters,expected",
    (
        (("new", "private", "gasoline"), {"cond": 1, "f": "p", "fu": 1}),
        (
            ("new", "private", "gasoline", "unknown"),
            {"cond": 1, "f": "p", "fu": 1},
        ),
        (
            (
                "new",
                "old",
                "private",
                "professional",
                "gasoline",
                "alcohol",
                "flex",
                "gas",
                "diesel",
            ),
            {"cond": [1, 2], "f": ["c", "p"], "fu": [1, 2, 3, 4, 5]},
        ),
    ),
)
def test_build_parameters(parameters, expected):
    params = build_parameters(*parameters)
    assert params == expected

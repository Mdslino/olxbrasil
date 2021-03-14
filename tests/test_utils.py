import pytest

from olxbrasil.utils import format_price


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

from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from olxbrasil.parsers.base import OlxBaseParser
from olxbrasil.parsers.car_parser import CarParser
from tests import BASE_DIR


@pytest.fixture(scope="session")
def car_html() -> str:
    with open(Path(BASE_DIR.absolute(), "assets/car/hyundai.html")) as car:
        return car.read()


@pytest.fixture(scope="session")
def car_soup(car_html):
    soup = BeautifulSoup(car_html, "html.parser")
    return soup


@pytest.fixture(scope="function")
def base_parser_with_car_soup(car_soup):
    parser = OlxBaseParser(car_soup)
    return parser


@pytest.fixture(scope="function")
def car_parser(car_soup):
    parser = CarParser(car_soup)
    return parser

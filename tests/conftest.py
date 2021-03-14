from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from olxbrasil.parsers import ListParser
from olxbrasil.parsers.car_parser import CarParser
from olxbrasil.parsers.item_parser import ItemParser
from tests import BASE_DIR


@pytest.fixture(scope="session")
def states():
    return {
        "AC",
        "AL",
        "AP",
        "AM",
        "BA",
        "CE",
        "ES",
        "GO",
        "MA",
        "MT",
        "MS",
        "MG",
        "PA",
        "PB",
        "PR",
        "PE",
        "PI",
        "RJ",
        "RN",
        "RS",
        "RO",
        "RR",
        "SC",
        "SP",
        "SE",
        "TO",
        "DF",
    }


@pytest.fixture(scope="session")
def ddd_constants():
    return {
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "21",
        "22",
        "24",
        "27",
        "28",
        "31",
        "32",
        "33",
        "34",
        "35",
        "37",
        "38",
        "41",
        "42",
        "43",
        "44",
        "45",
        "46",
        "47",
        "48",
        "49",
        "51",
        "53",
        "54",
        "55",
        "61",
        "62",
        "63",
        "64",
        "65",
        "66",
        "67",
        "68",
        "69",
        "71",
        "73",
        "74",
        "75",
        "77",
        "79",
        "81",
        "82",
        "83",
        "84",
        "85",
        "86",
        "87",
        "88",
        "89",
        "91",
        "92",
        "93",
        "94",
        "95",
        "96",
        "97",
        "98",
        "99",
    }


@pytest.fixture(scope="session")
def states_names_constants():
    return {
        "Amapá",
        "Amazonas",
        "Goiás",
        "Distrito Federal/Goiás",
        "Alagoas",
        "Tocantins",
        "Roraima",
        "Pernambuco",
        "Piauí",
        "Rondônia",
        "Espírito Santo",
        "São Paulo",
        "Santa Catarina",
        "Rio Grande do Norte",
        "Mato Grosso",
        "Mato Grosso do Sul",
        "Acre",
        "Sergipe",
        "Rio de Janeiro",
        "Paraíba",
        "Bahia",
        "Pará",
        "Rio Grande do Sul",
        "Paraná",
        "Minas Gerais",
        "Maranhão",
        "Ceará",
    }


@pytest.fixture(scope="session")
def car_html() -> str:
    with open(Path(BASE_DIR.absolute(), "assets/hyundai.html")) as car:
        return car.read()


@pytest.fixture(scope="session")
def car_soup(car_html) -> BeautifulSoup:
    soup = BeautifulSoup(car_html, "html.parser")
    return soup


@pytest.fixture(scope="session")
def apartment_soup(apartment_html) -> BeautifulSoup:
    soup = BeautifulSoup(apartment_html, "html.parser")
    return soup


@pytest.fixture(scope="function")
def item_parser_with_car_soup(car_soup) -> ItemParser:
    parser = ItemParser(car_soup)
    return parser


@pytest.fixture(scope="function")
def car_parser(car_soup) -> CarParser:
    parser = CarParser(car_soup)
    return parser


@pytest.fixture(scope="session")
def list_html() -> str:
    with open(Path(BASE_DIR.absolute(), "assets/listing.html")) as listing:
        return listing.read()


@pytest.fixture(scope="session")
def list_soup(list_html) -> BeautifulSoup:
    soup = BeautifulSoup(list_html, "html.parser")
    return soup


@pytest.fixture(scope="session")
def apartment_html() -> str:
    with open(Path(BASE_DIR.absolute(), "assets/apartment.html")) as apartment:
        return apartment.read()


@pytest.fixture(scope="function")
def list_parser(list_soup) -> ListParser:
    parser = ListParser(list_soup)
    return parser

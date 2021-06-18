from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from olxbrasil.filters import ItemFilter, LocationFilter
from olxbrasil.parsers import ListParser
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

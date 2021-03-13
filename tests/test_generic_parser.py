def test_get_title(generic_parser_with_car_soup):
    assert generic_parser_with_car_soup.title == "IX35 GLS AUT 2012"


def test_get_price(generic_parser_with_car_soup):
    assert generic_parser_with_car_soup.price == 65999.0


def test_get_seller(generic_parser_with_car_soup):
    assert generic_parser_with_car_soup.seller == "Alexandre"


def test_get_description(generic_parser_with_car_soup):
    assert (
            generic_parser_with_car_soup.description
            == """?IX35 TOP DE LINHA ?
? TETO SOLAR ,CAMBIO AUT?
?BANCOS EM COURO?
?FAROIS DE MILHA ,RODAS DE LIGA?"""
    )


def test_get_phone(generic_parser_with_car_soup):
    assert generic_parser_with_car_soup.phone == ""


def test_get_location(generic_parser_with_car_soup):
    assert generic_parser_with_car_soup.location == {
        "address": None,
        "neighbourhood": "Pilar Velho",
        "neighbourhoodId": 11157,
        "municipality": "Ribeirão Pires",
        "municipalityId": 3336,
        "zipcode": "09404590",
        "mapLati": 0,
        "mapLong": 0,
        "uf": "SP",
        "ddd": "11",
        "zoneId": 2939,
        "zone": "outras-cidades",
        "region": "São Paulo e região, SP",
    }

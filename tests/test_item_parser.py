def test_get_title(item_parser_with_car_soup):
    assert item_parser_with_car_soup.title == "IX35 GLS AUT 2012"


def test_get_price(item_parser_with_car_soup):
    assert item_parser_with_car_soup.price == 65999.0


def test_get_seller(item_parser_with_car_soup):
    assert item_parser_with_car_soup.seller == "Alexandre"


def test_get_description(item_parser_with_car_soup):
    assert (
        item_parser_with_car_soup.description
        == """?IX35 TOP DE LINHA ?
? TETO SOLAR ,CAMBIO AUT?
?BANCOS EM COURO?
?FAROIS DE MILHA ,RODAS DE LIGA?"""
    )


def test_get_phone(item_parser_with_car_soup):
    assert item_parser_with_car_soup.phone == ""


def test_get_location(item_parser_with_car_soup):
    assert item_parser_with_car_soup.location == {
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


def test_dict_transformation(item_parser_with_car_soup):
    parser_dictionary = dict(item_parser_with_car_soup)
    assert isinstance(parser_dictionary, dict)
    assert parser_dictionary == {
        "description": "?IX35 TOP DE LINHA ?\n? TETO SOLAR ,CAMBIO AUT?\n?BANCOS EM COURO?\n?FAROIS DE "
        "MILHA ,RODAS DE LIGA?",
        "location": {
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
        },
        "phone": "",
        "price": 65999.0,
        "properties": {
            "category": "Carros, vans e utilitários",
            "vehicle_model": "HYUNDAI 2.0 MPFI GLS 16V FLEX 4P AUTOMATICO",
            "vehicle_brand": "HYUNDAI",
            "cartype": "SUV",
            "regdate": "2012",
            "mileage": "110000",
            "motorpower": "2.0 - 2.9",
            "fuel": "Flex",
            "gearbox": "Automático",
            "car_steering": "Hidráulica",
            "carcolor": "Preto",
            "doors": "4 portas",
            "end_tag": "4",
            "owner": "Sim",
            "exchange": "Sim",
            "financial": "IPVA Pago",
            "car_features": "Vidro elétrico, Air bag, Trava elétrica, Ar condicionado, Direção hidráulica, "
            "Alarme, Som, Sensor de ré, Câmera de ré",
        },
        "seller": "Alexandre",
        "title": "IX35 GLS AUT 2012",
    }


def test_dict_get_item(item_parser_with_car_soup):
    assert item_parser_with_car_soup["title"] == "IX35 GLS AUT 2012"
    assert item_parser_with_car_soup["unknown"] is None

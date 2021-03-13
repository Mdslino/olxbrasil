def test_car_parser_get_properties(car_parser):
    assert car_parser.properties == {
        "car_features": "Vidro elétrico, Air bag, Trava elétrica, Ar condicionado, "
        "Direção hidráulica, Alarme, Som, Sensor de ré, Câmera de ré",
        "car_steering": "Hidráulica",
        "carcolor": "Preto",
        "cartype": "SUV",
        "category": "Carros, vans e utilitários",
        "doors": "4 portas",
        "end_tag": "4",
        "exchange": "Sim",
        "financial": "IPVA Pago",
        "fuel": "Flex",
        "gearbox": "Automático",
        "mileage": "110000",
        "motorpower": "2.0 - 2.9",
        "owner": "Sim",
        "regdate": "2012",
        "vehicle_brand": "HYUNDAI",
        "vehicle_model": "HYUNDAI 2.0 MPFI GLS 16V FLEX 4P AUTOMATICO",
    }


def test_car_parser_check_questions(car_parser):
    assert car_parser.is_flex()
    assert car_parser.is_exchangeable()
    assert car_parser.is_tax_paid()
    assert car_parser.is_sole_owner()

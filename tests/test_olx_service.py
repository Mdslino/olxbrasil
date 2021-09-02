import pytest
import respx
from httpx import ConnectError, Response

from olxbrasil.constants import CATEGORIES
from olxbrasil.exceptions import OlxRequestError
from olxbrasil.parsers import ItemParser
from olxbrasil.service import Olx


def test_olx_service_instance():
    service = Olx(category="cars")
    assert isinstance(service, Olx)


def test_olx_service_instance_error_with_invalid_category():
    with pytest.raises(ValueError):
        Olx(category="invalid")


@pytest.mark.vcr()
def test_olx_service_fetch_all_ids_without_sub_category():
    category = "cars"
    service = Olx(category=category)
    assert service.fetch_all()


@pytest.mark.vcr()
def test_olx_service_fetch_all_ids_with_invalid_page():
    category = "cars"
    service = Olx(category=category)
    assert service.fetch_all(101)


@pytest.mark.vcr()
def test_olx_service_fetch_all_ids_with_sub_category(item_filter):
    category = "cars"
    subcategory = "cars"
    service = Olx(
        category=category,
        subcategory=subcategory,
        filters=item_filter,
    )
    assert service.fetch_all()


@pytest.mark.vcr()
def test_olx_service_fetch_all_ids_with_sub_category_and_location(
    item_filter, location_filter
):
    category = "cars"
    subcategory = "cars"
    service = Olx(
        category=category,
        subcategory=subcategory,
        filters=item_filter,
        location=location_filter,
    )
    assert service.fetch_all()


def test_olx_service_fetch_all_ids_with_invalid_sub_category():
    category = "cars"
    subcategory = "invalid"
    with pytest.raises(ValueError):
        Olx(category=category, subcategory=subcategory)


@respx.mock
def test_olx_service_request_error():
    category = "cars"
    service = Olx(category=category)
    url = f"https://www.olx.com.br/{CATEGORIES[category]['category']}"
    route = respx.get(url)
    route.return_value = Response(500)
    with pytest.raises(OlxRequestError):
        service.fetch_all()


@pytest.mark.vcr()
def test_olx_service_get_item(item_filter, location_filter):
    category = "cars"
    service = Olx(
        category=category, filters=item_filter, location=location_filter
    )
    url = (
        "https://sp.olx.com.br/regiao-de-sorocaba/imoveis/apartamento-com-2"
        "-dormitorios-a-venda-52-m-por"
        "-r-279-000-00-bairro-da-vossoroca-sor-814717433"
    )
    assert isinstance(service.fetch_item(url), ItemParser)


@respx.mock
def test_olx_service_get_item_with_http_error(item_filter, location_filter):
    category = "cars"
    service = Olx(
        category=category, filters=item_filter, location=location_filter
    )
    url = (
        "https://sp.olx.com.br/regiao-de-sorocaba/imoveis/apartamento-com-2"
        "-dormitorios-a-venda-52-m-por"
        "-r-279-000-00-bairro-da-vossoroca-sor-814717433"
    )
    route = respx.get(url)
    route.return_value = Response(500)
    with pytest.raises(OlxRequestError):
        service.fetch_item(url)


@respx.mock
def test_olx_service_get_item_with_connect_error(item_filter, location_filter):
    category = "cars"
    service = Olx(
        category=category, filters=item_filter, location=location_filter
    )
    url = (
        "https://sp.olx.com.br/regiao-de-sorocaba/imoveis/apartamento-com"
        "-2-dormitorios-a-venda-52-m-por-r-279-000-00-bairro-da-vossoroca"
        "-sor-814717433"
    )
    route = respx.get(url).mock(side_effect=ConnectError)
    route.return_value = Response(500)
    with pytest.raises(OlxRequestError):
        service.fetch_item(url)

import pytest
import respx
from httpx import Response

from olxbrasil.constants import CATEGORIES
from olxbrasil.exceptions import OlxRequestError
from olxbrasil.parsers import ItemParser
from olxbrasil.service import Olx
from tests.data import list_data


def test_olx_service_instance():
    service = Olx(category="cars")
    assert isinstance(service, Olx)


def test_olx_service_instance_error_with_invalid_category():
    with pytest.raises(ValueError):
        Olx(category="invalid")


@respx.mock
def test_olx_service_get_all_ids_without_sub_category(list_html):
    category = "cars"
    service = Olx(category=category)
    url = f"https://www.olx.com.br/{CATEGORIES[category]['category']}"
    route = respx.get(url)
    route.return_value = Response(200, html=list_html)
    assert service.get_all() == list_data
    assert route.called


@respx.mock
def test_olx_service_get_all_ids_with_invalid_page(list_html):
    category = "cars"
    service = Olx(category=category)
    url = f"https://www.olx.com.br/{CATEGORIES[category]['category']}"
    route = respx.get(url)
    route.return_value = Response(200, html=list_html)
    assert service.get_all(101) == list_data
    assert route.called


@respx.mock
def test_olx_service_get_all_ids_with_sub_category(list_html, item_filter):
    category = "cars"
    subcategory = "parts"
    service = Olx(
        category=category, subcategory=subcategory, filters=item_filter
    )
    url = (
        f"https://www.olx.com.br/{CATEGORIES[category]['category']}/"
        f"{CATEGORIES[category]['subcategories'][subcategory]}"
    )
    url += item_filter.get_endpoint()
    route = respx.get(url, params=item_filter.get_filters())
    route.return_value = Response(200, html=list_html)
    assert service.get_all() == list_data
    assert route.called


def test_olx_service_get_all_ids_with_invalid_sub_category(list_html):
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
        service.get_all()


@respx.mock
def test_olx_service_get_item(apartment_html, item_filter):
    category = "cars"
    service = Olx(category=category, filters=item_filter)
    url = (
        "https://sp.olx.com.br/regiao-de-sorocaba/imoveis/apartamento-com-2-dormitorios-a-venda-52-m-por"
        "-r-279-000-00-bairro-da-vossoroca-sor-814717433"
    )
    route = respx.get(url)
    route.return_value = Response(200, html=apartment_html)
    assert isinstance(service.get_item(url), ItemParser)

import pytest
import respx
from httpx import Response, ConnectError

from olxbrasil import AsyncOlx
from olxbrasil.constants import CATEGORIES
from olxbrasil.exceptions import OlxRequestError
from olxbrasil.parsers import ItemParser
from tests.data import list_data


@pytest.mark.asyncio
async def test_async_olx_service_instance():
    service = AsyncOlx(category="cars")
    assert isinstance(service, AsyncOlx)


@pytest.mark.asyncio
async def test_async_olx_service_instance_error_with_invalid_category():
    with pytest.raises(ValueError):
        AsyncOlx(category="invalid")


@respx.mock
@pytest.mark.asyncio
async def test_async_olx_service_get_all_ids_without_sub_category(list_html):
    category = "cars"
    service = AsyncOlx(category=category)
    url = f"https://www.olx.com.br/{CATEGORIES[category]['category']}"
    route = respx.get(url)
    route.return_value = Response(200, html=list_html)
    result = await service.fetch_all()
    assert result == list_data
    assert route.called


@respx.mock
@pytest.mark.asyncio
async def test_async_olx_service_get_all_ids_with_invalid_page(list_html):
    category = "cars"
    service = AsyncOlx(category=category)
    url = f"https://www.olx.com.br/{CATEGORIES[category]['category']}"
    route = respx.get(url)
    route.return_value = Response(200, html=list_html)
    result = await service.fetch_all(101)
    assert result == list_data
    assert route.called


@respx.mock
@pytest.mark.asyncio
async def test_async_olx_service_get_all_ids_with_sub_category(
    list_html, item_filter
):
    category = "cars"
    subcategory = "cars"
    service = AsyncOlx(
        category=category,
        subcategory=subcategory,
        filters=item_filter,
    )
    url = (
        f"https://www.olx.com.br/{CATEGORIES[category]['category']}/"
        f"{CATEGORIES[category]['subcategories'][subcategory]}"
    )
    url += item_filter.get_endpoint()
    route = respx.get(url, params=item_filter.get_filters())
    route.return_value = Response(200, html=list_html)
    result = await service.fetch_all()
    assert result == list_data
    assert route.called


@pytest.mark.asyncio
async def test_async_olx_service_get_all_ids_with_invalid_sub_category(
    list_html,
):
    category = "cars"
    subcategory = "invalid"
    with pytest.raises(ValueError):
        AsyncOlx(category=category, subcategory=subcategory)


@pytest.mark.asyncio
@respx.mock
async def test_async_olx_service_request_error():
    category = "cars"
    service = AsyncOlx(category=category)
    url = f"https://www.olx.com.br/{CATEGORIES[category]['category']}"
    route = respx.get(url)
    route.return_value = Response(500)
    with pytest.raises(OlxRequestError):
        await service.fetch_all()


@respx.mock
@pytest.mark.asyncio
async def test_async_olx_service_get_item(
    apartment_html, item_filter, location_filter
):
    category = "cars"
    service = AsyncOlx(
        category=category, filters=item_filter, location=location_filter
    )
    url = (
        "https://sp.olx.com.br/regiao-de-sorocaba/imoveis/apartamento-com-2-dormitorios-a-venda-52-m-por"
        "-r-279-000-00-bairro-da-vossoroca-sor-814717433"
    )
    route = respx.get(url)
    route.return_value = Response(200, html=apartment_html)
    result = await service.fetch_item(url)
    assert isinstance(result, ItemParser)


@respx.mock
@pytest.mark.asyncio
async def test_async_olx_service_get_item_with_http_error(
    apartment_html, item_filter, location_filter
):
    category = "cars"
    service = AsyncOlx(
        category=category, filters=item_filter, location=location_filter
    )
    url = (
        "https://sp.olx.com.br/regiao-de-sorocaba/imoveis/apartamento-com-2-dormitorios-a-venda-52-m-por"
        "-r-279-000-00-bairro-da-vossoroca-sor-814717433"
    )
    route = respx.get(url)
    route.return_value = Response(500)
    with pytest.raises(OlxRequestError):
        await service.fetch_item(url)


@respx.mock
@pytest.mark.asyncio
async def test_async_olx_service_get_item_with_connect_error(
    apartment_html, item_filter, location_filter
):
    category = "cars"
    service = AsyncOlx(
        category=category, filters=item_filter, location=location_filter
    )
    url = (
        "https://sp.olx.com.br/regiao-de-sorocaba/imoveis/apartamento-com-2-dormitorios-a-venda-52-m-por"
        "-r-279-000-00-bairro-da-vossoroca-sor-814717433"
    )
    route = respx.get(url).mock(side_effect=ConnectError)
    route.return_value = Response(500)
    with pytest.raises(OlxRequestError):
        await service.fetch_item(url)

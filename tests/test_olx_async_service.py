import pytest
import respx
from httpx import ConnectError, Response

from olxbrasil import AsyncOlx
from olxbrasil.constants import CATEGORIES
from olxbrasil.exceptions import OlxRequestError
from olxbrasil.parsers import ItemParser

pytestmark = pytest.mark.asyncio


async def test_async_olx_service_instance():
    service = AsyncOlx(category="cars")
    assert isinstance(service, AsyncOlx)


async def test_async_olx_service_instance_error_with_invalid_category():
    with pytest.raises(ValueError):
        AsyncOlx(category="invalid")


@pytest.mark.vcr()
async def test_async_olx_service_get_all_ids_without_sub_category():
    category = "cars"
    service = AsyncOlx(category=category)
    result = await service.fetch_all()
    assert result


@pytest.mark.vcr()
async def test_async_olx_service_get_all_ids_with_invalid_page():
    category = "cars"
    service = AsyncOlx(category=category)
    result = await service.fetch_all(101)
    assert result


@pytest.mark.vcr()
async def test_async_olx_service_get_all_ids_with_sub_category(item_filter):
    category = "cars"
    subcategory = "cars"
    service = AsyncOlx(
        category=category,
        subcategory=subcategory,
        filters=item_filter,
    )
    result = await service.fetch_all()
    assert result


async def test_async_olx_service_get_all_ids_with_invalid_sub_category():
    category = "cars"
    subcategory = "invalid"
    with pytest.raises(ValueError):
        AsyncOlx(category=category, subcategory=subcategory)


@respx.mock
async def test_async_olx_service_request_error():
    category = "cars"
    service = AsyncOlx(category=category)
    url = f"https://www.olx.com.br/{CATEGORIES[category]['category']}"
    route = respx.get(url)
    route.return_value = Response(500)
    with pytest.raises(OlxRequestError):
        await service.fetch_all()


@pytest.mark.vcr()
async def test_async_olx_service_get_item(item_filter, location_filter):
    category = "cars"
    service = AsyncOlx(
        category=category, filters=item_filter, location=location_filter
    )
    url = (
        "https://sp.olx.com.br/regiao-de-sorocaba/imoveis/apartamento-com-2"
        "-dormitorios-a-venda-52-m-por"
        "-r-279-000-00-bairro-da-vossoroca-sor-814717433"
    )
    result = await service.fetch_item(url)
    assert isinstance(result, ItemParser)


@respx.mock
async def test_async_olx_service_get_item_with_http_error(
    item_filter, location_filter
):
    category = "cars"
    service = AsyncOlx(
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
        await service.fetch_item(url)


@respx.mock
async def test_async_olx_service_get_item_with_connect_error(
    item_filter, location_filter
):
    category = "cars"
    service = AsyncOlx(
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
        await service.fetch_item(url)

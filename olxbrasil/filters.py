import abc
from typing import Optional, Iterable, Dict

from olxbrasil.utils import build_boolean_parameters, build_search_parameters


class Filter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_filters(self, params: Optional[Dict] = None) -> str:
        ...  # pragma: nocover

    @abc.abstractmethod
    def get_endpoint(self) -> str:
        ...  # pragma: nocover


class CarFilter(Filter):
    def __init__(
        self,
        *,
        manufacturer: Optional[str] = None,
        model: Optional[str] = None,
        boolean_filters: Optional[Iterable] = tuple(),
        search_filters: Optional[Dict] = None,
    ):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__boolean_filters = boolean_filters
        self.__search_filters = search_filters

    def get_filters(self, params: Optional[Dict] = None):
        car_filters = params or {}
        if self.__boolean_filters:
            car_filters.update(
                build_boolean_parameters(*self.__boolean_filters)
            )
        if self.__search_filters:
            car_filters.update(
                build_search_parameters(**self.__search_filters)
            )

        return car_filters

    def get_endpoint(self) -> str:
        endpoint = ""

        if self.__manufacturer:
            endpoint += f"/{self.__manufacturer}"
            if self.__model:
                endpoint += f"/{self.__model}"

        return endpoint

import hashlib
from typing import Any, ClassVar
import datetime as dt

from requests import get

from api_marvel.exceptions import _check_response
from constans import PRI_KEY, API_MARVEL_HOST, PUB_KEY

client_version = 3.10


def hash_key(ts: int) -> str:
    return hashlib.md5(f"{ts}{PRI_KEY}{PUB_KEY}".encode()).hexdigest()


def headers() -> dict:
    return {
        "Content-Type": "application/json; charset=utf-8",
        "Date": f"{dt.datetime.now() + dt.timedelta(hours=9):'%a, %d %b %Y %X GMT'}"
    }


class APICharacterSearch:
    """ Conexión a API /v1/public/characters """

    _endpoint: ClassVar[str] = f"{API_MARVEL_HOST}/v1/public/characters"
    _client_version: ClassVar[float] = client_version

    def __init__(self, **kwargs):
        self.name_starts_with = kwargs.get("nameStartsWith", 'None')
        self.name = kwargs.get("name", 'None')
        self.query_params = {key: value for key, value in self._params.items() if value != 'None'}
        self.response = self._get

    @property
    def _params(self) -> dict:
        return {
            "name": self.name,
            "nameStartsWith": self.name_starts_with,
            "orderBy": "name",
            "apikey": PUB_KEY,
            "hash": hash_key(1),
            "ts": 1,
        }

    @property
    def _get(self) -> dict[str, Any]:
        return self._request(url=self._endpoint, params=self.query_params, headers=headers())

    @staticmethod
    def get_appearance(appearances: str, row: dict) -> int:
        try:
            returned = row.get(appearances).get("returned")
            if returned:
                return returned
        except Exception as e:
            return 0
        else:
            return 0

    def result(self, row: dict) -> dict:
        return {
            "id": row.get("id"),
            "name": row.get("name"),
            "image": row.get("thumbnail").get("path"),
            "appearances": sum([self.get_appearance(k, row) for k in row.keys()]),
        }

    def _request(self, **kwargs) -> dict | list:
        response = get(**kwargs)
        _check_response(response)
        return [self.result(row) for row in response.json().get("data").get("results")]

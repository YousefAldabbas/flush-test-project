from requests import request
from enum import Enum
from fastapi.encoders import jsonable_encoder


class ServicesEnum(int, Enum):
    test_1 = 1
    test_2 = 2


SERVICE_1_URL = "http://127.0.0.1:8000/"
SERVICE_2_URL = "http://127.0.0.1:8001/"


class Broker:
    def __init__(self, service: ServicesEnum) -> None:
        self.service = service

    def create(self, data: dict):
        url = SERVICE_1_URL if self.service == 1 else SERVICE_2_URL

        response = request("POST", url, json=jsonable_encoder(data))

        return response.json()

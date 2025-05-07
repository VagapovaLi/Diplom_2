import pytest
from copy import deepcopy as dc
from data.data import RequestUserData
from helper import Helper
from api_client import ApiClient

from urls import URL_USER_CREATE, URL_USER_LOGIN


@pytest.fixture
def create_user():

    user_data = dc(RequestUserData.payload)

    for key in user_data.keys():
        if key == 'email':
            user_data[key] = Helper.generate_random_string(RequestUserData.LENTH_KEYS_USER) + '@yandex.ru'
            continue
        user_data[key] = Helper.generate_random_string(RequestUserData.LENTH_KEYS_USER)

    response = ApiClient.post(url=URL_USER_CREATE, data=user_data)

    yield response

    ApiClient.delete(url=URL_USER_LOGIN, headers={'Authorization': f'{response.json()["accessToken"]}'})


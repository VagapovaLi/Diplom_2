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

    # response = requests.post(Urls.URL_USER_CREATE, json=user_data_login_password)
    #
    # yield response



# @pytest.fixture
#     # Генерирует данные пользователя со случайным логином, паролем и именем.
# def user_data_login_password():
#
#         user_data= helper.UserDataGenerator()
#         return user_data.generate_random_data_user()


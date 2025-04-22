import pytest
import requests
import helper
from urls import Urls


@pytest.fixture
def create_user(user_data_login_password):
    response = requests.post(Urls.URL_USER_CREATE, json=user_data_login_password)

    yield response


@pytest.fixture
    # Генерирует данные пользователя со случайным логином, паролем и именем.
def user_data_login_password():

        user_data= helper.UserDataGenerator()
        return user_data.generate_random_data_user()
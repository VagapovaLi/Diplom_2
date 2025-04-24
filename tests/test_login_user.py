import allure
import pytest
import requests
from data import Response
import json
from urls import Urls


@allure.story('Сценарии авторизации пользователя')
class TestCreateUser:
    @allure.title('авторизации пользователя с валидными данными.Ожидаемый результат: 200')
    def test_login_user_expected_answer_200(self, create_user):
        response_user = create_user
        user_data = json.loads(response_user.request.body)
        login_response = requests.post(Urls.URL_USER_LOGIN, json=user_data)

        assert login_response.status_code == 200 and login_response.json()['user']['email'] == user_data['email']



    @allure.title('Авторизации пользователя с неверным логином и паролем.Ожидаемый результат: 401')
    @pytest.mark.parametrize('key', ['email', 'password'])


    def test_login_user_with_invalid_credentials_expected_answer_401(self,create_user, key):
        response_user = create_user
        user_data = json.loads(response_user.request.body)
        payload = {
            'email': user_data["email"],
            'password': user_data["password"]
        }
        payload[key] = payload.get(key) + '!'

        login_response = requests.post(Urls.URL_USER_LOGIN, data=payload)
        assert login_response.status_code == 401  and login_response.json() == Response.RESPONSE_INCORRECT_DATA





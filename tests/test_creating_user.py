import allure
import pytest
import requests
from data import Response
from helper import StringGenerator
import json
from urls import Urls


@allure.story('Сценарии создания пользователя')
class TestCreateUser:
    @allure.title('Создание нового пользователя с валидными данными.Ожидаемый результат: 200')
    def test_create_new_user_success_answer_403(self, create_user):
        response = create_user

        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Создание пользователя который уже зарегистрирован:  403')
    def test_create_user_already_registered(self,create_user):
        response_user = create_user
        user_data = json.loads(response_user.request.body)
        duplicate_response = requests.post(Urls.URL_user_create, json=user_data)

        assert duplicate_response.status_code == 403 and duplicate_response.json() == Response.RESPONSE_USER_EXISTS

    @allure.title('Создание пользователя  без одного из полей:  403')
    @pytest.mark.parametrize('field', ['email', 'name', 'password'])
    def test_create_user_without_one_fields(self,create_user,field):

        payload = {
            "email": StringGenerator.generate_random_string(10) + '@yandex.ru',
            "password": StringGenerator.generate_random_string(10),
            "name": StringGenerator.generate_random_string(10)
        }

        payload.pop(field)
        response = requests.post(Urls.URL_user_create, data=payload)
        assert response.status_code == 403 and response.json() == Response.RESPONSE_INCOMPLETE_DATA
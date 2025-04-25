import allure
import pytest
import requests
from tests.helper import StringGenerator
from urls import Urls
from data import Response

@allure.story('Сценарии изменений данных пользователя')
class TestUpdatesUser:
    @allure.title('Изменение данных пользователя с авторизацией.Ожидаемый результат: 200')
    @pytest.mark.parametrize('key', ['email', 'name'])
    def test_update_user_data_with_auth_expected_answer_200(self, create_user, key):

        token = create_user.json().get('accessToken')
        payload = {'email': create_user.json()['user']['email'],
                   'name': create_user.json()['user']['name'],
                   key: StringGenerator.generate_random_string(10) if key == 'name'
                   else StringGenerator.generate_random_string(10) + '@yandex.ru'}


        response_update_user = requests.patch(Urls.URL_UPDATE_USERS, headers={'Authorization': f'{token}'},
                                               json=payload)

        assert response_update_user.status_code == 200
        assert  response_update_user.json()['user'][key] == payload[key]

    @allure.title('Изменение данных пользователя без авторизации.Ожидаемый результат: 401')

    def test_update_user_data_without_auth_expected_answer_401(self, create_user):

        response_update_user = requests.patch(Urls.URL_UPDATE_USERS,
                                              data = {'email': 'test' + create_user.json()['user']['email'],
                   'name': 'test' + create_user.json()['user']['name']})

        assert response_update_user.status_code == 401 and response_update_user.json() == Response.RESPONSE_NOT_AUTHORIZED






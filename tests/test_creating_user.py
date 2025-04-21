import allure
import pytest
import requests
#from data import Response
from urls import Urls



@allure.story('Сценарии создания пользователя')
class TestCreateUser:
    @allure.title('Создание пользователя с валидными данными.Ожидаемый результат: 201')
    def test_create_user_success_answer_403(self, create_user):
        response = create_user
        assert response.status_code == 403
import allure
import pytest
import requests
from data import RequestOrderData
from helper import StringGenerator
import json
from urls import Urls

@allure.story('Сценарии создания заказа')
class TestOrdersCreation:

    @allure.title('Создание заказа с ингредиентами под авторизованным пользователем.Ожидаемый результат: 200')
    def test_create_order_authorized_user_expected_answer_200(self, create_user):
        token = create_user.json().get('accessToken')
        payload =RequestOrderData.payload
        response = requests.post(Urls.URL_ORDER_CREATION, headers={'Authorization': token}, data=payload )

        assert response.status_code == 200 and response.json().get("success") is True


    @allure.title('Создание заказа с ингредиентами без авторизации пользователя.Ожидаемый результат: 200')
    def test_create_order_authorized_user_expected_answer_200(self):
        payload =RequestOrderData.payload
        response = requests.post(Urls.URL_ORDER_CREATION,  data=payload )

        assert response.status_code == 200 and response.json().get("success") is True


    @allure.title('Создание заказа без ингередиентов.Ожидаемый результат: 400')
    def test_create_order_without_ingredients_expected_answer_400(self, create_user):
        token = create_user.json().get('accessToken')
        payload = []

        response = requests.post(Urls.URL_ORDER_CREATION, headers={'Authorization': token}, data=payload)
        assert response.status_code == 400
        print(response.status_code)


    @allure.title('Создание заказа с невалидным хеш ингредиента.Ожидаемый результат: 500')
    def test_create_order_with_invalid_ingredient_hash_expected_answer_500(self, create_user):
        token = create_user.json().get('accessToken')
        payload = {
        "ingredients": ['61c0c5a71d1f82001_incorrect']
    }
        response = requests.post(Urls.URL_ORDER_CREATION, headers={'Authorization': token}, data=payload)
        assert response.status_code == 500
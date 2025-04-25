import allure
import requests
from data import RequestOrderData, Response
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


    @allure.title('Создание заказа с невалидным хеш ингредиента.Ожидаемый результат: 500')
    def test_create_order_with_invalid_ingredient_hash_expected_answer_500(self, create_user):
        token = create_user.json().get('accessToken')
        payload = {
        "ingredients": ['61c0c5a71d1f82001_incorrect']
    }
        response = requests.post(Urls.URL_ORDER_CREATION, headers={'Authorization': token}, data=payload)
        assert response.status_code == 500


    @allure.title('Получение заказа авторизованного пользователя.Ожидаемый результат: 200')
    def test_receiving_order_authorized_user_expected_answer_200(self, create_user):
        token = create_user.json().get('accessToken')
        payload =RequestOrderData.payload
        requests.post(Urls.URL_ORDER_CREATION, headers={'Authorization': token}, data=payload )
        response_order = requests.get(Urls.URL_RECEIVING_ORDER, headers={'Authorization': token})

        assert response_order.status_code == 200
        assert len(response_order.json()['orders']) == 1
        assert  response_order.json()['orders'][0]['ingredients']== (payload['ingredients'])

    @allure.title('Получение заказа пользователя без авторизации.Ожидаемый результат: 401')
    def test_receiving_order_without_authorization_user_expected_answer_200(self):
        response_order = requests.get(Urls.URL_RECEIVING_ORDER)
        assert response_order.status_code == 401 and response_order.json() == Response.RESPONSE_NOT_AUTHORIZED


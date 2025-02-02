import allure

from api_client import ApiClient
from conftetst import create_user, api
from data import ResponseData


@allure.suite("Получение заказов конкретного пользователя")
class TestGetUserOrder:

    @allure.title("Получение номера заказа зарегистрированного пользователя")
    def test_get_user_order_auth(self, create_user):
        ingredients = ApiClient.receive_ingredients().json()
        ingredient_0 = ingredients['data'][0]['_id']
        order = {"ingredients": [ingredient_0]}
        response_create_user = create_user[0]
        token = response_create_user.json()["accessToken"]
        response_create_order = ApiClient.create_orders(token, order)
        response_get_order = ApiClient.get_user_orders(token)
        response_data = response_get_order.json()
        assert response_get_order.status_code == 200 and response_data['success'] is True
        assert response_data['orders'][0]['number'] == response_create_order.json()['order']['number']

    @allure.title("Получение заказов незарегистрированным пользователем")
    def test_get_user_order_without_auth(self):
        token = ''
        response_get_order = ApiClient.get_user_orders(token)
        response_data = response_get_order.json()
        assert response_get_order.status_code == 401
        assert response_data["success"] is False
        assert response_data["message"] == ResponseData.AUTHORIZATION_ERROR_MESSAGE

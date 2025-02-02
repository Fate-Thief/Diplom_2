import allure
from conftetst import create_user, api

from api_client import ApiClient
from data import ResponseData


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа под зарегистрированным пользователем")
    def test_create_order_auth(self, create_user):
        ingredients = ApiClient.receive_ingredients().json()
        ingredient_0 = ingredients['data'][0]['_id']
        order = {"ingredients": [ingredient_0]}
        response_create_user = create_user[0]
        token = response_create_user.json()["accessToken"]
        response_create_order = ApiClient.create_orders(token, order)
        response_data = response_create_order.json()
        assert response_create_order.status_code == 200 and response_data['success'] is True
        assert response_data['order']['number'] is not None and response_data['order']['number'] != 0

    @allure.title("Создание заказа c ингредиентом c неверным хешем ")
    def test_create_order_invalid_hash_ingredients(self, create_user):
        ingredient = {"ingredients": ["000xxx000"]}
        response_create_user = create_user[0]
        token = response_create_user.json()["accessToken"]
        response_create_order = ApiClient.create_orders(token, ingredient)
        assert response_create_order.status_code == 500
        assert response_create_order.reason == ResponseData.INTERNAL_SERVER_ERROR_MESSAGE

    @allure.title("Создание заказа не зарегистрированным пользователем")
    def test_create_order_without_auth(self):
        token = ''
        ingredients = ApiClient.receive_ingredients().json()
        ingredient_0 = ingredients['data'][0]['_id']
        order = {"ingredients": [ingredient_0]}
        response_create_order = ApiClient.create_orders(token, order)
        response_data = response_create_order.json()
        # В документации написано "Только авторизованные пользователи могут делать заказы.", но на тестовом стенде можно, поэтому тест падает
        assert response_create_order.status_code == 401 and response_data['success'] is False
        assert response_data['message'] == ResponseData.AUTHORIZATION_ERROR_MESSAGE

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_not_ingredients(self, create_user):
        ingredient = {"ingredients": [""]}
        response_create_user = create_user[0]
        token = response_create_user.json()["accessToken"]
        response_create_order = ApiClient.create_orders(token, ingredient)
        response_data = response_create_order.json()
        assert response_create_order.status_code == 400 and response_data["success"] is False
        assert response_data["message"] == ResponseData.MISSING_INGREDIENT_MESSAGE

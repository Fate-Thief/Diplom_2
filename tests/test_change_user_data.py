import allure

from conftetst import create_user, api
from api_client import ApiClient
from helpers import new_user_body


@allure.suite("Изменение данных пользователя")
class TestUpdateDataUser:

    @allure.title("Изменение данных пользователя c авторизацией")
    def test_update_data_user_auth(self, create_user):
        response_create_user = create_user[0]
        token = response_create_user.json()["accessToken"]
        user_data = new_user_body()
        response = ApiClient.update_user_data(token, user_data)
        response_data = response.json()
        assert response.status_code == 200 and response_data['success'] is True
        assert response_data['user']['name'] == user_data['name']
        assert response_data['user']['email'] == user_data['email']

    @allure.title("Изменение данных без авторизации")
    def test_update_user_without_auth(self, create_user):
        token = ''
        user_data = new_user_body()
        response = ApiClient.update_user_data(token, user_data)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data["success"] is False
        assert response_data["message"] == "You should be authorised"

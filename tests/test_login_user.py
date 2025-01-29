import allure
from conftetst import create_user, api
from api_client import ApiClient


@allure.suite("Создание пользователя")
class TestLoginUser:
    @allure.title("Тест на создание уникального пользователя")
    def test_login_user(self, create_user):
        response_create_user_body = create_user[1]
        response = ApiClient.login_user(response_create_user_body)
        response_data = response.json()
        assert response.status_code == 200 and response_data['success'] is True
        assert response_data['accessToken']
        assert response_data['refreshToken']
        assert response_data['user']['name'] == create_user[1]["name"]
        assert response_data['user']['email'] == create_user[1]['email']

    @allure.title("Тест на создание уникального пользователя")
    def test_login_user_incorrect_data(self, create_user):
        response_create_user_body = create_user[1]
        # Замена пароля на не верный
        response_create_user_body["password"] = response_create_user_body["password"] + "a"
        response = ApiClient.login_user(response_create_user_body)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data["success"] is False
        assert response_data["message"] == "email or password are incorrect"

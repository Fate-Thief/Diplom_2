import allure
import pytest

from conftetst import create_user, api
from api_client import ApiClient
from data import ResponseData


@allure.suite("Создание пользователя")
class TestCreateUser:
    @allure.title("Тест на создание уникального пользователя")
    def test_create_unique_user(self, create_user):
        response = create_user[0]
        response_data = response.json()
        assert response.status_code == 200 and response_data['success'] is True
        assert response_data['user']['name'] == create_user[1]["name"]
        assert response_data['user']['email'] == create_user[1]['email']
        assert response_data['accessToken']

    @allure.title("Тест на повторную регистрацию пользователя")
    def test_create_existing_user(self, create_user):
        existing_user = create_user[1]
        response_existing_user = ApiClient.create_new_user(existing_user)
        response_data_existing_user = response_existing_user.json()
        assert response_existing_user.status_code == 403
        assert response_data_existing_user["success"] is False
        assert response_data_existing_user["message"] == ResponseData.USER_ALREADY_EXISTS_MESSAGE

    @allure.title("Тест на регистрацию пользователя с  одним пустым из обязательныйх полей")
    @pytest.mark.parametrize("missing_field", [{"email": "test@@yandex.ru", "password": "test_password"},
                                               {'password': '12345678', 'name': 'test_name'},
                                               {'email': 'test@yandex.ru', 'name': 'test_name'}
                                               ])
    def test_create_user_with_empty_field(self, missing_field):
        response_user_with_empty_field = ApiClient.create_new_user(missing_field)
        response_data_user_with_empty_field = response_user_with_empty_field.json()
        assert response_user_with_empty_field.status_code == 403
        assert response_data_user_with_empty_field["success"] is False
        assert response_data_user_with_empty_field["message"] == ResponseData.REQUIRED_FIELDS_MISSING_MESSAGE

import allure
import requests

from urls import Endpoints


class ApiClient:

    @staticmethod
    @allure.step("Создание пользователя")
    def create_new_user(new_user_body):
        response = requests.post(Endpoints.AUTH_REGISTER, json=new_user_body)
        return response

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        response = requests.delete(Endpoints.API_AUTH_USER, headers={"Authorization": token})
        return response

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(user_body):
        response = requests.post(Endpoints.API_AUTH_LOGIN, json=user_body, timeout=50)
        return response

    @staticmethod
    @allure.step("Обновление данных о пользователе")
    def update_user_data(token, payload):
        response = requests.patch(Endpoints.API_AUTH_USER, headers={"Authorization": token}, data=payload)
        return response

    @staticmethod
    @allure.step("Обновление данных о пользователе")
    def receive_ingredients():
        response = requests.get(Endpoints.API_INGREDIENTS)
        return response

    @staticmethod
    @allure.step("Создание заказа")
    def create_orders(token, ingredients):
        response = requests.post(Endpoints.API_ORDERS, headers={"Authorization": token}, data=ingredients)
        return response

    @staticmethod
    @allure.step("Получение заказа")
    def get_user_orders(token):
        response = requests.get(Endpoints.API_ORDERS, headers={"Authorization": token})
        return response

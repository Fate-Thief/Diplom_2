class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'


class Endpoints:
    # User
    AUTH_REGISTER = Urls.BASE_URL + "/api/auth/register"
    API_AUTH_USER = Urls.BASE_URL + "/api/auth/user"
    API_AUTH_LOGIN = Urls.BASE_URL + "/api/auth/login"

    # Orders
    API_ORDERS = Urls.BASE_URL + "/api/orders"
    API_INGREDIENTS = Urls.BASE_URL + "/api/ingredients"

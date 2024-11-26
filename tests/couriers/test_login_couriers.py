import allure
import requests
from data import Urls
from faker_data import FakerData


class TestLoginCourier:
    @allure.title('Тест на успешную авторизацию курьера')
    def test_login_courier_success(self, courier):
        response = requests.post(
            Urls.LOGIN_COURIERS_URL,
            courier)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Тест на невозможность авторизоваться незарегистрированному пользователю ')
    def test_login_non_existent_courier_error(self):
        response = requests.post(
            Urls.LOGIN_COURIERS_URL,
            FakerData.generate_data_account_without_name())
        assert response.status_code == 404 and 'Учетная запись не найдена' in response.text

    @allure.title('Тест на обязательность поля "login"')
    def test_missing_required_login_error(self):
        response = requests.post(
            Urls.LOGIN_COURIERS_URL,
            FakerData.generate_data_account_without_login())
        assert response.status_code == 400 and 'Недостаточно данных для входа' in response.text

    @allure.title('Тест на обязательность полей "password"')
    def test_missing_required_password_error(self):
        response = requests.post(
            Urls.LOGIN_COURIERS_URL,
            FakerData.generate_data_account_without_password())
        assert response.status_code == 504

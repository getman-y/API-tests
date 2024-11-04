import allure
import requests
from data import Urls
from faker_data import FakerData


class TestCreateCourier:
    @allure.title('Тест на успешное создание курьера')
    def test_create_courier_success(self):
        response = requests.post(
            Urls.CREATE_COURIERS_URL,
            FakerData.generate_full_data_account())
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Тест на невозможность создать двух курьеров с одинаковым логином')
    def test_create_two_couriers_with_same_login_error(self):
        data = FakerData.generate_full_data_account()
        requests.post(Urls.CREATE_COURIERS_URL, data)
        response = requests.post(
            Urls.CREATE_COURIERS_URL,
            data)
        assert response.status_code == 409 and 'Этот логин уже используется. Попробуйте другой.' in response.text

    @allure.title('Тест на обязательность логина при создании курьера')
    def test_create_courier_without_login_error(self):
        response = requests.post(
            Urls.CREATE_COURIERS_URL,
            FakerData.generate_data_account_without_login())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Тест на обязательность пароля при создании курьера')
    def test_create_courier_without_password_error(self):
        response = requests.post(
            Urls.CREATE_COURIERS_URL,
            FakerData.generate_data_account_without_password())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

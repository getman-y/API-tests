import requests
from faker import Faker

from data import Urls


class FakerData:
    @staticmethod
    def generate_full_data_account():
        faker_data = Faker()
        login = faker_data.user_name()
        password = faker_data.password()
        first_name = faker_data.name()
        data = {
            "login": login,
            "password": password,
            "first_name": first_name
        }
        return data

    @staticmethod
    def generate_data_account_without_login():
        faker_data = Faker()
        password = faker_data.password()
        first_name = faker_data.name()
        data = {
            "password": password,
            "first_name": first_name
        }
        return data

    @staticmethod
    def generate_data_account_without_password():
        faker_data = Faker()
        login = faker_data.user_name()
        first_name = faker_data.name()
        data = {
            "login": login,
            "first_name": first_name
        }
        print(data)
        return data

    @staticmethod
    def generate_data_account_without_name():
        faker_data = Faker()
        login = faker_data.user_name()
        password = faker_data.password()
        data = {
            "login": login,
            "password": password
        }
        return data

    @staticmethod
    def register_new_courier_and_return_login_password():
        login_pass = {}
        faker_data = Faker()
        login = faker_data.user_name()
        password = faker_data.password()
        first_name = faker_data.name()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(Urls.CREATE_COURIERS_URL, data=payload)

        if response.status_code == 201:
            login_pass["login"] = login
            login_pass["password"] = password
        return login_pass

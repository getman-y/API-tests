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


class FakerOrders:
    data = {
        "firstName": "Юля",
        "lastName": "Гетман",
        "address": "Москва",
        "metroStation": 1,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            ""
        ]
    }

import requests
from data import Urls
from faker_data import FakerData


class CourierMethods:
    @staticmethod
    def create_courier_and_return_data():
        data = FakerData.generate_full_data_account()
        requests.post(
            Urls.CREATE_COURIERS_URL,
            data)
        return {'login': data.get('login'), 'password': data.get('password')}

    @staticmethod
    def login_courier_and_return_id(data):
        response = requests.post(
            Urls.LOGIN_COURIERS_URL,
            data)
        return response.json()['id']

    @staticmethod
    def delete_courier(courier_id):
        payload = {'id': courier_id}
        requests.delete(
            f'{Urls.CREATE_COURIERS_URL}/{courier_id}', params=payload, data=payload)

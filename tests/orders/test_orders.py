import json
import allure
import pytest
import requests
from data import Urls
from faker_data import FakerOrders


class TestOrders:

    @pytest.mark.parametrize('data', [{"color": ["BLACK"]}, {"color": ["GREY"]},
                                      {"color": ["BLACK", "GREY"]}, {"color": [""]}, ])
    @allure.title('Тест на успешное создание заказа')
    def test_create_order_success(self, data):
        FakerOrders.data.update(data)
        response = requests.post(Urls.ORDERS_URL, data=json.dumps(FakerOrders.data),
                                 headers={'Content-Type': 'application/json'})
        assert response.status_code == 201 and 'track' in response.text

    @allure.title('Тест на успешное возвращение списка заказов')
    def test_return_list_orders_success(self):
        payload = {'limit': '1', 'page': '0'}
        response = requests.get(Urls.ORDERS_URL, params=payload)
        assert response.status_code == 200 and 'orders' in response.text

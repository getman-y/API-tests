import pytest
from methods.courier_methods import CourierMethods


@pytest.fixture()
def courier():
    couriers = CourierMethods()
    data = couriers.create_courier_and_return_data()
    yield data
    courier_id = couriers.login_courier_and_return_id(data)
    couriers.delete_courier(courier_id)


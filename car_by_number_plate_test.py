import pytest
import requests
import dotenv
import os

@pytest.fixture(scope="function", params=[
(1, 2, 3),
("abc", "abc", "abcabc"),
(5, 4, 9)],
ids=["len>5","len<5","len==5"]
)
def param_test(request):
    return request.param

#2 POST Запрос данных ТС по ГОС.знаку
def test_car_by_number_plate(obtain_token):
    host = os.getenv('HOST') + "/v2/insured_objects/cars/by_number_plate"
    print(host)
    assert True

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

#4 POST Создание ТС
def test_car_creating(obtain_token):
    host = os.getenv('HOST') + "/v3/insured_objects/cars"
    print(host)
    assert True

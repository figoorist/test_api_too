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

#6 POST Объединение субъектов и объектов страхования в одну сущность
def test_drivers_car_union(obtain_token):
    host = os.getenv('HOST') + "/v1/insured_objects/"
    print(host)
    assert True

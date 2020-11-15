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

#7 POST Создание договора
def test_agreement_creating(obtain_token):
    host = os.getenv('HOST') + "/v3/agreements/calculations"
    print(host)
    assert True

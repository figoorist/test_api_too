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

#8 PATCH Обновление Договора в системе AgentApp
def test_agreement_renewal(obtain_token):
    host = os.getenv('HOST') + "/v1/agreements/"
    print(host)
    assert True

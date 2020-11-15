import pytest
import requests
import dotenv
import os

@pytest.fixture(scope="session")
def obtain_token(request):
    host = os.getenv('HOST') + "/v1/users/obtain-token"
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    response = requests.post(host, data = {'username':username, 'password':password})

    return response.json()['token']

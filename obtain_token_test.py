import pytest
import requests
import dotenv
import os

dotenv.load_dotenv()

correct_username = os.getenv('USERNAME')
incorrect_username_1 = "@mail.ru"
incorrect_username_2 = "ya.ru"

correct_password = os.getenv('PASSWORD')
wrong_password = "123456"
blank_password = ""

@pytest.fixture(scope="function", params=[
({'username':correct_username, 'password':correct_password}, 200, "token", ""),
({'username':correct_username, 'password':wrong_password}, 400, "non_field_errors", ["Unable to log in with provided credentials."]),
({'username':incorrect_username_1, 'password':correct_password}, 400, "non_field_errors", ["Unable to log in with provided credentials."]),
({'username':correct_username, 'password':blank_password}, 400, "password", ["This field may not be blank."]),
({'username':incorrect_username_1, 'password':blank_password}, 400, "password", ["This field may not be blank."])
],
ids=["correct username, correct password",
    "correct username, wrong password",
    "incorrect username 1, correct_password",
    "correct username, blank password",
    "incorrect username 1, blank password"
    ]
)
def param_test(request):
    return request.param

#1 POST Получение токена
def test_obtain_token(obtain_token, param_test):
    (params_data, expected_status_code, expected_node, expected_message) = param_test

    host = os.getenv('HOST') + "/v1/users/obtain-token"
    response = requests.post(host, data = params_data)

    errors = []

    if not response.status_code == expected_status_code:
        errors.append("status codes do not match")
    if not expected_node in response.json():
        errors.append("node {0} doesn't contain in response".format(expected_node))
    elif not expected_message == response.json()[expected_node] and response.status_code != 200:
        errors.append("message {0} doesn't contain in response".format(expected_message))

    assert not errors, "errors occured:\n{}".format("\n".join(errors))

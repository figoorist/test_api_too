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
(correct_username, correct_password, 200, "token", ""),
(correct_username, wrong_password, 400, "non_field_errors", ["Unable to log in with provided credentials."]),
(incorrect_username_1, correct_password, 400, "non_field_errors", ["Unable to log in with provided credentials."]),
(correct_username, blank_password, 400, "password", ["This field may not be blank."]),
(incorrect_username_1, blank_password, 400, "password", ["This field may not be blank."])
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
    (username, password, expected_status_code, expected_node, expected_message) = param_test

    host = os.getenv('HOST') + "/v1/users/obtain-token"
    response = requests.post(host, data = {'username':username, 'password':password})

    errors = []

    # replace assertions by conditions
    if not response.status_code == expected_status_code:
        errors.append("status codes do not match")
    if not expected_node in response.json():
        errors.append("node {0} doesn't contain in response".format(expected_node))
    elif not expected_message == response.json()[expected_node] and response.status_code != 200:
        errors.append("message {0} doesn't contain in response".format(expected_message))

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))

    #assert response.status_code == expected_status_code

import pytest
import requests
import dotenv
import os

dotenv.load_dotenv()

correct_number = "O518XT98"
number_with_cirillic = "О518ХТ98"
number_with_russian_symbols = "O518ЧT98"
blank_number = ""
wrong_number = "777"
number_with_punctuation = "?;;.,!!"

@pytest.fixture(scope="function", params=[
({"number_plate":correct_number}, 201, "vin_number", ""),
({"number_plate":number_with_cirillic}, 201, "vin_number", ""),
({"number_plate":number_with_russian_symbols}, 400, "error", "Не удалось получить данные от АвтоКод"),
({"number_plate":blank_number}, 400, "error", "Не удалось получить данные от АвтоКод"),
({"number_plate":wrong_number}, 400, "error", "Не удалось получить данные от АвтоКод"),
({"number_plate":number_with_punctuation}, 400, "error", "Не удалось получить данные от АвтоКод")
],
ids=["correct_number",
    "number with cirillic",
    "number with russian_symbols",
    "blank number",
    "wrong number",
    "number with punctuation"
    ]
)
def param_test(request):
    return request.param


#2 POST Запрос данных ТС по ГОС.знаку
def test_car_by_number_plate(obtain_token, param_test):
    (params_data, expected_status_code, expected_node, expected_message) = param_test

    host = os.getenv('HOST') + "/v2/insured_objects/cars/by_number_plate"

    response = requests.post(host, data = params_data, headers={"Authorization": "Token {0}".format(obtain_token)})

    errors = []

    if not response.status_code == expected_status_code:
        errors.append("status codes do not match")
    if not expected_node in response.json():
        errors.append("node {0} doesn't contain in response".format(expected_node))
    elif not expected_message == response.json()[expected_node] and response.status_code != 201:
        errors.append("message {0} doesn't contain in response".format(expected_message))

    assert not errors, "errors occured:\n{}".format("\n".join(errors))

import data
import configuration
import requests
import sender_stand_request
import pytest

## ======================= Positive Asserts ==================== ##

def positive_assert(kit_name):
    user_response = sender_stand_request.post_new_client_kit(kit_name)

    assert user_response.status_code == 201
    response_body = user_response.json()
    assert response_body.get("name") == kit_name["name"]



## ===================== Positive Tests ====================== ##

def test_create_kit_allowed_chars_1_success():
    positive_assert(data.one_letter)

def test_create_kit_max_allowed_chars_511_success():
    positive_assert(data.max_allowed_chars)

def test_create_kit_with_special_chars_success():
    positive_assert(data.special_chars)

def test_create_kit_with_spaces_success():
    positive_assert(data.name_with_spaces)

def test_create_kit_with_numbers_success():
    positive_assert(data.name_with_numbers)

## ======================= Negative Asserts ====================##

def negative_assert(kit_name):
    user_response = sender_stand_request.post_new_client_kit(kit_name)

    assert user_response.status_code == 400


## ===================== Negative Tests ====================== ##

def test_create_kit_zero_chars_code_400():
    negative_assert(data.zero_chars)

def test_create_kit_512_chars_code_400():
    negative_assert(data.surpass_max_allowed_chars)

def test_create_kit_empty_params_code_400():
    negative_assert(data.no_name)

def test_create_kit_integer_code_400():
    negative_assert(data.int_numbers)

import pytest
import json

from src.constants import FILE_NAME
from src.parse import parse

@pytest.fixture
def customers():
    customers = parse(FILE_NAME)
    yield customers

def test_parsed_file_length(customers):
    assert len(customers) == 32

def test_parsed_customer_one_user_id(customers):
    assert customers[0]['user_id'] == 12

def test_parsed_customer_one_name(customers):
    assert customers[0]['name'] == 'Christina McArdle'

def test_parsed_customer_latitude(customers):
    assert customers[0]['latitude'] == '52.986375'

def test_parsed_customer_longitude(customers):
    assert customers[0]['longitude'] == '-6.043701'

def test_parsed_customer_object_user_id(customers):
    for customer in customers:
        if 'user_id' not in customer:
            assert False
    assert True

def test_parsed_customer_object_name(customers):
    for customer in customers:
        if 'name' not in customer:
            assert False
    assert True

def test_parsed_customer_object_longitude(customers):
    for customer in customers:
        if 'longitude' not in customer:
            assert False
    assert True

def test_parsed_customer_object_latitude(customers):
    for customer in customers:
        if 'latitude' not in customer:
            assert False
    assert True

def test_parsed_missing_file():
    with pytest.raises(Exception):
        customers = parse('missing.txt')

def test_parsed_customer_missing_key():
    with pytest.raises(KeyError):
        customers = parse('tests/test_customers_key_error.txt')

def test_parsed_customer_invalid_json():
    with pytest.raises(Exception):
        customers = parse('tests/test_customers_value_error.txt')

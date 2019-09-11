import pytest

from src.parse import parse
from src.invite import invite
from src.constants import FILE_NAME

@pytest.fixture
def invitees():
    customers = parse(FILE_NAME)
    invitees = invite(customers)
    yield invitees

def test_invitees_length(invitees):
    assert len(invitees) == 16

def test_invitees_user_ids(invitees):
    user_ids = []
    for invitee in invitees:
        user_ids.append(invitee['user_id'])
    assert sorted(user_ids) == [4,5,6,8,11,12,13,15,17,23,24,26,29,30,31,39]

def test_invitees_length_zero():
    customers = parse('tests/test_invitees_zero.txt')
    invitees = invite(customers)
    assert len(invitees) == 0

def test_invitees_length_all():
    customers = parse('tests/test_invitees_all.txt')
    invitees = invite(customers)
    assert len(invitees) == 2

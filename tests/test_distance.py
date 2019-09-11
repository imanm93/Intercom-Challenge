import pytest

from src.point import Point
from src.distance import distance
from src.constants import DUBLIN_OFFICE_LOCATION

def test_distance_to_London():
    London = Point(51.5074, -0.1278)
    dist = distance(London, DUBLIN_OFFICE_LOCATION)
    assert dist == pytest.approx(463, 1)

def test_distance_to_Dublin():
    dist = distance(DUBLIN_OFFICE_LOCATION, DUBLIN_OFFICE_LOCATION)
    assert dist == pytest.approx(0, 0.001)

def test_distance_order_insensitive():
    London = Point(51.5074, -0.1278)
    dist1 = distance(DUBLIN_OFFICE_LOCATION, London)
    dist2 = distance(London, DUBLIN_OFFICE_LOCATION)
    assert dist1 == pytest.approx(dist2, 0.001)

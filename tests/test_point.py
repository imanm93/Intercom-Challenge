import pytest
import math

from src.point import Point

def test_point_x_degree_to_radian_conversion():
    p = Point(90, 0)
    assert p.x == (math.pi / 2)

def test_point_y_degree_to_radian_conversion():
    p = Point(0, 90)
    assert p.y == (math.pi / 2)

def test_point_x_out_of_bounds_max():
    with pytest.raises(ValueError):
        p = Point(91, 0)

def test_point_x_out_of_bounds_min():
    with pytest.raises(ValueError):
        p = Point(-91, 0)

def test_point_y_out_of_bounds_max():
    with pytest.raises(ValueError):
        p = Point(0, 181)

def test_point_y_out_of_bounds_min():
    with pytest.raises(ValueError):
        p = Point(0, -181)

def test_point_x_type():
    with pytest.raises(Exception):
        p = Point("0", 90)

def test_point_y_type():
    with pytest.raises(Exception):
        p = Point(0, "90")

def test_point_type():
    with pytest.raises(Exception):
        p = Point("0", "90")

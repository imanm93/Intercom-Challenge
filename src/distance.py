import math
from src.constants import EARTH_MEAN_RADIUS

def distance(point_one, point_two):
    """Return a float

    Calculate the distance between two points in a sphere in Kilometres
    """

    point_one_X, point_one_Y = point_one.x, point_one.y # phi1,lambda1
    point_two_X, point_two_Y = point_two.x, point_two.y # phi2,lambda2

    # Reference:  See wikipedia article - https://en.wikipedia.org/wiki/Great-circle_distance - for distance formulae

    sin_phi_one = math.sin(point_one_X) # sin phi1
    sin_phi_two = math.sin(point_two_X) # sin phi2

    cos_phi_one = math.cos(point_one_X) # cos phi1
    cos_phi_two = math.cos(point_two_X) # cos phi2

    sin_delta = math.sin(point_two_Y - point_one_Y) # sin delta lambda
    cos_delta = math.cos(point_two_Y - point_one_Y) # cos delta lambda

    atan_y = math.sqrt((cos_phi_two * sin_delta)**2 + ((cos_phi_one * sin_phi_two) - (sin_phi_one * cos_phi_two * cos_delta))**2)
    atan_x = (sin_phi_one * sin_phi_two) + (cos_phi_one * cos_phi_two * cos_delta)

    return math.atan2(atan_y, atan_x) * EARTH_MEAN_RADIUS

import math

class Point:
    """This class represents a geographical point in radians"""

    def __init__(self, x, y):

        if x < -90 or x > 90:
            raise ValueError("Latitude must be between -90 and 90 degrees")

        if y < -180 or y > 180:
            raise ValueError("Longitude must be between -180 and 180 degrees")

        try:
            self.x = self.deg_to_rad(x)
            self.y = self.deg_to_rad(y)
        except TypeError:
            raise Exception("Location coordinates must be of type Number")

    def deg_to_rad(self, degree):
        """Return a float

        Convert degree to radians
        """
        return degree * (math.pi / 180)

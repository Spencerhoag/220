"""
sphere.py
"""
import math


class Sphere:
    """
    represents a sphere with a radius, surface area, and volume.
    """
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * math.pow(self.radius, 3)

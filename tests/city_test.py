import unittest

from models.city import *

from models.country import *

class TestCity(unittest.TestCase):
    def setUp(self):
        self.london = City("London", "Tower of London", "23°")
        self.berlin = City("Berlin", "Brandenburg Gate", "24°")
        self.moscow = City("Moscow", "Red Square", "24°")

    def test_city_has_name(self):
        self.assertEqual("Berlin", self.berlin.name)

    def test_city_has_attractions(self):
        self.assertEqual("Brandenburg Gate", self.berlin.attractions)

    def test_city_temperature(self):
        self.assertEqual("24°", self.berlin.temperature)

    


    #     self.name = name
    #     self.attractions = attractions
    #     self.temperature = temperature
    #     self.id = id
    #     self.visited = visited
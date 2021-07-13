import unittest

from models.city import *

from models.country import *

class TestCity(unittest.TestCase):
    def setUp(self):
        self.uk = Country("UK", "Europe", "67,000,000", "English", "Pound(£)")
        self.germany = Country("Germany", "Europe", "83,000,000", "German", "Euro(€)")
        self.russia = Country("Russia", "Europe/Asia", "144,000,000", "Russian", "Ruble(₽)")

        self.london = City("London", "UK", "Tower of London", "23°", self.uk)
        self.berlin = City("Berlin", "Germany", "Brandenburg Gate", "24°", self.germany)
        self.moscow = City("Moscow", "Russia", "Red Square", "24°", self.russia)


    def test_city_has_name(self):
        self.assertEqual("Berlin", self.berlin.name)

    def test_city_has_attractions(self):
        self.assertEqual("Brandenburg Gate", self.berlin.attractions)

    def test_city_temperature(self):
        self.assertEqual("24°", self.berlin.temperature)

    def test_city_has_a_country(self):
        self.assertEqual("Germany", self.berlin.country)

    #     self.name = name
    #     self.country = country
    #     self.attractions = attractions
    #     self.temperature = temperature
    #     self.id = id
    #     self.visited = visited
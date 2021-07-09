import unittest

from models.country import *

from models.city import *

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.uk = Country("UK", "London", 67000000, "English", "Pound")
        self.germany = Country("Germany", "Berlin", 83000000, "German", "Euro")
        self.russia = Country("Russia", "Moscow", 144000000, "Russian", "Ruble")


        # self.name = name
        # self.capital_city = capital_city
        # self.population = population
        # self.language = language
        # self.currency = currency
        # self.id = id
        # self.visited = visited
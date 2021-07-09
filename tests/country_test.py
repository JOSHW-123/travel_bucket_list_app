import unittest

from models.country import *

from models.city import *

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.uk = Country("UK", "Europe", "67000000", "English", "Pound")
        self.germany = Country("Germany", "Europe", "83000000", "German", "Euro")
        self.russia = Country("Russia", "Europe/Asia", "144000000", "Russian", "Ruble")

    def test_country_has_name(self):
        self.assertEqual("UK", self.uk.name)

    def test_country_population(self):
        self.assertEqual("67000000", self.uk.population)

    def test_country_geographical_area(self):
        self.assertEqual("Europe", self.uk.geographical_area)

    def test_country_language(self):
        self.assertEqual("English", self.uk.language)

    def test_country_currency(self):
        self.assertEqual("Pound", self.uk.currency)

        # self.name = name
        # self.geographical_area = geographical_area
        # self.population = population
        # self.language = language
        # self.currency = currency
        # self.id = id
        # self.visited = visited
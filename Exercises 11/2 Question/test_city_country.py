## 11-2. Population: Modify your function so it requires a third parameter,
## population. It should now return a single string of the form City, Country –
## population xxx, such as Santiago, Chile – population 5000000. Run test
## _cities.py again. Make sure test_city_country() fails this time.
## Modify the function so the population parameter is optional. Run test
## _cities.py again, and make sure test_city_country() passes again.
## Write a second test called test_city_country_population() that verifies you can call your function with the values 'santiago', 'chile', and
## 'population=5000000'. Run test_cities.py again, and make sure this new test
## passes.

import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    def test_city_country_population(self):
        """Can I include a population argument?"""
        santiago_chile = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')

unittest.main()

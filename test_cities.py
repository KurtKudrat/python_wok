import unittest
from city_function import city_and_country


class CityAndCountry(unittest.TestCase):

    '''testing city_country function out put.'''

    def test_city_country(self):
        '''do city name and country like Tokyo, Japan out put correctly '''
        full_city_info = city_and_country('tokyo','japan')
        self.assertEqual(full_city_info,'Tokyo, Japan')

    def test_city_country_populatiom(self):
        '''do city name and country like Tokyo, Japan , Population: 1000 out put correctly '''
        full_city_info = city_and_country('tokyo','japan','1000')
        self.assertEqual(full_city_info,'Tokyo, Japan, Population: 1000' )

unittest.main
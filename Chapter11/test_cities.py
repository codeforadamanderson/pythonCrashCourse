import unittest
from city_functions import city_state

class city_fuctions_test(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_state(self):
        """Do names like 'Kansas City, Missouri' work?"""
        formatted_city = city_state('kansas city', 'missouri')
        self.assertEqual(formatted_city, 'Kansas City, Missouri')

    def test_city_state_population(self):
        """Do names like 'Tampa Bay, Florida - Population: 3142663' work?"""
        formatted_city = city_state('tampa bay', 'florida', '3142663')
        self.assertEqual(
            formatted_city, 'Tampa Bay, Florida - Population: 3142663')
        
if __name__ == '__main__':
    unittest.main()
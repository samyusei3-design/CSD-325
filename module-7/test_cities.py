#Samuel Guizar
#9/16/26
#Module 7.2 Assignment

#Import unit test and city_country function
import unittest
from city_functions import city_country

#Create a class to test the city_country function
class TestCityCountry(unittest.TestCase):

    #Create a test method to test the city_country function
    def test_city_country(self):
        
        self.assertEqual(city_country('Santiago', 'Chile'), 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
    
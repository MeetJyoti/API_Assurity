import json
import unittest
import requests


API = 'https://api.tmsandbox.co.nz/v1/Categories/6328/Details.json?catalogue=false'

class APITEST(unittest.TestCase):

    assurity = requests.get(API)

    if assurity.status_code != 200:
        raise Exception('GET {}'.format(assurity.status_code))

    def test_name(self):
        
        self.assertEqual(self.assurity.json().get('Name'), 'Badges')

    def test_canRelist(self):
        
        self.assertTrue(self.assurity.json().get('CanRelist'))

    def test_Betterposition(self):
        
        promotions = self.assurity.json().get('Promotions')
        for item in promotions:
            if (item.get('Name') == 'Feature'):
                self.assertTrue('Better position in category' in item.get('Description'))


if __name__ == '__main__':

    print('API Test Running........')
    unittest.main()
    
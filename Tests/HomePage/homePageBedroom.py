import unittest

from WebDriverWrapper import Singleton

class HomePageBedroom(unittest.TestCase):
    
    def setUp(self):
        self.driver = Singleton.getInstance().driver

    def test_NavBar_Bedroom_Item(self):
        driver = self.driver
        driver.get('https://www.1stopbedrooms.com/')

        driver.find_element_by_id('menu3').click()

        url = driver.current_url
        pageTitle = driver.find_element_by_class_name('page-title').text

        self.assertIn('bedroom', url, 'Wrong URL by clicking Bedroom in navigation bar.')
        self.assertEqual(pageTitle, 'Bedroom', 'Wrong page title by clicking Bedroom in navigation bar.')

    def tearDown(self):
        self.driver.delete_all_cookies()
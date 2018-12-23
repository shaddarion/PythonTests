import unittest

from WebDriverWrapper import Singleton

class HomePageLivingRoom(unittest.TestCase):
    
    def setUp(self):
        self.driver = Singleton.getInstance().driver

    def test_NavBar_LivingRoom_Item(self):
        driver = self.driver
        driver.get('https://www.1stopbedrooms.com/')

        driver.find_element_by_id('menu5').click()

        url = driver.current_url
        pageTitle = driver.find_element_by_class_name('page-title').text

        self.assertIn('living', url, 'Wrong URL by clicking Living Room in navigation bar.')
        self.assertEqual(pageTitle, 'Living Room', 'Wrong page title by clicking Living Room in navigation bar.')

    def tearDown(self):
        self.driver.delete_all_cookies()
import unittest

from WebDriverWrapper import Singleton

class BedroomPageCatalog(unittest.TestCase):
    
    def setUp(self):
        self.driver = Singleton.getInstance().driver

    def test_Bedroom_Catalog(self):
        driver = self.driver
        driver.get('https://www.1stopbedrooms.com/')

        driver.find_element_by_id('menu3').click()

        driver.find_element_by_class_name('catalog-layred-tabs').find_element_by_link_text('Bedroom Sets').click()

        url = driver.current_url
        self.assertIn('bedroom/bedroom-sets', url, 'Wrong URL by clicking Bedroom in navigation bar.')

        pageTitle = driver.find_element_by_class_name('page-title').text
        self.assertEqual(pageTitle, 'Bedroom Sets')        

    def tearDown(self):
        self.driver.delete_all_cookies()
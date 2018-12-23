import unittest

from WebDriverWrapper import Singleton
from selenium import webdriver

class BedroomPageCatalog(unittest.TestCase):
    
    def setUp(self):
        # self.driver = webdriver.Chrome('')
        self.driver = Singleton.getInstance().driver

    def test_Bedroom_Catalog(self):
        driver = self.driver
        driver.get('https://www.1stopbedrooms.com/')

        driver.find_element_by_id('menu3').click()

        driver.find_element_by_class_name('catalog-layred-tabs').find_element_by_link_text('Bedroom Sets').click()

        url = driver.current_url
        pageTitle = driver.find_element_by_class_name('page-title').text

        self.assertIn('bedroom/bedroom-sets', url, 'Wrong URL by clicking Bedroom in navigation bar.')

    def tearDown(self):
        self.driver.delete_all_cookies()
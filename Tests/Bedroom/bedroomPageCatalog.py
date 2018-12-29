import unittest

from WebDriver.WebDriverWrapper import WebDriverWrapper
from WebDriverLocator.Locators import Locators

class BedroomPageCatalog(unittest.TestCase):
    
    def setUp(self):
        self.webDriver = WebDriverWrapper.getInstance()

    def test_Bedroom_Catalog(self):
        driver = self.webDriver
        driver.get('https://www.1stopbedrooms.com/')

        driver.clickElement(Locators.HomePage.NavigationBar.bedRoomButton)

        categoryContainer = driver.getWebElement(Locators.NavigationBarChildPages.categoryContainer)

        driver.findElementByLinkText('B111edroom Sets', categoryContainer).click()        

        url = driver.getCurrentUrl()
        self.assertIn('bedroom/bedroom-sets', url, 'Wrong URL by clicking Bedroom in navigation bar.')

        pageTitle = driver.getWebElement(Locators.NavigationBarChildPages.pageTitle).text
        self.assertIn('Bedroom Sets', pageTitle)

        self.fail('testttttttttttttt')
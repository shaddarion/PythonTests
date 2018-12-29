import unittest

from WebDriver.WebDriverWrapper import WebDriverWrapper
from WebDriverLocator.Locators import Locators

class HomePageBedroom(unittest.TestCase):
    
    def setUp(self):
        self.webDriver = WebDriverWrapper.getInstance()

    def test_NavBar_Bedroom_Button(self):
        driver = self.webDriver
        driver.get('https://www.1stopbedrooms.com/')

        driver.clickElement(Locators.HomePage.bedRoomNavigationBarButton).click()

        url = driver.getCurrentUrl()
        pageTitle = driver.getWebElement(Locators.NavigationBarChildPages.pageTitle).text

        self.assertIn('bedroom', url, 'Wrong URL by clicking Bedroom in navigation bar.')
        self.assertEqual(pageTitle, 'Bedroom', 'Wrong page title by clicking Bedroom in navigation bar.')

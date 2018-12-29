import unittest

from WebDriver.WebDriverWrapper import WebDriverWrapper
from WebDriverLocator.Locators import Locators

class HomePageLivingRoom(unittest.TestCase):
    
    def setUp(self):
        self.webDriver = WebDriverWrapper.getInstance()

    def test_NavBar_LivingRoom_Button(self):
        driver = self.webDriver
        driver.get('https://www.1stopbedrooms.com/')

        driver.clickElement(Locators.HomePage.livingRoomNavigationBarButton)
        # driver.getWebElement(Locators.HomePage.livingRoomNavigationBarButton).click()

        url = driver.getCurrentUrl()
        self.assertIn('living', url, 'Wrong URL by clicking Living Room in navigation bar.')

        pageTitle = driver.getWebElement(Locators.NavigationBarChildPages.pageTitle).text        
        self.assertEqual(pageTitle, 'Living Room', 'Wrong page title by clicking Living Room in navigation bar.')
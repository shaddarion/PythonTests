import unittest
from selenium import webdriver
import WebDriverWrapper

class GoogleTestCase(unittest.TestCase):
    
    def setUp(self):
        # self.browser = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')
        # self.browser.implicitly_wait(59)
        # self.addCleanup(self.browser.quit)
        self.browser = WebDriverWrapper.Singleton.getInstance().driver

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

    def testPageTitle2(self):
        self.browser.get('https://www.1stopbedrooms.com/')
        self.assertIn('Google', self.browser.title)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)


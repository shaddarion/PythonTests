import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import WebDriverWrapper
from Pages.homePage import HomePage

class HomePageTestCases(unittest.TestCase):
    
    def setUp(self):
        # self.driver = WebDriverWrapper.Singleton.getInstance().driver 
        self.driver = webdriver.Chrome('C:/ChromeDriver/chromedriver.exe')

    def test_PageTitle(self):

        driver = self.driver
        homePage = HomePage(driver)

        self.driver.get('https://www.1stopbedrooms.com/')

        # driver.find_element_by_class_name('home1-categories-block-content').click()

        driver.get_screenshot_as_file('test.png')
        

        if len(driver.find_elements_by_class_name('home1-categories-block-content')) > 0:
            pass
        else:
            self.fail('FAAAAAAAAAAAAIL') 

        # try: 
        #     homePage.getHomeCategoriesBlock().click()
        # except NoSuchElementException:
        #     print('Exception occured!!!')    
                

    #@unittest.skip('Skip for a while')
    def testPageTitle2(self):
        self.driver.get('https://www.1stopbedrooms.com/')
        self.assertIn('Google', self.driver.title)

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='G:/Developer/GitHub/PythonTests/Reports'))


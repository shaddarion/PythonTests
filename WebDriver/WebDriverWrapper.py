import json
import platform

from selenium import webdriver
from SuiteEnv import SuiteEnv
from WebDriver.UIElementLocator import UIElementLocator

def getDriverPath(pcName):
    with open('Computers.json', 'r') as f:
        fileContent = str(f.read())

    content = json.loads(fileContent)
    if pcName not in content:
        raise ValueError("Sorry, your computer is not in Computers.json file.")
    return content[pcName]

class WebDriverWrapper:
    # Here will be the instance stored.
    __instance                 = None
    __driver                   = None
    __driver_implicitly_wait   = 10
    __driver_page_load_timeout = 59

    @staticmethod
    def getInstance():
        """ Static access method. """
        if WebDriverWrapper.__instance == None:
            WebDriverWrapper()
        return WebDriverWrapper.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if WebDriverWrapper.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            WebDriverWrapper.__instance = self
            
            webdriverPath = self.getDriverPath()
            self.__driver = webdriver.Chrome(webdriverPath)
            self.__driver.implicitly_wait(self.__driver_implicitly_wait)
            self.__driver.set_page_load_timeout(self.__driver_page_load_timeout)
            self.__driver.maximize_window()

    def getScreenShotAsFile(self, path):
        print(path)
        self.__driver.get_screenshot_as_file(path)

    def getDriverPath(self):
        """ Returns path to the webdriver if your PC is in list. """
        webdriverPath = getDriverPath(platform.node())
        browser_env = SuiteEnv.getInstance().getEnv("browser")
        
        if browser_env == 'chrome':
            return webdriverPath + 'chromedriver.exe'
        elif browser_env == 'firefox':
            return webdriverPath + 'firefoxdriver.exe'
        else:
            return webdriverPath + 'chromedriver.exe'
    
    # FindElement block
    def getWebElement(self, locator, parent = None):
        (idType, value) = locator
        if (idType == UIElementLocator.ID):
            return self.findElementByID(value, parent)
        elif (idType == UIElementLocator.CLASS_NAME):
            return self.findElementByClassName(value, parent)
        elif (idType == UIElementLocator.CSS_SELECTOR):
            return self.findElementByCssSelector(value, parent)
        elif (idType == UIElementLocator.LINK_TEXT):
            return self.findElementByLinkText(value, parent)
        else:
            raise Exception("Wrong type id")

    def findElementByID(self, value, parent = None):
        if (parent == None):
            return self.__driver.find_element_by_id(value)
        else:
            return parent.find_element_by_id(value)

    def findElementByClassName(self, value, parent = None):
        if (parent == None):
            return self.__driver.find_element_by_class_name(value)
        else:
            return parent.find_element_by_class_name(value)

    def findElementByCssSelector(self, value, parent = None):
        if (parent == None):
            return self.__driver.find_element_by_css_selector(value)
        else:
            return parent.find_element_by_css_selector(value)

    def findElementByLinkText(self, value, parent = None):
        if (parent == None):
            return self.__driver.find_element_by_link_text(value)
        else:
            return parent.find_element_by_link_text(value)
    #####################

    # FindElements block
    def getWebElements(self, locator, parent = None):
        (idType, value) = locator
        if (idType == UIElementLocator.ID):
            return self.findElementsByID(value, parent)
        elif (idType == UIElementLocator.CLASS_NAME):
            return self.findElementsByClassName(value, parent)
        elif (idType == UIElementLocator.CSS_SELECTOR):
            return self.findElementsByCssSelector(value, parent)
        elif (idType == UIElementLocator.LINK_TEXT):
            return self.findElementsByLinkText(value, parent)
        else:
            raise Exception("Wrong type id")
    
    def findElementsByID(self, value, parent = None):
        if (parent == None):
            return self.__driver.find_elements_by_id(value)
        else:
            return parent.find_elements_by_id(value)

    def findElementsByClassName(self, value, parent = None):
        if (parent == None):
            return self.__driver.find_elements_by_class_name(value)
        else:
            return parent.find_elements_by_class_name(value)

    def findElementsByCssSelector(self, value, parent = None):
        if (parent == None):
            return self.__driver.find_elements_by_css_selector(value)
        else:
            return parent.find_elements_by_css_selector(value)
    
    def findElementsByLinkText(self, value, parent = None):
        if (parent == None):
            return self.__driver.find_elements_by_link_text(value)
        else:
            return parent.find_elements_by_link_text(value)
    #######################

    def get(self, url):
        self.__driver.get(url)

    def getCurrentUrl(self):
        return self.__driver.current_url

    def deleteAllCookies(self):
        self.__driver.delete_all_cookies()

    def quit(self):
        if (self.__driver):
            self.__driver.quit()

    def clickElement(self, locator, parent = None):
        self.getWebElement(locator, parent).click()
    
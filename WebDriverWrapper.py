import json
import platform

from selenium import webdriver
from SuiteEnv import SuiteEnv

def getDriverPath(pcName):
    with open('Computers.json', 'r') as f:
        fileContent = str(f.read())

    content = json.loads(fileContent)
    if pcName not in content:
        raise ValueError("Sorry, your computer is not in database")
    return content[pcName]

class Singleton:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
            
            webdriverPath = self.getDriverPath()
            self.driver = webdriver.Chrome(webdriverPath)
            # self.driver = webdriver.Chrome('C:/ChromeDriver/chromedriver.exe')
            self.driver.implicitly_wait(6)
            self.driver.set_page_load_timeout(59)
            self.driver.maximize_window()

    def quit(self):
        if (self.driver):
            self.driver.quit()

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
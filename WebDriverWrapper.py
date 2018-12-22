import json
import platform

from selenium import webdriver

import SuiteEnv

def getDriverPath(pcName):
    with open('os.json', 'r') as f:
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
            # webdriverPath = getDriverPath(platform.node())
            # webdriver_env = SuiteEnv.SuiteEnv.getInstance().getEnv("webdriver")
            self.driver = webdriver.Chrome('C:/ChromeDriver/chromedriver.exe')
            self.driver.implicitly_wait(6)
            self.driver.set_page_load_timeout(59)
            self.driver.maximize_window()

    def quit(self):
        if (self.driver):
            self.driver.quit()

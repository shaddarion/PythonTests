from selenium import webdriver

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
            self.driver = webdriver.Chrome('C:/ChromeDriver/chromedriver.exe')
            self.driver.implicitly_wait(20)
            self.driver.set_page_load_timeout(59)
            self.driver.maximize_window()
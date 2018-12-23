class SuiteEnv:
    # Here will be the instance stored.
    __instance = None
    map = {}

    @staticmethod
    def getInstance():
        """ Static access method. """
        if SuiteEnv.__instance == None:
            SuiteEnv()
        return SuiteEnv.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if SuiteEnv.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SuiteEnv.__instance = self

    def putEnv(self, key, value):
        self.map[key] = value

    def getEnv(self, key):
        if key not in self.map:
            raise Exception("Can't find key - " + key + ". Maybe you misspelled an argument. Pay attention to the arguments you've passed through command line.")
        return self.map[key]
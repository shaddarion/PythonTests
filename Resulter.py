import unittest
import TelegramBot

class Resulter(unittest.TestResult):    
    _telegram = TelegramBot.TelegramBot()
        
    def startTest(self, test):
        print('startTestRun')
        self._telegram.sendMessage_("Now is running " + str(test))
        super().startTest(test)

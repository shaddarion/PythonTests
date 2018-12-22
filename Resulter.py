import unittest
import TelegramBot
from TelegramBot import TelegramBot

class Resulter(unittest.TestResult):    
    _bot = TelegramBot()

    # def startTestRun(self):
    #     self._bot.sendMessage('startTestRun')

    def addFailure(self, test, err):
        self._bot.sendMessage('Failure occured: ' + str(test) + ' ' + str(err))
        super().addFailure(test, err)

    def addError(self, test, err):
        self._bot.sendMessage('Error occured: ' + str(test) + ' ' + str(err))
        super().addError(test, err)

    def startTest(self, test):
        self._bot.sendMessage('Now is running ' + str(test))
        super().startTest(test)

    # def stopTest(self, test):
    #     print('stopTest')
    #     self._bot.sendMessage('Now is stoped ' + str(test))

    #     if test._outcome.success == False:
    #         self._bot.sendMessage('Test failed: lalala ' + str(test))
    #     else:
    #         self._bot.sendMessage('Test passed: lololo ' + str(test))

    #     super().startTest(test)

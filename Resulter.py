import unittest
import TelegramBot
from TelegramBot import TelegramBot
from WebDriverWrapper import Singleton
from Reporter import Reporter

class Resulter(unittest.TestResult):    
    _bot = TelegramBot()

    def startTestRun(self):
        self._bot.sendMessage('New Test Run')

    def addFailure(self, test, err):
        testName = str(test._testMethodName)
        Singleton.getInstance().driver.get_screenshot_as_file(Reporter.getInstance().getReportFolder() + '/' + testName + 'Failure.png')
        # self._bot.sendMessage('Failure occured: ' + testName + ' ' + str(err))
        super().addFailure(test, err)

    # def addError(self, test, err):
    #     self._bot.sendMessage('Error occured: ' + str(test) + ' ' + str(err))
    #     super().addError(test, err)

    # def stopTest(self, test):
    #     print('stopTest')
    #     self._bot.sendMessage('Now is stoped ' + str(test))

    #     if test._outcome.success == False:
    #         self._bot.sendMessage('Test failed: lalala ' + str(test))
    #     else:
    #         self._bot.sendMessage('Test passed: lololo ' + str(test))

    #     super().startTest(test)

import unittest
import TelegramBot
from TelegramBot import TelegramBot
from WebDriver.WebDriverWrapper import WebDriverWrapper
from Reporter import Reporter

class Resulter(unittest.TestResult):    
    _bot = TelegramBot()

    def startTestRun(self):
        self._bot.sendMessage('New Test Run')

    def startTest(self, test):
        WebDriverWrapper.getInstance().deleteAllCookies()

    def addFailure(self, test, err):
        testName = str(test._testMethodName)
        WebDriverWrapper.getInstance().getScreenShotAsFile(Reporter.getInstance().getReportFolder() + '/' + testName + '_Failure.png')
        super().addFailure(test, err)

    def addError(self, test, err):
        testName = str(test._testMethodName)
        WebDriverWrapper.getInstance().getScreenShotAsFile(Reporter.getInstance().getReportFolder() + '/' + testName + '_Error.png')
        super().addError(test, err)

    # def stopTest(self, test):
    #     print('stopTest')
    #     self._bot.sendMessage('Now is stoped ' + str(test))

    #     if test._outcome.success == False:
    #         self._bot.sendMessage('Test failed: lalala ' + str(test))
    #     else:
    #         self._bot.sendMessage('Test passed: lololo ' + str(test))

    #     super().startTest(test)

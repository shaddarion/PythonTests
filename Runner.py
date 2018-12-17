import unittest
import Program
import WebDriverWrapper
import Resulter
import HtmlTestRunner
import datetime
from TelegramBot import TelegramBot

bot = TelegramBot()

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Program.HomePageTestCases))

resulter = Resulter.Resulter()
#HtmlTestRunner.HTMLTestRunner.resultclass = Resulter.Resulter
unittest.TextTestRunner.resultclass = Resulter.Resulter

# file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H%M_report.html")
# output = open(file_name, "w")

runner = unittest.TextTestRunner(verbosity=2)
#runner = HtmlTestRunner.HTMLTestRunner(output=output, verbosity = 1)
resulter = runner.run(suite)

bot.sendMessage('Errors:\n' + str(len(resulter.errors)) + '\nFailures:\n' + str(len(resulter.failures)) + '\nSkipped:\n' + str(len(resulter.skipped)) + '\nTestCount:\n' + str(resulter.testsRun))

print("errors")
print(len(resulter.errors))

for er in resulter.errors:
    (className, error) = er
    print(str(className))

print("failures")
print(len(resulter.failures))
print("skipped")
print(len(resulter.skipped))
print("testsRun")
print(resulter.testsRun)

WebDriverWrapper.Singleton.getInstance().driver.quit()
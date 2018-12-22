import unittest
import Program
import WebDriverWrapper
from Resulter import Resulter
import HtmlTestRunner
import datetime
from TelegramBot import TelegramBot
import SuiteEnv

import sys

from argparse import ArgumentParser

def writeResult(output, arrayResult, strResult):
    if len(arrayResult) > 0:
        output.write(strResult + ':\n\n')

        for i in arrayResult:
            output.write('TEST METHOD NAME - ' + i[0]._testMethodName + ':\n\n')
            output.write(str(i[1]))
            output.write('\n')

        output.write('\n')

def makeReport(resulter, output):
    writeResult(output, resulter.errors, 'Errors')
    writeResult(output, resulter.failures, 'Failures')

def suiteRunner():
    bot = TelegramBot()

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Program.HomePageTestCases))

    resulter = Resulter()
    unittest.TextTestRunner.resultclass = Resulter

    file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H%M_report.txt")
    output = open(file_name, "w")

    runner = unittest.TextTestRunner(verbosity=2)
    resulter = runner.run(suite)
    makeReport(resulter, output)

    WebDriverWrapper.Singleton.getInstance().quit()
    output.close()

    bot.sendMessage('Errors:\n' + str(len(resulter.errors)) + '\nFailures:\n' + str(len(resulter.failures)) + '\nSkipped:\n' + str(len(resulter.skipped)) + '\nTestCount:\n' + str(resulter.testsRun))

    print("errors")
    print(len(resulter.errors))    
    print("failures")
    print(len(resulter.failures))
    print("skipped")
    print(len(resulter.skipped))
    print("testsRun")
    print(resulter.testsRun)
    


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-w", "--webdriver", help="webdriver type")
    
    args = parser.parse_args()
    print(args)
    if 'help' is args:
        parser.print_help()
    else:
        SuiteEnv.SuiteEnv.getInstance().putEnv("webdriver", args.webdriver)
        suiteRunner()
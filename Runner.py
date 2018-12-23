import unittest
import datetime
import WebDriverWrapper
from argparse import ArgumentParser

from Resulter import Resulter
from TelegramBot import TelegramBot
from SuiteEnv import SuiteEnv

def writeResult(output, arrayResult, strResult):
    if len(arrayResult) > 0:
        output.write(strResult + ':\n\n')

        for i in arrayResult:
            output.write('TEST METHOD NAME - ' + i[0]._testMethodName + ':\n\n')
            output.write(str(i[1]))
            output.write('\n')

        output.write('\n')

def makeReport(file_name, resulter, patternString):
    output = open('Reports/' + file_name, 'w')
    
    output.write('Errors:\n' + str(len(resulter.errors)) + '\nFailures:\n' + str(len(resulter.failures)) + '\nSkipped:\n' + str(len(resulter.skipped)) + '\nTestCount:\n' + str(resulter.testsRun) + '\n\n')

    writeResult(output, resulter.errors, 'Errors')
    writeResult(output, resulter.failures, 'Failures')

    output.close()

def suiteRunner(patternString):
    bot = TelegramBot()

    patternTests = '*' + patternString + '*.py'
    tests = unittest.TestLoader().discover('.', pattern = patternTests)

    resulter = Resulter()
    unittest.TextTestRunner.resultclass = Resulter

    resulter = unittest.TextTestRunner(verbosity=1).run(tests)

    reportFileName = datetime.datetime.now().strftime('%Y_%m_%d_%H%M_' + patternString + '_report.txt')
    makeReport(reportFileName, resulter, patternString)

    WebDriverWrapper.Singleton.getInstance().quit()

    bot.sendMessage('Errors:\n' + str(len(resulter.errors)) + '\nFailures:\n' + str(len(resulter.failures)) + '\nSkipped:\n' + str(len(resulter.skipped)) + '\nTestCount:\n' + str(resulter.testsRun))
    bot.sendDocument('Reports/' + reportFileName)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-b', '--browser', help='browser type')
    parser.add_argument('-t', '--testPatern', help='start tests by pattern')
    
    args = parser.parse_args()
    print(args)
    if 'help' is args:
        parser.print_help()
    elif 'testPatern' in args:
        SuiteEnv.getInstance().putEnv('browser', args.browser)
        suiteRunner(args.testPatern)
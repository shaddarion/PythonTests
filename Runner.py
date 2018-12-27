import unittest
import WebDriverWrapper
from argparse import ArgumentParser
from Resulter import Resulter
from TelegramBot import TelegramBot
from SuiteEnv import SuiteEnv
from Reporter import Reporter

def suiteRunner(patternString):
    bot = TelegramBot()
    patternTests = ''

    if patternString == 'all':
        patternTests = '*.py'
    else:
        patternTests = '*' + patternString + '*.py'       

    tests = unittest.TestLoader().discover('.', pattern = patternTests)

    unittest.TextTestRunner.resultclass = Resulter

    reporter = Reporter.createInstance('Reports', patternString)

    resulter = unittest.TextTestRunner(verbosity=1).run(tests)

    # Make report and send notification if there're an errors or failures
    if len(resulter.errors) > 0 or len(resulter.failures) > 0:
        reporter.makeReport(resulter)

        bot.sendMessage('Errors:\n' + str(len(resulter.errors)) + '\nFailures:\n' + str(len(resulter.failures)) + '\nSkipped:\n' + str(len(resulter.skipped)) + '\nTestCount:\n' + str(resulter.testsRun))    
        bot.sendDocument(reporter.getReportFileName())

    WebDriverWrapper.Singleton.getInstance().quit()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-b', '--browser', help='browser type')
    parser.add_argument('-t', '--testPattern', help='start tests by pattern')
    
    args = parser.parse_args()
    print(args)
    if 'help' is args:
        parser.print_help()
    elif 'testPattern' in args:
        SuiteEnv.getInstance().putEnv('browser', args.browser)
        suiteRunner(args.testPattern)
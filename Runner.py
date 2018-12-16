import unittest
import Program
import WebDriverWrapper
import Resulter

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Program.GoogleTestCase))

resulter = Resulter.Resulter()
unittest.TextTestRunner.resultclass = Resulter.Resulter

runner = unittest.TextTestRunner(verbosity=2)
resulter = runner.run(suite)
print("errors")
print(len(resulter.errors))
print("failures")
print(len(resulter.failures))
print("skipped")
print(len(resulter.skipped))
print("testsRun")
print(resulter.testsRun)

WebDriverWrapper.Singleton.getInstance().driver.quit()
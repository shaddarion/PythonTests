import unittest

class Resulter(unittest.TestResult):

    # @classmethod
    def startTest(self, test):
        # super().startTest(test)
        print('startTestRun')
        super().startTest(test)

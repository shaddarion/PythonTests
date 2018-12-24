import datetime
import os

class Reporter:
    __instance       = None
    __pathToFolder   = ''
    __folderName     = ''
    __testPattern    = ''
    __reportFileName = 'Report.txt'

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Reporter.__instance == None:
            raise Exception("Should be created first!")
        return Reporter.__instance 

    @staticmethod
    def createInstance(pathToFolder, testPattern):
        """ Static access method. """
        if Reporter.__instance == None:
            Reporter(pathToFolder, testPattern)
        return Reporter.__instance 

    def __init__(self, pathToFolder, testPattern):
        """ Virtually private constructor. """
        if Reporter.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Reporter.__instance = self

        self.__pathToFolder = pathToFolder
        self.__testPattern  = testPattern

    def makeReport(self, resulter):
        output = open(self.getReportFileName(), 'w')
        
        output.write('Errors:\n' + str(len(resulter.errors)) + '\nFailures:\n' + str(len(resulter.failures)) + '\nSkipped:\n' + str(len(resulter.skipped)) + '\nTestCount:\n' + str(resulter.testsRun) + '\n\n')

        self.__writeResult(output, resulter.errors, 'Errors')
        self.__writeResult(output, resulter.failures, 'Failures')

        output.close()

    def getReportFileName(self):
        return self.getReportFolder() + '/' + self.__reportFileName

    def getReportFolder(self):
        if not self.__folderName:
            self.__createReportFolder()

        return self.__pathToFolder + '/' + self.__folderName
        
    def __writeResult(self, output, arrayResult, strResult):
        if len(arrayResult) > 0:
            output.write(strResult + ':\n\n')

            for i in arrayResult:
                output.write('TEST METHOD NAME - ' + i[0]._testMethodName + ':\n\n')
                output.write(str(i[1]))
                output.write('\n')

            output.write('\n')

    def __createReportFolder(self):
        prevCurrentFolder = os.getcwd()
        os.chdir(self.__pathToFolder)
        self.__folderName = datetime.datetime.now().strftime('%Y_%m_%d_%H%M_' + self.__testPattern)
        os.mkdir(self.__folderName)
        os.chdir(prevCurrentFolder)
    
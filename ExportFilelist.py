# -*- coding: utf-8 -*-
import getopt
import sys
import os
import re
"""
def regularFilename():

def findFilename():
    print "findFilename"

    fd = open('')
"""
class Listfilename(object):
    gsrcPath = ""
    gdstPath = ""
    def __init__(self, srcPath=None, dstPath=None):
        global gsrcPath
        global gdstPath
        gsrcPath = srcPath
        gdstPath = dstPath

    def scanDirectory(self, targetPath='.'):
        print "============================="
        fileList ={}

        for dirpath, dirnames, filenames in os.walk(targetPath):
            for filename in filenames:
                fileList[filename] = dirpath

        return fileList

    def regularFile(self, fileList, pattern):
        print "============================="
        filenames = fileList.keys()
        for filename in filenames:
            match = re.search(pattern=pattern,string=filename,flags=re.IGNORECASE)

            if match == None:
                del fileList[filename]

            else:
                pass

        return fileList

    def writeFile(self, fileList, path):
        print "============================="
        dstPath = path
        fd = open(dstPath, 'w')
        for filename in fileList:
            fd.write(filename)
            fd.write('\n')

        fd.close()

if __name__ == "__main__":

    fileList = []
    filenames = []

    classList = Listfilename()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:w:p:", ["pattern="])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(1)

    for opt, arg in opts:
        if opt == "-f":
            print " [*] scanning file : {0}".format(arg)
            fileList = classList.scanDirectory(arg)

        #    Listfilename(arg)
        elif (opt == "-p") or (opt == "--pattern"):
            print " [+] add pattern : {0}".format(arg)
            filenames = classList.regularFile(fileList, arg)

        elif (opt == '-w') or (opt == '--write'):
            print " [+] write file : {0}".format(arg)
            classList.writeFile(filenames, arg)

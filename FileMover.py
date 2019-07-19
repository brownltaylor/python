import os
import re
import shutil 
import sys

srcDir = os.listdir("C:\Users\shack\Documents\FileMoverChallenge\source")
destDir = os.listdir("C:\Users\shack\Documents\FileMoverChallenge\destination")

def validate(fileName):  
    pattern = re.match("[a-z]{3}[0-9]{1}[\w][0-9]{10}[\w][0-9]{4}(.txt)", fileName)
    return pattern
        

def convertToDict(fileDir):
    fileList = []
    fileDict = dict()
    print fileDir
    for srcFile in fileDir:
        if sys.argv[1] == "--log":
            print "Parsing files for valid format..." 
        valid = validate(srcFile)
        if valid != None:
            fileList.append(srcFile)
            fileDict.update({srcFile : srcFile.split("_")[1]})
        for key in fileDict: 
            if sys.argv[1] == "--log":
                print key + " is valid."
                print fileDict    
        return fileDict
        
def moveFiles(fileDir): 
    fileDict = convertToDict(fileDir)
    for destFolder in destDir:
        for key, value in fileDict.items():
            if value == destFolder: 
                shutil.move("C:\Users\shack\Documents\FileMoverChallenge\source/{0}".format(key), "C:\Users\shack\Documents\FileMoverChallenge\destination/{0}".format(value))
    
def copyFiles(fileDir):
   fileDict = convertToDict(fileDir)
   for destFolder in destDir:
      for key, value in fileDict.items(): 
            shutil.copy("C:\Users\shack\Documents\FileMoverChallenge\source/{0}".format(key), "C:\Users\shack\Documents\FileMoverChallenge\destination/{0}".format(value))   
        
        
def run(fileDir): 
    if sys.argv[1] == "--move": 
        moveFiles(fileDir)
    if sys.argv[1] == "--copy": 
        copyFiles(fileDir)
        
convertToDict(srcDir)


import os
import glob
import threading
from nltk.util import ngrams
from nltk.stem.porter import PorterStemmer

#Stemmer to stem the words
ps = PorterStemmer()

def digestData(rawData):
    """generates the ngrams of the given text
        | input : raw data read from the file stream
        | output: ngrams of the given input
    """
    #strip the punctuations
    finerText = str(rawData).lower().translate(None, "!?*+@#$%^&*()<>\"\':;.,-|_\n\r")
    #stem the data
    stemmedText = ps.stem(finerText)
    #generate character 5-grams of the stemmed text 
    return ngrams(list(stemmedText),5)

def digestFile(inFilePath, outFilePath):
    """reads file from inFilePath digests data and outputs
       the data in the outFilePath folder
       | input : path to the input file to read data inFilePath, 
                 path to the output file to write data outFilePath
       | output: None
    """
    #open input stream
    inFile = open(inFilePath)

    #open output stream
    outFile = open(outFilePath, "w")
    
    #read inputstream
    rawData = inFile.read()
    outFile.write(digestData(rawData))

def digestMultipleFiles(inFileList, outFilePath):
    """digests multiple files given in the inFileList
       and generates corresponding data in the outFilePath
       | input : digest the files given in the inFileList
       | output: None
    """
    for fileName in inFileList:
        digestFile(fileName, outFilePath+fileName)

def digestAllFiles(inDirectory, outDirectory):
    """uses 10 parallel threads to read 
       all the files in the inDirectory
       digests data and writes in the outDirectory
       each file in the outDirectory contains the respective
       ngrams of each file
       | input : directory name in which the corpus is situated
       | output: None
    """
    path = dirname + "/"
    thread_list=[]
    for i in range(1,10):
        listOfFiles = glob.glob(inDirectory+"/"+str(i)+"*")
        t = threading.Thread(target=digestMultipleFiles, args=(listOfFiles, outDirectory))
        thread_list.append(t)

    #start the thread execution
    for thread in thread_list:
        thread.start()
    
    #wait for the threads to stop
    for thread in thread_list:
        thread.join()


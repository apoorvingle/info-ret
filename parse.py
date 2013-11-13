import glob
from nltk.util import ngrams
from nltk.stem.porter import PorterStemmer

rawData = []
#open files
lOfFiles = glob.glob("corpusr/*.txt")
for docs in lOfFile:
    try:
        f = open(docs)
        rawData.append(f.read())
        f.close()
    except:
        pass


#read data 
#rawData = str(f.read())

#get the documents from the file

#strip the text off from punctuations

#stemmer
#ps = PorterStemmer()
#text = ps.stem(text)

#tokenize
#l = list(text)
#build character ngrams from the document

#n = 5
#fiveGrams = ngrams(l,n)
#for grams in fiveGrams:
#    print grams
#

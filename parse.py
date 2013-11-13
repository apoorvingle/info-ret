from nltk.util import ngrams
import sgmllib
import string

class FoundBody(Exception):
    pass

class ExtractBody(sgmllib.SGMLParser):
    def __init__(self,verbose=0):
        sgmllib.SGMLParser.__init__(self, verbose)
        self.body= self.data = None
    
    def handle_data(self, data):
        if self.data is not None:
            self.data.append(data)
    
    def start_body(self, attrs):
        self.data = []

    def end_title(self):
        self.body = string.join(self.data,"")
        raise FoundBody                             #AbortParsing as data found

def extract(file):
    #extract body from an sgml file stream
    p = ExtractBody()
    try:
        while 1:
            s = file.read(4096)
            if not s:
                break
            p.feed(s)
        p.close()
    except FoundBody:
        return p.body
    return None


#open file
f = open(r'reuters21578/reut2-000.sgm')

#read data 
rawData = f.read()

#get the documents from the file
print extract(open(r'reuters21578/reut2-000.sgm'))


#strip the text off from punctuations


#build character ngrams from the document
#n = 5
#fiveGrams = ngrams(text.lower().split(),n)
#for grams in fiveGrams:
#    print grams


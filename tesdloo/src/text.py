# import nltk.data
#nltk.download('punkt')
from src.MyRegex import *
from src.KMP import *
from src.BM import *
class Text:
    # konstuktor
    def __init__(self,filename):
        with open(filename,'r') as file:
            self.filename =filename.split('/')[-1]
            self.sentences = file.read().replace('. ','.\n').split('\n')  
    #getter
    def getName(self):
        return self.filename    
    def __repr__(self):
        for sentence in self.sentences:
            print(sentence)

    #matching
    def match(self,pat, met):
        if(met==1):
            return self.matchRegex(pat)
        elif(met==2):
            return self.matchKMP(pat)
        else:
            assert met==3
            return self.matchBM(pat) 
        
    def matchRegex(self,pat):
        for sentence in self.sentences:
            if(re.search(pat.lower(),sentence.lower())!=None):
                return sentence
        return None
    def matchKMP(self,pat):
        for sentence in self.sentences:
            if(KMPSearch(pat,sentence)):
                return sentence
        return None
    def matchBM(self,pat):
        for sentence in self.sentences:
            if(BMSearch(pat,sentence)):
                return sentence
        return None


# import nltk.data
#nltk.download('punkt')
from MyRegex import *
import KMP
import BM
class Text:
    def __init__(self,filename):
        with open('test1.txt','r') as file:
            self.sentences = file.read().replace('. ','.\n').split('\n')      
    # def __repr__(self):
    #     for sentence in self.sentences:
    #         print(sentence)
    def matchRegex(self,pat):
        for sentence in self.sentences:
            if(re.search(pat.lower(),sentence.lower())!=None):
                return sentence
        return None
    def matchKMP(self,pat):
        for sentence in self.sentences:
            if(KMP.KMPSearch(pat,sentence)):
                return sentence
        return None
    def matchBM(self,pat):
        for sentence in self.sentences:
            if(BM.search(pat,sentence)):
                return sentence
        return None
    def match(self,pat, met):
        if(met==1):
            return self.matchRegex(pat)
        elif(met==2):
            return self.matchKMP(pat)
        else:
            assert met==3
            return self.matchBM(pat)

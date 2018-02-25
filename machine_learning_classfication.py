import nltk
import sys

class MLC:
    def __init__(self,dataset):
        self.dataset = dataset
        self.ngramset = {}

    def generate_ngram_features(self,n):
        if n not in self.ngramset:
            self.ngramset[n] = []
        

    def get_reviews(dataset):
        '''accept a list of messages, return a list of messages that are classfied as useful results'''


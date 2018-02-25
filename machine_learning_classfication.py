import nltk
import sys
import pickle
from sklearn.linear_model import LogisticRegression

class MLC:
    def __init__(self,dataset,score):
        self.dataset = dataset
        self.score = score
        self.ngramset = {}
        self.pos_tags = ['$', "''", '(', ')', ',', '--', '.', ':', 'CC', 'CD', 'DT', 'EX', 'FW', 'IN',
                    'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$'
            , 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$',
                    'WRB', '``','#']
        f = open('expressive_subjectivity_words.pkl', 'rb')
        self.expressive_subjectivity_words = pickle.load(f)[:50]  # load the 50 most frequent words
        f.close()
        f = open('direct_subjectivity_words.pkl','rb')
        self.direct_subjectivity_words = pickle.load(f)[:50]
        f.close()

    def generate_ngram_features(self,n,message):
        '''accept a list of messages, return a set of features where each line is a line of features'''
        if n not in self.ngramset:
            lower_tokens = []
            for data in self.dataset:
                lower_tokens.extend(nltk.word_tokenize(data.lower()))
            self.ngramset[n] = nltk.FreqDist(lower_tokens)
        feature = []
        tokens = nltk.word_tokenize(message.lower())
        for keyword in self.ngramset[n]:
            if keyword in tokens:
                feature.append(0)
            else:
                feature.append(1)
        return feature

    def generate_pos_features(self,message):
        '''accept a list of messages, return a list of features for each of the message'''
        pos_dict = {}
        for tag in self.pos_tags:
            pos_dict[tag] = 0
        tokens = nltk.word_tokenize(message.lower())
        for (text, tag) in nltk.pos_tag(tokens):
            pos_dict[tag] += 1
        return list(pos_dict.values())

    def generate_imperative_expression_features(self,message):
        '''generate a binary feature indicating whether it is an imperative snetence'''
        tokens = nltk.word_tokenize(message)
        if nltk.pos_tag(tokens)[0][1] == 'VB':  # if the starting word have a verb POS
            return 1  # Then it's an imperative sentence
        elif 'must' in message or 'should' in message or 'need to' in message or 'have to' in message or 'ought to' in message:  # if a sentence contains such words
            return 1  # Then it's an imperative sentence
        else:
            return 0

    def generate_length_features(self,message):
        '''generate the number of words in a sentence'''
        tokens = nltk.word_tokenize(message)
        return len(tokens)

    def generate_expressive_subjectivity_features(self,message):
        occurence = []
        message = message.lower()
        for word in self.expressive_subjectivity_words:
            if word in message:
                occurence.append(1)
            else:
                occurence.append(0)
        return occurence

    def generate_direct_subjectivity_features(self,message):
        occurence = []
        message = message.lower()
        for word in self.direct_subjectivity_words:
            if word in message:
                occurence.append(1)
            else:
                occurence.append(0)
        return occurence

    def generate_feature_set(self,dataset):
        feature_set = []
        for data in dataset:
            feature = self.generate_pos_features(data)+self.generate_expressive_subjectivity_features(data)\
                      +self.generate_direct_subjectivity_features(data)+ [self.generate_imperative_expression_features(data),self.generate_length_features(data)]
            feature_set.append(feature)
        return feature_set

    def get_reviews(self,messages):
        '''accept a list of messages, return a list of messages that are classfied as useful results'''
        training_data = self.generate_feature_set(self.dataset)
        test_data = self.generate_feature_set(messages)
        model = LogisticRegression(multi_class='multinomial',solver='newton-cg')
        model.fit(training_data,self.score)
        predictions = model.predict(test_data)
        return [messages[i] for i in range(len(predictions)) if predictions[i] == 1]




f = open('text.txt','r')
text = f.readlines()
f.close()
messages = []
scores = []
for l in text:
    message,score = l.split('^')
    messages.append(message)
    scores.append(int(score[:-1]))
train = messages[:112]
test = messages[112:]
m = MLC(train,scores[:112])
reviews = set(m.get_reviews(test))
for l in reviews:
    print(l)

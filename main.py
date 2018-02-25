from  get_introduction import *
from  get_api import *
from machine_learning_classfication import *
from search import *
from reader import *

currency = get_coin_info()
currency = currency.replace(' ','-')
get_introduction(currency)
# messages = get_Twitter_result(currency)
f = open('train.txt','r')
text = f.readlines()
f.close()
messages = []
scores = []
for l in text:
    message,score = l.split('^')
    messages.append(message)
    scores.append(int(score[:-1]))
train = messages
m = MLC(train,scores)
search_coin(currency)
parse_data(currency)
f = open(currency+'.txt')
test = f.readlines()
f.close()
reviews = set(m.get_reviews(test))
f = open('review'+currency+'.txt','w')
for l in reviews:
    f.write(l+'\n')
f.close()



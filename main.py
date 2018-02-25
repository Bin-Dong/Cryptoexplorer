from  get_introduction import *
from  get_api import *
from machine_learning_classfication import *

currency = get_coin_info()
get_introduction(currency)
# messages = get_Twitter_result(currency)
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
f = open('review'+currency+'.txt','w')
for l in reviews:
    f.write(l+'\n')
f.close()



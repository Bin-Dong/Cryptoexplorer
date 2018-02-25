import pickle
# '''database[full coin name] = [ average rating,number of raters, [ [rating,comment], .....] ]'''


def write_comment(name,comment,rating=None):
    '''accept full crypto currency name, user comments, and ratings'''
    database[name][0] = (database[name][0]*database[name][1]+rating)/(database[name][1]+1)
    database[name][1] += 1    # increase the counter by one
    database[name][2].append([rating,comment])

def create_mapping():
    f = open("mapping.txt", "r")
    currency_list = f.readlines();
    f.close()
    mapping = {}
    for line in currency_list:
        split = line.split(':')
        if split[0] not in mapping:
            mapping[split[0]] = []
        mapping[split[0]].append(split[1][0:-1])
    return mapping

def create_database():
    new_database = {}
    f = open("mapping.txt", "r")
    currency_list = f.readlines()
    f.close()
    for line in currency_list:
        split = line.split(":")
        new_database[split[1][0:-1]] = [0,0,[]] #rating is index 0, counter is index 1, and list of comments is index 2.
    return new_database;

def list_comment(name):
    return database[name][0], database[name][1], database[name][2]

def delete_comment(name,index):
    '''delete the comment on the website
        index = the index of that comment
        name = the full coin name'''
    database[name][2].pop(index)

def delete_currency(name):
    database.pop(name)

def save_database():
    f = ('dataset.pkl','wb')
    pickle.dump(database,f,-1)
    f.close()

def load_database():
    f = open('dataset.pkl','rb')
    database = pickle.load(f)
    f.close()

database = create_database()
mapping = create_mapping()
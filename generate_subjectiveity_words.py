import pickle

def generate_expressive_subjectivity_features():
    '''generate a list of binary features for subjectivity words'''
    corpus_root = r'mpqa_2_0_database/'
    f = open(corpus_root + 'doclist.mpqaOriginalSubset')
    filenames = f.read().splitlines()
    f.close()
    expressive_subjectivity_words = {}
    for filename in filenames:
        doc = open(corpus_root + 'docs/' + filename, 'rb')  # the original text file
        a = open(corpus_root + 'man_anns/' + filename + '/gateman.mpqa.lre.2.0', 'r')  # the annotation file
        annotation = a.read().splitlines()
        for line in annotation[5:]:
            split_info = line.split('\t')
            start, end = split_info[1].split(',')
            start = int(start)
            end = int(end)
            word_type = split_info[3]
            if word_type == 'GATE_expressive-subjectivity':
                doc.seek(start, 0)
                word = doc.read(end - start).decode('utf-8').lower()
                if word in expressive_subjectivity_words:
                    expressive_subjectivity_words[word] += 1
                else:
                    expressive_subjectivity_words[word] = 1
        doc.close()
    sorted_words = sorted(expressive_subjectivity_words, key=expressive_subjectivity_words.get, reverse=True)
    f = open('expressive_subjectivity_words.pkl','wb')
    pickle.dump(sorted_words,f,-1)
    f.close()

def generate_direct_subjectivity_features():
    '''generate a list of binary features for subjectivity words'''
    corpus_root = r'mpqa_2_0_database/'
    f = open(corpus_root + 'doclist.mpqaOriginalSubset')
    filenames = f.read().splitlines()
    f.close()
    direct_subjectivity_words = {}
    for filename in filenames:
        doc = open(corpus_root + 'docs/' + filename, 'rb')  # the original text file
        a = open(corpus_root + 'man_anns/' + filename + '/gateman.mpqa.lre.2.0', 'r')  # the annotation file
        annotation = a.read().splitlines()
        for line in annotation[5:]:
            split_info = line.split('\t')
            start, end = split_info[1].split(',')
            start = int(start)
            end = int(end)
            word_type = split_info[3]
            if word_type == 'GATE_direct-subjective' and end-start >= 2:
                doc.seek(start, 0)
                word = doc.read(end - start).decode('utf-8').lower()
                if word in direct_subjectivity_words:
                    direct_subjectivity_words[word] += 1
                else:
                    direct_subjectivity_words[word] = 1
        doc.close()
    sorted_words = sorted(direct_subjectivity_words, key=direct_subjectivity_words.get, reverse=True)
    f = open('direct_subjectivity_words.pkl','wb')
    pickle.dump(sorted_words,f,-1)
    f.close()

generate_expressive_subjectivity_features()
generate_direct_subjectivity_features()
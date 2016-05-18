import nltk
import gzip
import sys
import MeCab

jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^！？。]*[！？。]?')
word_index = {}
word_count = {}
node_surface_list = []
tagger = MeCab.Tagger('')
tagger.parse(' ')

def ngram(n, node_surface_list, word_count, word_index):
    for i in range(len(node_surface_list) - n + 1):     # 先頭にしたときにn-gramがとれる各単語について
        ng = "/".join(node_surface_list[i:i + n])       # ngramをとって追加していく
        if ng not in word_index:
            new_index = len(word_index) + 1
            word_index[ng] = new_index
        if word_index[ng] in word_count:
            word_count[word_index[ng]] += 1
        else:
            word_count[word_index[ng]] = 1
    return

text = gzip.open(sys.argv[1],'rt',encoding='utf-8').read()
reviews = text.split('\n')
del reviews[-1]
for review in reviews:
    node_surface_list = []
    sents = jp_sent_tokenizer.tokenize(review)
    del sents[-1]
    for sent in sents:
        node = tagger.parseToNode(sent)
        while node:
            node_surface_list.append(node.surface)
            node = node.next

    if sys.argv[2] == 'unigram':
        for i in range(len(node_surface_list)):
            uni = node_surface_list[i]
            if uni not in word_index:
                new_index = len(word_index) + 1
                word_index[uni] = new_index
            if word_index[uni] in word_count:
                word_count[word_index[uni]] += 1
            else:
                word_count[word_index[uni]] = 1
        for k,v in sorted(word_count.items(),key=lambda x:x[0]):
            print(str(k) + ':' + str(v) + ' ',end='')      
        print()
        word_count = {}

    if sys.argv[2] == 'bigram':
        for i in range(len(node_surface_list) - 1):
            bi =  node_surface_list[i] + node_surface_list[i+1]
            if bi not in word_index:
                new_index = len(word_index) + 1
                word_index[bi] = new_index
            if word_index[bi] in word_count:
                word_count[word_index[bi]] += 1
            else:
                word_count[word_index[bi]] = 1
        for k,v in sorted(word_count.items(),key=lambda x:x[0]):
            print(str(k) + ':' + str(v) + ' ',end='')
        print()
        word_count = {}

    if sys.argv[2] =='trigram':
        for i in range(len(node_surface_list) - 2):
            tri = node_surface_list[i] + node_surface_list[i+1] + node_surface_list[i+2]
            if tri not in word_index:
                new_index = len(word_index) + 1
                word_index[tri] = new_index
            if word_index[tri] in word_count:
                word_count[word_index[tri]] += 1
            else:
                word_count[word_index[tri]] = 1
        for k,v in sorted(word_count.items(),key=lambda x:x[0]):
            print(str(k) + ':' + str(v) + ' ',end='')
        print()
        word_count = {}

    if sys.argv[2] == 'ngram':
        ngram(int(sys.argv[3]),node_surface_list, word_count, word_index)
        for k,v in word_count.items():
            print(str(k) + ':' + str(v) + ' ',end='')
        print()

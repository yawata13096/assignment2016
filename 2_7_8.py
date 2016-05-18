import nltk
import gzip
import sys
import MeCab

jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^！？。]*[！？。]?')
word_index = {}
word_count = {}
tagger = MeCab.Tagger('')
tagger.parse(' ')

#def ngram(n_, surface_list_, word_count_, word_index_):
#    for i in range(len(surface_list_) - n_ + 1): # 先頭にしたときにn-gramがとれる各単語について
#        ng = "/".join(surface_list_[i:i+n_]) # ngramをとって追加していく
#        if ng not in word_index_:
#            new_index = len(word_index_) + 1
#            word_index_[ng] = new_index
#        if word_index_[ng] in word_count_:
#            word_count_[word_index_[ng]] += 1
#        else:
#            word_count_[word_index_[ng]] = 1
#    return

def unigram():
    if not node.surface == '':
        if node.surface not in word_index:
            new_index = len(word_index) + 1
            word_index[node.surface] = new_index
        if word_index[node.surface] in word_count:
            word_count[word_index[node.surface]] += 1
        else:
            word_count[word_index[node.surface]] = 1

def bigram():
    i = 0
    for i in range(len(node_surface_list) - 1):
        bi_word = node_surface_list[i] + node_surface_list[i+1]
        i += 1
        if bi_word not in word_index:
            new_index = len(word_index) + 1
            word_index[bi_word] = new_index
        if word_index[bi_word] in word_count:
            word_count[word_index[bi_word]] += 1
        else:
            word_count[word_index[bi_word]] = 1

def trigram():
    i = 0
    for i in range(len(node_surface_list) - 2):
        tri_word = node_surface_list[i] + node_surface_list[i+1] + node_surface_list[i+2]
        i += 1
        if tri_word not in word_index:
            new_index = len(word_index) + 1
            word_index[tri_word] = new_index
        if word_index[tri_word] in word_count:
            word_count[word_index[tri_word]] += 1
        else:
            word_count[word_index[tri_word]] = 1

text = gzip.open(sys.argv[1],'rt',encoding='utf-8').read()
reviews = text.split()
node_surface_list = []
for review in reviews:
    sents = jp_sent_tokenizer.tokenize(review)
    del sents[-1]

    for sent in sents:
        node = tagger.parseToNode(sent)
        if sys.argv[2] == 'unigram':
            while node:
                unigram()
                node = node.next
        if sys.argv[2] == 'bigram' or 'trigram':
            while node:
                node_surface_list.append(node.surface)
                node = node.next
            
    if sys.argv[2] == 'bigram':
        bigram()
    if sys.argv[2] == 'trigram':
        trigram()

    for k,v in word_count.items():
        print(str(k) + ':' + str(v) + ' ',end='')      
    print()
    word_count = {}

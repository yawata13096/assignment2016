import nltk
import gzip
import sys
import MeCab

jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^！？。]*[！？。]?')
word_index = {}
word_count = {}
tagger = MeCab.Tagger('')
tagger.parse(' ')
content_list = ['名詞','動詞','形容詞','形容動詞','副詞']

text = gzip.open(sys.argv[1],'rt',encoding='utf-8').read()
reviews = text.split()
for review in reviews:
    sents = jp_sent_tokenizer.tokenize(review)
    del sents[-1]
    for sent in sents:
        node = tagger.parseToNode(sent)
        while node:
            if not node.surface == '':
                if node.feature.split(',')[0] in content_list:
                    if node.surface not in word_index:
                        new_index = len(word_index) + 1
                        word_index[node.surface] = new_index
                    if word_index[node.surface] in word_count:
                        word_count[word_index[node.surface]] += 1
                    else:
                        word_count[word_index[node.surface]] = 1
            node = node.next
    for k,v in word_count.items():
        print(str(k) + ':' + str(v) + ' ',end='')
        word_count = {}
    print()

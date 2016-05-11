import nltk
import gzip
import sys
jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^！？。]*[！？。]?')

sents = gzip.open(sys.argv[1],'rt',encoding='utf-8').read()
first = sents.split()[0]
sent= jp_sent_tokenizer.tokenize(first)
del sent[-1]
print(sent)

import nltk
import sys
import shelve
word_count={}
sh_word_index=shelve.open("word_shelf")
f=open(sys.argv[1])
f1=f.read()
f.close()
sents=nltk.sent_tokenize(f1)
for sent in sents:
    words=nltk.word_tokenize(sent)
    for word in words:
        if word not in sh_word_index:
            new_index=len(sh_word_index)+1
            sh_word_index[word]=new_index
        if word in word_count:
            word_count[sh_word_index[word]]+=1
        else:
            word_count[sh_word_index[word]]=1
for key,value in word_count.items():
    print(str(key)+':'+str(value)+' ',end='')
print()
sh_word_index.close()

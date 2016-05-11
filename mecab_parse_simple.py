import MeCab
tagger = MeCab.Tagger('')
tagger.parse(' ')
node = tagger.parseToNode('「豊工に行っています。」')
while node:
    print('%s %s %s' %(node.surface, node.feature.split(',')[1], node.feature.split(',')[6]))
    node = node.next

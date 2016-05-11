import CaboCha
parser = CaboCha.Parser('-n1 -f1')
tree = parser.parse('「豊工に行っています。」')
for i in range(tree.token_size()):
    token = tree.token(i)
    if not len(token.ne)==1 :
        print(token.surface,'\t',token.ne)

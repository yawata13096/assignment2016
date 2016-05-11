import CaboCha
parser = CaboCha.Parser()
tree = parser.parseToString('「豊工へ行っています。」')
for bunsetsu in tree.split():
    print(bunsetsu) 

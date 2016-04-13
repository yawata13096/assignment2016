import sys
dic={}
for x in open(sys.argv[1],'r'):
    y=x.strip().split(" ")
    for z in y:
        if z in dic:
            dic[z]+=1
        else:
            dic[z]=1
for key,value in sorted(dic.items(),key=lambda A:A[1],reverse=True):
    print(value,key)
            

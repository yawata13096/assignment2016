import sys
for evaluation in open(sys.argv[1]):
    if int(evaluation) >= 4:
        print(1)
    else:
        print(-1)

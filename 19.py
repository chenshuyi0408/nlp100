from collections import Counter
from sys import argv
col1=[]
with open(argv[1]) as files:
    f=files.readlines()
for a in f:
    f2=a.replace("\t"," ")
    f3=f2.split(" ")
    col1.append(f3[0]+"\n")
number_counter = Counter(col1)
for i in number_counter.most_common():
    print(i)
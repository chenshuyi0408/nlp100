from sys import argv
col1=[]
col2=[]
with open(argv[1]) as files:
    f=files.readlines()

for a in f:
    f2=a.replace("\t"," ")
    f3=f2.split(" ")
    col1.append(f3[0]+"\n")
    col2.append(f3[1]+"\n")
with open("col1.txt","w") as z:
    z.write("".join(col1))
with open("col2.txt","w") as x:
    x.write("".join(col2))




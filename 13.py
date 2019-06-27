from sys import argv
merge=[]
with open(argv[1]) as col1:
    col1=col1.readlines()
with open(argv[2]) as col2:
    col2=col2.readlines()
for i in range(len(col1)):
    merge.append(col1[i]+"\t"+col2[i]+"\n")
print(merge)

with open("merge.txt","w") as z:
    z.write("".join(merge))
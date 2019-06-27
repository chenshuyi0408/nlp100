from sys import argv
x=int(input())
fix=[]

with open(argv[1]) as lines:
    f=lines.readlines()

for i in range(len(f)):
    if i<x:
        fix.append(f[i])
print (fix)
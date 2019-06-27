from sys import argv
x=int(input())
fix=[]

with open(argv[1]) as lines:
    f=lines.readlines()
a=len(f)
for i in range(a):
    if i>=a-x:
        fix.append(f[a-i])
print (fix)
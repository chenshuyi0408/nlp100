from sys import argv
N=int(input())
with open(argv[1]) as lines:
    f=lines.readlines()
x=ceil(N/len(f))


from sys import argv
import math
N=int(input())
with open(argv[1]) as lines:
    f=lines.readlines()
x=math.ceil(N/len(f))
f=f[::x]
print(f)

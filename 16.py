import math
N=int(input())
z=[]
with open('hightemp.txt') as lines:
    f=lines.readlines()
x=math.ceil(len(f)/N)
print(len(f)/N)
for i in range(len(f)):
    if (i+1)%x==0:
        print(f[i].strip())
        print('-----')
    else:
        print(f[i].strip())




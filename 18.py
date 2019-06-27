from sys import argv
with open(argv[1]) as files:
    f=files.readlines()
ahh=sorted(f,key=lambda x:x[2],reverse=True)
for i in ahh:
    print(i.strip())

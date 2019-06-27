from sys import argv

with open(argv[1]) as start_file:
    line = len(start_file.readlines())


print(line)
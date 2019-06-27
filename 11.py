from sys import argv

with open(argv[1]) as file:
    files=file.read()
file2=files.replace("  ", " ")
print(file2)
# 1st way f = open("new_file.txt", "rt")
# f = open("new_file.txt")
f = open("new_file.txt", "r")

print(f.read())
# Read specific parts of a file
f = open("new_file.txt", "r")
# print(f.read(12))
# print(f.readline()) # read a line
# print(f.readline())

for x in f:
    print(x)
f.close()
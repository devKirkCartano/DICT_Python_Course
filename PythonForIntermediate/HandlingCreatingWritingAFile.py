# Create new file
# f = open("new_file.txt", "x")

# Write to file, overwrite, create new file if not exist
f = open("new_file.txt", "w")
f.write("Introduction to Python")

# Read a file
f = open("new_file.txt", "r")
# print(f.read())

# To append to existing file
f = open("new_file.txt", "a")
f.write("\nPython intermediate")
f = open("new_file.txt", "r")
print(f.read())
f.close()

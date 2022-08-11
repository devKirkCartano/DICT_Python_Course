import os 
# f = open("new_file.txt", "r")

# print(f.read())

# f = open("new_file.txt", "r")

# print(f.readline())
# for x in f:
    # print(x)
if os.path.exists("new_file.txt"):
    os.remove("new_file.txt")  # deletes a file
    print("File deleted successfully") 
else:
    print("File does not exist")
# os.remove("new_file.txt") # deletes a file
# f.close()

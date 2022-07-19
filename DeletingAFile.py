import os
# If not sure if a file exists, use os.path.exists()
if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("File deleted successfully")
else:
    print("The file does not exist")

# If sure
os.remove("try.txt")

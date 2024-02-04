import os

source = "test.txt"
destination = "C:\\Users\\91755\\OneDrive\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("Already a file present")
    else:
        os.read(source,destination)
        print(source+ "moved")
except FileNotFoundError:
    print(source + "not found")
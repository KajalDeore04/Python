import os

try:
    os.remove('C:\\Users\\91755\\OneDrive\\Desktop\\Test.txt')
except FileNotFoundError:
    print("File not found")

#os.rmdir()   to remove folder , doesnt delete if not empty, need shutil module
#os.rmtree()   removes even if not empty

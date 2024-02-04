import os

#copy the path of file you need to detect
#needs double back slash - escape sequence for a backslash within a string

path = "C:\\Users\\91755\\OneDrive\\Desktop\\Test.txt"

if os.path.exists(path):             #check if file present
    print("Location exists!")
    if os.path.isfile(path):          #checks if that's a file
        print("That's a file")
    elif os.path.isdir(path):         #checks if that's a directory/folder
        print("That's a directory")
else:
    print("does not exist")

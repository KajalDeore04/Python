
#with open('test.txt')     #only file name if within project folder

with open('C:\\Users\\91755\\OneDrive\\Desktop\\Test.txt') as file:  #after using with open file automaticlally closes but doesnt catch exception like file not located
    print(file.read())                                              #make sure you save the text u have written in the text file

#print(file.close())             prints true of file closed and vice versa

try:
    with open('C:\\Users\\91755\\OneDrive\\Desktop\\Test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
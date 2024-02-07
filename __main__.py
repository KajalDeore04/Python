# Suppose we have a file named Kajal.py with function
def welcome():
    print("Namaste")

welcome()
# And we have a main.py file where we import kajal file and write
import Kajal
Kajal.welcome()

# and run the the program program, then Namaste will be printed twice
# one because of function call in kajal.py and second because of importing and calling function
# if we remove welcome() from Kajal.py then it will be printed once
# to avoid such problems of being printed twice
# we write
if __name__ = "__main__":
    welcome()
# this will print only one time because we mentioned call the function only when its main file

#The if __name__ == "__main__" idiom is a common pattern
# used in Python scripts to determine whether the script
# is being run directly or being imported as a module into another script.
#This idiom is useful because it allows you to reuse code from a script by importing it as a module
# into another script, without running the code in the original script
a = int(input("Enter age\n"))
print("Your age:", a)

# Conditional Operators
# <, >, !=, ==, <=, >=

# print(a<18)       #bools returning true or false just like conditions
# print(a>18)
# print(a<=18)
# print(a>=18)
# print(a==18)
# print(a!=18)


if(a>18):
    print("Drive")        # has indentations- the spaces before line, just like braces

elif(a==18) :
    print("wait")

else:
    print("dont drive")




''' Quiz'''
print("Quiz Time")
# greets according to time using time module

import time                            #imports local time if on your local system

current_time = time.strftime('%H:%M:%S')     #strftime- "string format time." method in time module
print(current_time)


hour = int(time.strftime('%H'))        # strftime gives time in string so converted it into int
print(hour)

if(hour < 12):
    print("Good Morning")

elif(12 < hour & hour < 20 ):
    print("afternoon")

else:
    print("night")


# The strftime function takes a format string as an argument, which specifies the desired format for the output string.
#
# Here's a brief overview of the format codes commonly used with strftime:
#
# %Y: Year with century as a decimal number (e.g., 2024).
# %m: Month as a zero-padded decimal number (01, 02, ..., 12).
# %d: Day of the month as a zero-padded decimal number (01, 02, ..., 31).
# %H: Hour (00, 01, ..., 23).
# %M: Minute (00, 01, ..., 59).
# %S: Second (00, 01, ..., 59).
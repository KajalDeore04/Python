# performs tasks when called
a = 9
b = 8
mean1 = (a*b)/(a+b)
print(mean1)

c = 10
d = 15
mean2 = (c*d)/(c+d)
print(mean2)

# to encapsulate the logic of above instead of writing separetly we use function

def mean(a,b):
    '''this is a docstring can contain logic or any comment
    but it is different than comment coz if u print --doc-- then it prints unlike comments'''
    mean = (a*b)/(a+b)
    print(mean)
    print(mean.__doc__)

print("I am using function")
mean(15,4)


def perimeter(a,b):
    pass                 # used when we want to write the body later so that it does not throw any error



#Types of arguments
# 1.Default
def average(a=5, b=9):
     print("Average is:", (a+b)/2)
#
# 2. Keyword
average(b=9,a=5)   #sequence can be changed
#
# # 3. required
def average(a, b = 9):
    print("Average is:", (a+b)/2)   #a is required to run this function

# 4. Variable length arguments (VarAgrs)
def average(*numbers):                    # takes arguments as a tuple
    for i in numbers:
        sum = 0
        sum = sum + i
    print("Average is:", sum/len(numbers))     #will take as many as we provide


average(5,4,6,8,9)

# if used ** in argument then takes agrument as a dictionary

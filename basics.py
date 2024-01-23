# IN PYTHON EVERYTHING IS OBJECT

# printing
print("hello")
print(65)
print("hello", 8)
print(8*7)

# new line print
print("no\nway")

'''
multiline comment
'''



#quotes in text / escape sequence
print("hey \"girl\"")

#separator and end
print("hey ", 7, 8, sep=" $", end="\n009\n")



#variable
a=1
print(a)

b="kajal"
print(b)

c=True
print(c)

d=None
print(d)
#cant concatenate two diff data types using +









#data types

print("type of var a is", type(a))  #gives data type of provided variable
print("type of var b is", type(b))
print("type of var c is", type(c))
print("type of var d is", type(d))




#complex number
e=complex(8,-5)      #forms complex number
print(e)
print("data type of e", type(e))





# list is collection of elements of same or diff data types (mutable)

list=[8,2.3,[-4,5],["apple", "banana"]]
print(list)

# tuple is same as list but (immutable / cant change)

tuple=[8,2.3,[-4,5],["apple", "banana"]]
print(tuple)

#mapped data : dictionary  = collection of key and value (pairs)

dict={"name":"kajal" , "age":19 , "vote":True}
print(dict)








#operators
print(5+8)
print(5-8)
print(5*8)
print(5/8)
print(5//8)   # floor division - quotient without decimal point
print(5%8)
print(5**8)   # 5 , 8 times or 5 raised to 8





#typecasting - convert one data type to another
num1 = "1"
num2 = "2"
print(num1+num2)  # will print 12 as both are provided as a string

print(int(num1)+int(num2)) #even if its string the int function will convert the string into integer and then perform op

# 1. explicit typecasting - done by programmer (e.g. above)
# 2. inmplicit typecasting - after operating , lower order data types gets converted into higher order data type

print(2+4.5) # answer will be float due to implicit typecasting



#formating a number

number = 3.14159
print("the number pi is {:.2f}".format(number))      # prints till two numbers after decimal

cash = 10000000
print("I have cash of  {:,}".format(cash))          # adds comma on appropriate place
print("I have cash of  {:b}".format(cash))          # binary
print("I have cash of  {:o}".format(cash))          # octal
print("I have cash of  {:x}".format(cash))          # hexadecimal
print("I have cash of  {:E}".format(cash))          # scientific notation



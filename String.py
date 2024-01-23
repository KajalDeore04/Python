#Strings are immutable

# single line string
me = "Kajal"
friend = 'J'            # element inside single quote is considered as a string too
print("hello..." + me)  #concatenates
print("hello..." , me)

print(me[0])     #indexing from 0 so will print letter at 0th pos
#print(me[5])    #index error




# multiline string
i = '''Hello                     
       Good Morning
       How are you?'''         #if without quotes then EOL (end of line) error
print(i)                       # Prints as it is on individual lines and same number of spaces

#loop through the string to access
print("loop through the string to access")
for character in i:
    print(character)


# format function

# animal = "cow"
# place = "moon"

#print(animal , "jumped over the",place)

# print("{} jumped over the {}".format("cow", "moon"))
# print("{} jumped over the {}".format(animal,place))
# print("{1} jumped over the {0}".format(animal,place))        #positional argument
print("{animal} jumped over the {place}".format(animal = "cow",place = "moon"))


name = "Python"
print("hello my name is {:10}. how are you".format(name))     # adds padding of 10 spaces
print("hello my name is {:<10}. how are you".format(name))    #aligns to left
print("hello my name is {:>10}. how are you".format(name))    #aligns to right
print("hello my name is {:^10}. how are you".format(name))    #aligns to center






#STRING SLICING
print("STRING SLICING")
print(i[0:5])  #prints elements in i from index 0 to 4
print(i[:5])   #auto zero
print(i[:])    #0 to length
print(i[0:-3]) #negative slicing= length-3
print(me[-1:-3])  #from 4th to 2nd which doesnt makes sense




print("LENGTH")
print(len(me))  #prints length
fruit = " I love Mango"
print("length of fruit string is", len(fruit))







'''QUIZ'''
nm = "Kajal"
print(nm[-4:-2])     #prints length-4(1) to previous of length-2(3)  answer = aj






#STRING METHODS
print("STRING METHODS")
a = "Apple !!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.swapcase())       #lower to upper and vice versa
print(a.rstrip("!"))      #removes ! from behind only
print(a.replace("Apple","Mango"))   #all apples in string will be replaced
print(a.split(" "))       #splits strings if encounter spaces into list
print(a.capitalize())     #caps to the first letter only
print(a.center(50))       #moves string to center by adding 50 spaces
print(a.count("p"))       #shows repetition
print(a.endswith("e"))    #bool tells if string ends with e or not
print(a.startswith("A"))  #case sensetive
b = "Welcome to the console"
print(b.endswith("to",4,10))  #considers string from index 4 to 9 and checks if ends with to
print(b.find("to"))       # finds the starting pos of to , exits with -1 if not found
#print(b.index("a"))       #exits with error if a not found
print(b.isalnum())         #checks if alphanumeric
print(b.isalpha())         #false if numbers,spaces,punctuations present
print(b.islower())         #check if all lower
print(b.isupper())
print(b.isprintable())     #false if /n like characters are present
print(b.isspace())         #true if only spaces are present
print(b.istitle())         #true if first letter of each word cap
print(b.title())           #every first letter of every word cap











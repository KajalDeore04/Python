# tuple - ordered and unchangable collection , groups related data

student = ("Marie",24,"female")

print(student.count("Marie"))     # shows how many times its repeated
print(student.index("female"))     # gives index of that element

for i in student:                 # prints tuple
    print(i)

if "Marie" in student:            #checks if present
    print("Present")


#student.append(" kajal")       can not be appended as tuple is unchangable